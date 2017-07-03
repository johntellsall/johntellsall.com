python3 -m venv env
. env/bin/activate
pip install --upgrade pip

echo Django >> requirements.txt
pip install -r requirements.txt
django-admin startproject hello

cd hello/
python manage.py runserver

curl -i localhost:8000

python manage.py startapp cats
