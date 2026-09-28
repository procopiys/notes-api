from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#Настройка базы данных Postgres
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#Модель User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

    notes = db.relationship("Note", backref="user", lazy=True)

#Модель Note
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    ) 
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


#Создание таблицы
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {
        "message": "Notes API is running"
        }

#GET — получить все заметки
@app.route("/api/notes", methods=["GET"])
def get_notes():
    search = request.args.get("search")

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    query = Note.query

    # Фильтрация
    if search:
        query = query.filter(
            Note.title.ilike(f"%{search}%")
        )

    # Пагинация
    pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    result = []

    for note in pagination.items:
        result.append({
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "user": {
                "id": note.user.id,
                "username": note.user.username,
                "email": note.user.email
            }
        })

    return {
        "notes": result,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total": pagination.total,
        "pages": pagination.pages
    }

#POST — создать заметку
@app.route("/api/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    user = db.session.get(User, data["user_id"])

    if user is None:
        return {
            "error": "User not found"
        }, 404

    note = Note(
        user_id=data["user_id"],
        title=data["title"],
        content=data["content"]
    )

    db.session.add(note)
    db.session.commit()

    return {
        "id": note.id,
        "user_id": note.user_id,
        "title": note.title,
        "content": note.content
    }, 201

#GET /api/notes/<id> — получить одну заметку
@app.route("/api/notes/int:note_id", methods=["GET"])
def get_note(note_id):
    note = db.session.get(Note, note_id)

    if note is None:
        return {
            "error": "Note not found"
        }, 404

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }

#PUT — изменить заметку
@app.route("/api/notes/int:note_id", methods=["PUT"])
def update_note(note_id):
    data = request.get_json()

    note = db.session.get(Note, note_id)

    if note is None:
        return {
            "error": "Note not found"
        }, 404

    note.title = data["title"]
    note.content = data["content"]

    db.session.commit()

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }

#DELETE — удалить заметку
@app.route("/api/notes/int:note_id", methods=["DELETE"])
def delete_note(note_id):
    note = db.session.get(Note, note_id)

    if note is None:
        return {
            "error": "Note not found"
        }, 404

    db.session.delete(note)
    db.session.commit()

    return {
        "message": "Note deleted successfully"
    }

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()

    user = User(
        username=data["username"],
        email=data["email"]
    )

    db.session.add(user)
    db.session.commit()

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)