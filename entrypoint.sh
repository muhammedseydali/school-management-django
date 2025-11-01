

#!/bin/sh
set -e

APP_PORT=${PORT:-8000}

# (WORKDIR is already /app)
# cd /app

/opt/venv/bin/gunicorn \
  --worker-temp-dir /dev/shm \
  school_management.wsgi:application \
  --bind "0.0.0.0:${APP_PORT}"