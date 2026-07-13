# mayor4code

A Django web app for **structured Python learning** — lessons, locked progression, instant quiz scoring, leaderboard, completion certificates, and a live Python playground.

---

## Features

- Register / Login / Logout with show/hide password toggle
- Dashboard with overall progress bar and per-lesson tracking
- 12 complete Python lessons (pre-loaded via seed command)
- Locked progression — each lesson unlocks only after passing the previous quiz (60% pass mark)
- Lesson pages with previous / next navigation
- Multiple-choice quizzes with one-question-per-page UI and instant scoring
- Dark / Light mode toggle — persists across sessions, mobile-friendly
- Auto-issued completion certificates with unique verification codes
- Interactive Python playground with safe sandboxed code execution
- Leaderboard showing top users by average score
- Settings page (update profile, appearance, security)
- Password reset via email
- Admin panel for managing lessons, quizzes, questions, and user progress

---

## Lessons Included

1. Introduction to Python
2. Variables and Data Types
3. Conditional Statements
4. Loops
5. Functions
6. Lists
7. Dictionaries
8. Strings in Depth
9. Tuples and Sets
10. List Comprehensions
11. File I/O
12. Error Handling

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2 |
| Database | SQLite (dev) / PostgreSQL (production) |
| Static Files | WhiteNoise |
| Configuration | python-decouple |
| Frontend | HTML, CSS (custom design system), Vanilla JS |
| Icons | Tabler Icons (webfont CDN) |
| Fonts | Space Grotesk, Inter, JetBrains Mono (Google Fonts) |

---

## Quick Start

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file (see Environment Variables section below)

# 4. Apply migrations
python manage.py migrate

# 5. Seed lessons and quizzes
python manage.py seed_lessons

# 6. Collect static files
python manage.py collectstatic --noinput

# 7. (Optional) Create admin superuser
python manage.py createsuperuser

# 8. Run development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the app.

---

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Email (required for password reset in production)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

> In development (`DEBUG=True`) password reset emails print to the console instead of sending.

---

## Admin Panel

Go to `http://127.0.0.1:8000/admin/` to manage:

- Lessons and lesson HTML content
- Quizzes and questions (options A-D, correct answer)
- User progress records
- Issued certificates

---

## Project Structure

```
mayor4code_final/
├── accounts/           # Auth, dashboard, profile, settings, playground, certificates
├── courses/            # Lesson models, views, seed command
├── quizzes/            # Quiz models and views
├── progress/           # UserLessonProgress and Certificate models
├── templates/
│   ├── base_public.html    # Public pages layout (nav + footer)
│   ├── base_auth.html      # Authenticated pages layout (sidebar)
│   ├── accounts/           # Login, register, dashboard, profile, etc.
│   ├── courses/            # Lesson list and detail
│   ├── quizzes/            # Quiz page
│   └── includes/           # Reusable fragments
├── static/
│   ├── css/                # design-system, components, layout, pages
│   ├── img/                # Favicon, certificate SVG
│   └── sw.js               # Service worker (PWA caching)
├── config/             # settings.py, urls.py, wsgi.py
├── manage.py
└── requirements.txt
```

---

## How It Works

### Lesson Progression
Lessons are locked by default. A lesson unlocks only after the user passes the previous lesson's quiz with at least 60%. Progress is tracked per user per lesson.

### Certificates
Automatically issued when a user completes all 12 lessons. Each certificate has a unique code (`CERT-XXXXXXXX`) generated with `secrets`. The code can be shared for verification.

### Python Playground
Code is executed in a subprocess with a 5-second timeout and 10,000-character limit. Dangerous imports (`os`, `sys`, `subprocess`, `shutil`) are blocked. Temporary files are cleaned up after execution.

### Dark / Light Mode
Toggle via the navbar sun/moon button. Preference is saved in `localStorage`. Applied before first render to prevent flash of wrong theme.

---

## Re-seed Lessons

```bash
# Clear and re-seed all lessons and quizzes
python manage.py seed_lessons --clear
```

---

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for full production deployment instructions.

Key production checklist:
- Set `DEBUG=False`
- Set a strong `SECRET_KEY`
- Configure `ALLOWED_HOSTS`
- Set up PostgreSQL and `DATABASE_URL`
- Configure email SMTP settings
- Run `python manage.py collectstatic --noinput`

---

## License

MIT
