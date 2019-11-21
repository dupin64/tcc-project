# BACKEND

## Stack
Component      | Spec 
---            | ---      
Database       | SqlLite
O.R.M          | Django

## Virtual environment setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run migrations
```bash
python manage.py migrate
```

## Start development server
```bash
python manage.py runserver
```