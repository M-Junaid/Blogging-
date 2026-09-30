# Blogging Platform

A simple Django-based blogging and gallery application for showcasing flower posts, editing entries, and deleting content through a clean web interface.

## Features

- Product/blog listing page
- Blog detail view
- Create, edit, and delete blog entries
- Image upload support using Django media files
- Responsive Bootstrap-based UI
- Admin panel support for content management

## Tech Stack

- Python 3.11
- Django 5.2
- SQLite
- Pillow
- Bootstrap 4

## Project Structure

```text
blogsite/
├── blogsite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── gallery/
│   ├── templates/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── manage.py
├── db.sqlite3
├── media/
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/M-Junaid/Blogging-.git
cd Blogging-
```

2. Create and activate a virtual environment

```bash
python -m venv myproject
myproject\Scripts\activate
```

3. Install dependencies

```bash
pip install django pillow
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Usage

- Visit the homepage to view all blog entries.
- Click a blog card to see its full details.
- Use the edit and delete links to manage entries.
- Use the Django admin panel for backend-management features.

## Screenshots

The project displays a blog listing page with flower-themed content and image cards.

## License

This project is for educational and portfolio purposes.

## Author

M Junaid
