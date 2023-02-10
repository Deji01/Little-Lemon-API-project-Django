# Little-Lemon-API-project-Django
Little Lemon API Project. Django

### Project Setup
```bash
# create virtual environment
pipenv shell

# install django
pipenv install django djangorestframework

# start django project
django-admin startproject LittleLemon .

# create new app
python3 manage.py startapp LittleLemonAPI
```
## Steps Taken
1. Add `LittleLemonAPI` & `rest_framework` to `INSTALLED_APPS` in `settings.py`.
2. Create models
3. Add Changes to Database
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```