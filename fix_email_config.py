# Script to fix email configuration in settings.py
import re

# Read the current settings.py
with open('config/settings.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix email configuration lines
content = re.sub(r'EMAIL_HOST = config\("EMAIL_HOST"\)', 'EMAIL_HOST = config("EMAIL_HOST", default="")', content)
content = re.sub(r'EMAIL_HOST_USER = config\("EMAIL_HOST_USER"\)', 'EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")', content)
content = re.sub(r'EMAIL_HOST_PASSWORD = config\("EMAIL_HOST_PASSWORD"\)', 'EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")', content)
content = re.sub(r'DEFAULT_FROM_EMAIL = config\("DEFAULT_FROM_EMAIL"\)', 'DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="webmaster@localhost")', content)

# Write the fixed content back
with open('config/settings.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Email configuration fixed successfully!")