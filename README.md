# MyPortfolio

A Django portfolio website for showcasing profile information, contact details, and project experience.

## Features

- Home page with personal profile information
- Experience listing and detail pages
- Admin-managed portfolio content
- Cloudinary-backed media storage
- Whitenoise static file handling
- Render-friendly build script

## Tech Stack

- Python
- Django
- SQLite for local development
- PostgreSQL-compatible database configuration through `dj-database-url`
- Cloudinary for uploaded media
- Gunicorn and Whitenoise for production deployment

## Project Structure

```text
myPortfolio/
├── manage.py
├── myPortfolio/
│   ├── settings.py
│   └── urls.py
├── portfolio/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── static/
├── templates/
├── requirements.txt
└── build.sh
```

## Getting Started

1. Clone the repository.

```bash
git clone https://github.com/rkshankar05/MyPortfolio.git
cd MyPortfolio
```

2. Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Create a `.env` file.

```env
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
DB_SSL_REQUIRE=False
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

5. Run migrations.

```bash
python manage.py migrate
```

6. Start the development server.

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Admin

Create a superuser to manage About and Experience content:

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`.

## Deployment

The `build.sh` script installs dependencies, collects static files, and runs migrations:

```bash
./build.sh
```

For production, set the required environment variables in your hosting provider and use Gunicorn to run the app.

## Routes

- `/` - Home page
- `/experience/` - Experience list
- `/experience/<slug>/` - Experience detail
- `/admin/` - Django admin
