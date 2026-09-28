def create_user(client):
    response = client.post(
        "/api/users",
        json={
            "username": "TestUser",
            "email": "test@example.com"
        }
    )

    return response.get_json()


def create_note(client, user_id, title="Test note", content="Test content"):
    response = client.post(
        "/api/notes",
        json={
            "user_id": user_id,
            "title": title,
            "content": content
        }
    )

    return response


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200


def test_create_user(client):
    user = create_user(client)

    assert user["username"] == "TestUser"
    assert user["email"] == "test@example.com"


def test_create_note(client):
    user = create_user(client)

    response = create_note(client, user["id"])

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test note"
    assert data["content"] == "Test content"
    assert data["user_id"] == user["id"]


def test_get_notes(client):
    user = create_user(client)

    create_note(
        client,
        user["id"],
        "Python",
        "Изучаю Python"
    )

    response = client.get("/api/notes")

    assert response.status_code == 200

    data = response.get_json()

    assert "notes" in data
    assert data["total"] == 1
    assert len(data["notes"]) == 1


def test_get_notes_search(client):
    user = create_user(client)

    create_note(
        client,
        user["id"],
        "Python",
        "Изучаю Python"
    )

    create_note(
        client,
        user["id"],
        "Flask",
        "Изучаю Flask"
    )

    response = client.get("/api/notes?search=Python")

    assert response.status_code == 200

    data = response.get_json()

    assert data["total"] == 1
    assert data["notes"][0]["title"] == "Python"


def test_get_notes_pagination(client):
    user = create_user(client)

    for i in range(5):
        create_note(
            client,
            user["id"],
            f"Note {i}",
            f"Content {i}"
        )

    response = client.get(
        "/api/notes?page=1&per_page=2"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["page"] == 1
    assert data["per_page"] == 2
    assert data["total"] == 5
    assert data["pages"] == 3
    assert len(data["notes"]) == 2


def test_create_note_with_invalid_user(client):
    response = create_note(
        client,
        user_id=999
    )

    assert response.status_code == 404


def test_get_nonexistent_note(client):
    response = client.get("/api/notes/999")

    assert response.status_code == 404