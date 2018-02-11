# TheRomanCatholicArchive.com
Online archive of Catholic books

## How to run locally

1. Install `python 3.x`
2. Install `django` by running `pip3 install django` in a terminal window as administrator
3. `cd` into the directory you cloned this project
3. Run `python3 manage.py createsuperuser`, remember the credentials you use
4. Run `python3 manage.py migrate`
5. Run `python3 manage.py runserver`
6. Open a web browser and navigate to http://127.0.0.1:8000/
7. Open a web browser and navigate to http://127.0.0.1:8000/admin. You should be able to log in with the credentials you used earlier and add, edit, and remove books. Navigate back to http://127.0.0.1:8000/ at any time to see the website as a non-admin.