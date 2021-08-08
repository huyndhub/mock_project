# Mock Project

## Pre-require
1. Database: Postgresql

## Local setup
1. Create virtualenv in folder `mock_project/tmp/venv` and activate
2. Install requirements inside a Python3.x virtual environment: `pip install -r requirements.txt`
3. Setup environment variables files: 
   Copy `mock_project/mock_project/conf/.env.example` 
   To `mock_project/mock_project/conf/.env` 
   and fill the fields.
4. Run `python manage.py migrate`
5. Run test server: `python manage.py runserver`


## Create app
1. Create a new folder `mock_project/apps/app_name`
2. Run `python manage.py startapp app_name mock_project/apps/app_name`
3. Change field `name` = `mock_project.apps.app_name` in file `mock_project/apps/app_name/apps.py`
4. Append `mock_project.apps.app_name` to `INSTALLED_APPS` in file `mock_project/conf/base.py` 


