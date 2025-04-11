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
