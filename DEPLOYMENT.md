# Deployment Configuration

## For Render.com:
- Runtime: Python 3.11
- Build Command: pip install -r requirements.txt
- Start Command: cd backend && python app.py
- Environment: Python

## For Heroku:
- Runtime: python-3.11.9 (specified in runtime.txt)
- Buildpacks: heroku/python
- Start Command: web: cd backend && gunicorn app:app --bind 0.0.0.0:$PORT --timeout 120 --workers 1

## For Railway:
- Runtime: Python 3.11
- Start Command: cd backend && python app.py
- Build Command: pip install -r requirements.txt

## Environment Variables (if needed):
- PORT: 5000 (automatically set by platforms)
- PYTHONPATH: /app (automatically set)
