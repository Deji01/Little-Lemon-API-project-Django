# Little-Lemon-API-project-Django
Little Lemon API Project. Django

### Project Setup
```bash
# create virtual environment
pipenv shell

# install django
pipenv install django

# start django project
django-admin startproject LittleLemon .

# create new app
python3 manage.py startapp LittleLemonAPI
```
## Steps Taken
- Add LittleLemonAPI to INSTALLED_APPS in settings.
- Create models
- Add Changes to Database
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```