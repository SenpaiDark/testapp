# mayor4code

A Django MVP web app for **Computer-Aided Python Tutoring** — structured lessons, quizzes, locked progression, and instant scoring.

## Features

- Register / Login / Logout
- Show/Hide password eye icon on all auth forms
- Dashboard with overall progress bar
- 5 complete Python lessons (pre-loaded via seed command)
- Locked progression — each lesson unlocks only after passing the previous quiz
- Lesson page with prev/next navigation
- Multiple-choice quiz with automatic scoring
- Dark / Light mode toggle
- Favicon (M initial)
- Clean responsive UI

## Lessons Included

1. Introduction to Python
2. Variables and Data Types
3. Conditional Statements
4. Loops
5. Functions

## Setup

```bash
'python -m venv venv'
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_lessons        # loads all 5 lessons + quizzes
python manage.py createsuperuser
python manage.py runserver
```

## Re-seed (reset lessons)

```bash
python manage.py seed_lessons --clear
```

## Admin Panel

Go to <http://127.0.0.1:8000/admin/> to manage lessons, quizzes, and user progress.

## Notes

- A lesson unlocks only after the user passes the previous lesson's quiz.
- Passing requires scoring at or above the quiz pass mark (default: 60%).
- Lesson content is stored as HTML — edit it in the admin panel safely.
- To add more lessons: use the admin panel or extend `seed_lessons.py`.
