# ALX Travel App - Backend

The ALX Travel App is a Django-based backend for a travel listing platform, designed with industry best practices for scalability, maintainability, and team collaboration.

## Project Overview

This project serves as the foundation for a travel platform, providing:

* Robust API backend with Django REST Framework
* MySQL database configuration
* Automated API documentation with Swagger
* Secure environment management
* CORS support for cross-domain requests
* Future-ready task queuing with Celery/RabbitMQ

## Features

* **RESTful API Architecture** : Built with Django REST Framework
* **Automated Documentation** : Interactive Swagger UI at `/swagger/`
* **Secure Configuration** : Environment-based secrets management
* **Cross-Origin Support** : CORS headers for API accessibility
* **MySQL Database** : Production-ready database setup
* **Task Queuing** : Celery + RabbitMQ integration (future implementation)

## Prerequisites

* Python 3.12+
* MySQL 8.0+
* RabbitMQ (for future Celery tasks)
* Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/alx_travel_app.git
cd alx_travel_app
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```text
SECRET_KEY='your-secret-key-here'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

MYSQL_DATABASE=alx_travel_db
MYSQL_USER=alx_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306

# For future Celery tasks
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
```

### 5. Database setup

Create MySQL database and user:

```sql
CREATE DATABASE alx_travel_db;
CREATE USER 'alx_user'@'localhost' IDENTIFIED BY 'your_mysql_password';
GRANT ALL PRIVILEGES ON alx_travel_db.* TO 'alx_user'@'localhost';
FLUSH PRIVILEGES;
```

### 6. Run migrations

```bash
python manage.py migrate
```

## Running the Application

Start the development server:

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## API Documentation

Access interactive API documentation:

* Swagger UI: `http://localhost:8000/swagger/`
* ReDoc: `http://localhost:8000/redoc/`

## Project Structure

```text
alx_travel_app/
├── .env.example                 # Environment variable template
├── .gitignore                   # Git ignore rules
├── manage.py                    # Django management script
│
├── alx_travel_app/              # Main project package
│   ├── __init__.py
│   ├── asgi.py
|   ├── requirement.txt          # Project dependencies
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py
|   └── listings/                # Listings application
        ├── migrations/          # Database migrations
        ├── __init__.py
        ├── admin.py             # Admin configuration
        ├── apps.py              # App configuration
        ├── models.py            # Database models
        ├── tests.py             # Application tests
        ├── urls.py              # App URL routes
        └── views.py             # API views
│   └── README.md

```

## License

This project is for educational purpose within the ALX ProDEV program.
