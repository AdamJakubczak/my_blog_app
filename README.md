# My Blog App

A simple blog application built with Django, allowing users to register, login, and create, edit, or delete posts. Includes pagination for the blog index page.

## Features

- User registration and authentication
- Create, edit, and delete blog posts
- User-specific post permissions (authors can only modify or delete their own posts)
- Paginated blog index with 3 posts per page
- Flash messages for user interaction feedback

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/my-blog-app.git
    cd my-blog-app
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
