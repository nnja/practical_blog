This is a sample Django blog app for Practical Python

To run this example:

Create a virtual environment
```bash
$ python3 -m venv env
$ source env/bin/activate
```

Install requirements
```bash
(env) $ python -m pip install -r requirements.txt
```

Migrate the Database
```bash
(env) $ python manage.py migrate
```

Create a super user
```bash
(env) $ python manage.py createsuperuser
```

Run the server
```bash
(env) $ python manage.py runserver
```

Your server should run at [http://localhost:8000/](http://localhost:8000/)