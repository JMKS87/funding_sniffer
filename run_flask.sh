export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=0
source venv/bin/activate
python -m flask run --host=0.0.0.0
