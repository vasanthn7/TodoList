# TodoList
Python/Django based To-do List

Instructions to install the application
* Once cloned, install all the packages specified in the requirements.txt
* Run migrations
* Run server using the command `python manange.py runserver`
* To enable the autodelete feature, run celery's worker and beat simultaniously using the command `celery -A todo worker -B` after activating the environment.


PS: The application also requires MySQL and mysql-devel
