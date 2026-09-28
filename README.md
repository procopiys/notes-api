# Notes API

REST API для управления пользователями и заметками.

Проект разработан в рамках учебной практики по backend-разработке.

## Стек технологий

- Python 3.14
- Flask
- SQLAlchemy
- PostgreSQL
- pytest
- Docker
- Docker Compose
- Git / GitHub
- Postman

## Возможности

API поддерживает:

- создание пользователей;
- создание заметок;
- получение списка заметок;
- получение информации о пользователе;
- фильтрацию заметок;
- пагинацию;
- связь пользователей и заметок;
- работу с PostgreSQL;
- автоматические тесты;
- запуск в Docker.

## Структура проекта

```text
notes-api/
├── tests/
│   ├── conftest.py
│   └── test_api.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md

Запуск проекта

Docker
    Установить Docker Desktop.
        Клонировать репозиторий:
            git clone https://github.com/YOUR_USERNAME/notes-api.git
            cd notes-api

        Запустить проект:
            docker compose up --build
        
        После запуска API доступен по адресу:
            http://127.0.0.1:5000

        Остановить контейнеры:
            docker compose down

API
    Получить список заметок
        GET /api/notes
    
    Пример: 
        curl http://127.0.0.1:5000/api/notes
    
    Создать пользователя
        POST /api/users
        Content-Type: application/json
    Тело запроса:
        {
            "username": "Pro",
            "email": "pro@example.com"
        }

    Создать заметку
        POST /api/notes
        Content-Type: application/json
    Тело запроса:
        {
            "user_id": 1,
            "title": "Изучение Flask",
            "content": "Создание REST API на Flask"
        }

    Получить заметку
        GET /api/notes/<id>
    Пример:
        curl http://127.0.0.1:5000/api/notes/1

    Изменить заметку
        PUT /api/notes/<id>
        Content-Type: application/json
    Пример:
        {
            "title": "Изучение Flask и PostgreSQL",
            "content": "Обновлённая заметка"
        }

    Удалить заметку
        DELETE /api/notes/<id>
    Пример:
        curl -X DELETE http://127.0.0.1:5000/api/notes/1

Фильтрация и пагинация
    Получение заметок с поиском:
        GET /api/notes?search=Flask

    Пагинация:
        GET /api/notes?page=1&per_page=10

Тестирование
    Для запуска тестов используется pytest.
        Активировать виртуальное окружение:
            venv\Scripts\activate

        Запустить тесты:
            python -m pytest

Docker
    Проект запускается с использованием Docker Compose.
        Архитектура приложения:
              Client
                │
                ▼
             Flask API
                │
                ▼
            SQLAlchemy
                │
                ▼
            PostgreSQL

    Контейнеры:
        notes-api
        notes-postgres

    Проверить состояние контейнеров:
        docker compose ps

    Посмотреть логи:
        docker compose logs

Переменные окружения
    Секретные данные хранятся в .env.
        Пример:
            DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/notes_db

    Файл .env не должен публиковаться в GitHub.

Автор
Слепцов Прокопий
Учебная практика по backend-разработке.