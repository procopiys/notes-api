# 📝 Notes API

REST API для управления пользователями и заметками.

Учебный backend-проект, разработанный в рамках учебной практики.

---

## 🛠️ Стек технологий

- Python 3.14
- Flask
- SQLAlchemy
- PostgreSQL
- pytest
- Docker
- Docker Compose
- Gunicorn
- Postman
- Git / GitHub

---

## 🚀 Возможности

API поддерживает:

- 👤 создание пользователей;
- 📝 создание заметок;
- 📋 получение списка заметок;
- 🔎 получение отдельной заметки;
- ✏️ изменение заметок;
- 🗑️ удаление заметок;
- 🔍 фильтрацию заметок;
- 📄 пагинацию;
- 🔗 связь пользователей и заметок;
- 🗄️ работу с PostgreSQL;
- 🧪 автоматические тесты;
- 🐳 запуск приложения в Docker.

---

## 📁 Структура проекта

```text
notes-api/
│
├── tests/
│   └── test_api.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md
```

---

# ▶️ Запуск проекта

## 🐳 Запуск через Docker

Убедитесь, что установлен Docker Desktop.

### 1. Клонирование репозитория

```bash
git clone https://github.com/procopiys/notes-api.git
cd notes-api
```

### 2. Запуск проекта

```bash
docker compose up --build
```

После запуска API будет доступен по адресу:

```text
http://127.0.0.1:5000
```

### 3. Остановка контейнеров

```bash
docker compose down
```

---

# 🌐 API

## 📋 Получить список заметок

GET

```text
/api/notes
```

Пример:

```bash
curl http://127.0.0.1:5000/api/notes
```

---

## 👤 Создать пользователя

POST

```text
/api/users
```

Заголовок:

```text
Content-Type: application/json
```

Тело запроса:

```json
{
    "username": "Pro",
    "email": "pro@example.com"
}
```

---

## 📝 Создать заметку

POST

```text
/api/notes
```

Заголовок:

```text
Content-Type: application/json
```

Тело запроса:

```json
{
    "user_id": 1,
    "title": "Изучение Flask",
    "content": "Создание REST API на Flask"
}
```

---

## 🔎 Получить отдельную заметку

GET

```text
/api/notes/<id>
```

Пример:

```bash
curl http://127.0.0.1:5000/api/notes/1
```

---

## ✏️ Изменить заметку

PUT

```text
/api/notes/<id>
```

Заголовок:

```text
Content-Type: application/json
```

Тело запроса:

```json
{
    "title": "Изучение Flask и PostgreSQL",
    "content": "Обновлённая заметка"
}
```

---

## 🗑️ Удалить заметку

DELETE

```text
/api/notes/<id>
```

Пример:

```bash
curl -X DELETE http://127.0.0.1:5000/api/notes/1
```

---

# 🔍 Фильтрация и пагинация

## Поиск заметок

```http
GET /api/notes?search=Flask
```

## Пагинация

```http
GET /api/notes?page=1&per_page=10
```

---

# 🧪 Тестирование

Для тестирования используется pytest.

### 1. Активировать виртуальное окружение

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 2. Запустить тесты

```powershell
python -m pytest
```

При успешном выполнении тестов pytest должен показать:

```text
PASSED
```

---

# 🐳 Docker

Проект запускается с помощью Docker Compose.

## Архитектура приложения

```text
             Client
                │
                ▼
        Flask / Gunicorn
                │
                ▼
           SQLAlchemy
                │
                ▼
           PostgreSQL
```

## Контейнеры

```text
notes-api
notes-postgres
```

### Проверить состояние контейнеров

```powershell
docker compose ps
```

### Посмотреть логи

```powershell
docker compose logs
```

### Остановить проект

```powershell
docker compose down
```

---

# 🔐 Переменные окружения

Секретные данные хранятся в файле:

```text
.env
```

Пример:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/notes_db
```

> ⚠️ Файл `.env` не должен публиковаться в GitHub.

Он добавлен в `.gitignore`.

---

# 📦 Зависимости

Зависимости проекта находятся в:

```text
requirements.txt
```

Установка:

```powershell
pip install -r requirements.txt
```

Обновление списка зависимостей:

```powershell
pip freeze > requirements.txt
```

---

# 📌 Статус проекта

| Компонент | Статус |
|---|---|
| Flask API | ✅ |
| CRUD | ✅ |
| SQLAlchemy | ✅ |
| PostgreSQL | ✅ |
| Docker | ✅ |
| Docker Compose | ✅ |
| Gunicorn | ✅ |
| pytest | ✅ |
| Git | ✅ |
| GitHub | 🚧 |
| Деплой | 🚧 |

---

# 👨‍💻 Автор

**Слепцов Прокопий**

Учебная практика по backend-разработке.

---

## 📄 Лицензия

Учебный проект. Используется в образовательных целях.
