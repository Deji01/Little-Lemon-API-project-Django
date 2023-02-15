# Little-Lemon-API-project-Django
Little Lemon API Project. Django

### Project Setup [Start]
```bash
# create virtual environment
pipenv shell

# install django djangorestframework djoser djangorestframework-simplejwt
pipenv install django djangorestframework djoser djangorestframework-simplejwt

# start django project
django-admin startproject LittleLemon .

# create new app
python3 manage.py startapp LittleLemonAPI
```
## Steps Taken
1. Add `LittleLemonAPI` & `rest_framework` to `INSTALLED_APPS` in `settings.py`

2. Create models

3. Add Changes to Database

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
4. Run Development Web Server

```bash
python3 manage.py runserver
```
## NOTE 
Throttling was setup