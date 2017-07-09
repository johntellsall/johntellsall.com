https://docs.djangoproject.com/en/1.11/intro/tutorial01/

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

# XX more here


clear ; curl -i localhost:8000/cats/

# edit cats/models.py
# add 'cats' to hello/settings.py
python manage.py makemigrations cats

# output what would be created:
$ python manage.py sqlmigrate cats 0001
BEGIN;
--
-- Create model Cat
--
CREATE TABLE "cats_cat" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "image_url" varchar(200) NOT NULL);
COMMIT;


# actually create the important Cat table
python manage.py migrate

pip install django-extensions
# add 'django_extensions' to hello/settings.py INTALLED_APPS
python manage.py shell_plus


>>> Cat.objects.count()
0
>>> Cat.objects.create(name='Lil Bub')
<Cat: Cat object>
>>> Cat.objects.count()
1




>>> u.username='johnm'
>>> u.set_
u.set_password(           u.set_unusable_password(  
>>> u.set_
u.set_password(           u.set_unusable_password(  
>>> u.set_password('beer')
>>> u.save


# Login-Registration

https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
