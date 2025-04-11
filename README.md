# Team Task Manager API

A simple backend API built with Django and Django REST Framework (DRF) to manage tasks for team members. Includes authentication using JWT and supports task creation, listing, and filtering per user.

## Features

- User registration and login with JWT authentication
- Password validation and email uniqueness checks
- Task CRUD operations (Create, Read, Update, Delete)
- Each task is assigned to the user who created it
- Only authenticated users can access their own tasks

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- Simple JWT
- SQLite (default, can be changed to MySQL/PostgreSQL)

## Installation

1. **Clone the repo**
```bash  
git clone https://github.com/your-username/team-task-manager.git](https://github.com/MohammedAldarwish/Task-Manager-django-DRF.git
cd team-task-manager
````

2. **Activation Virtual env**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````
3. **Install project dependencies**
```bash
pip install -r requirements.txt
````
4. **Apply database migrations**
```bash
python manage.py migrate
````
5. **Run the development server**
```bash
python manage.py runserver
````

## API Endpoints

| Method | Endpoint            | Description               |
|--------|---------------------|---------------------------|
| POST   | /accounts/login/    | Login and get JWT tokens  |
| POST   | /accounts/register/ | Register new user         |
| GET    | /tasks/             | List user tasks (auth)    |
| POST   | /tasks/             | Create a new task (auth)  |
| PUT    | /tasks/{id}/        | Update task (auth)        |
| DELETE | /tasks/{id}/        | Delete task (auth)        |

