# Script to fix logging configuration in settings.py
import re

# Read the current settings.py
with open('config/settings.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix logging configuration - remove file handler and use only console
logging_config = '''# Logging - production-safe configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
           极"style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}'''

# Replace the entire logging section
content = re.sub(r'# Logging\nLOGGING = \{.*?\n\}', logging_config, content, flags=re.DOTALL)

# Write the fixed content back
with open('config/settings.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Logging configuration fixed successfully!")