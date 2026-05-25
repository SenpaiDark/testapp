# Render Deployment Guide for mayor4code

This guide will help you deploy your Django application to Render.

## Prerequisites

- GitHub account with your code pushed to a repository
- Render account (sign up at [render.com](https://render.com))

## Deployment Steps

### 1. Prepare Your Repository

Ensure your code is committed and pushed to GitHub. Verify that:

- `.gitignore` excludes sensitive files (`.env`, `db.sqlite3`, etc.)
- All necessary files are included

### 2. Create Render Account & Connect

1. Sign up at [render.com](https://render.com)
2. Connect your GitHub account
3. Import your repository

### 3. Create Web Service

1. Choose "Web Service"
2. Select your repository
3. Configure the service:

**Basic Settings:**

- **Name**: `mayor4code` (or your preferred name)
- **Environment**: Python
- **Region**: Choose closest to your users
- **Branch**: `main` (or your deployment branch)

**Build Settings:**

- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Start Command**: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

**Plan:**

- Start with Free tier for testing
- Upgrade to paid for better performance

### 4. Environment Variables

Set these in Render dashboard under Environment Variables:

```bash
SECRET_KEY=your-random-secret-key-here-make-it-very-long-and-secure
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com,localhost,127.0.0.1
```

**Generate a secure SECRET_KEY:**

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 5. Database Setup

1. Create a PostgreSQL database on Render
2. Render automatically provides `DATABASE_URL` environment variable
3. Your app will automatically use PostgreSQL in production

### 6. Post-Deployment Setup

After deployment completes, run these commands in Render's Console:

```bash
python manage.py migrate
python manage.py seed_lessons
python manage.py createsuperuser
```

## Environment Configuration

### Production Variables (.env.production)

Copy these to your Render environment variables:

```bash
SECRET_KEY=your-secure-random-key
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com,localhost,127.0.0.1
```

### Optional Email Configuration

For production email, add these variables:

```bash
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
```

## Troubleshooting

### Common Issues

1. **Build fails**: Check that all dependencies are in requirements.txt
2. **Static files not loading**: Verify WhiteNoise configuration
3. **Database connection issues**: Ensure PostgreSQL is properly set up
4. **Logging errors**: The app now uses console-only logging for Render compatibility

### Logs

View logs in Render dashboard under your service's "Logs" tab.

## Maintenance

- Regularly update dependencies
- Monitor performance in Render dashboard
- Set up custom domain if needed
- Enable auto-deploy from main branch

## Support

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)

## Notes

- The app uses WhiteNoise for static files
- PostgreSQL is automatically configured via DATABASE_URL
- Security headers are enabled in production
- Console email is used by default (configure SMTP for production emails)
