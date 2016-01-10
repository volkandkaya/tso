##To set up the project

* Create a new folder called "tso"
* cd tso
* Use "virtualenv -p python3 env" for Python3 virtualenv
* use "source env/bin/activate" for env
* Clone the repo
* cd tso
* "pip install -r requirements.txt" to download Django
* Then run "python manage.py makemigrations"
* Then run "python manage.py migrate"
* Then run "python manage.py scraper"
* Then run "python manage.py runserver"
* Go onto localhost (http://127.0.0.1:8000/)
* After that you should be able to see a list of users who starred the project