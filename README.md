* Make virtual environment: mkvirtualenv -p python3 testproject_env
* Install packages for project :- pip install -r requirements.txt
* Create DB:
	1.sudo su - postgres
	2. psql
	3. CREATE DATABASE testproject_db;
	4. CREATE USER testproject_dba  WITH PASSWORD '1234';
	5. GRANT ALL PRIVILEGES ON DATABASE testproject_db TO testproject_dba;
	6. \q (to quit)
	7. exit
* Create local.env file with following data:
	export TEST_PROJECT_DEBUG='True'
	export TEST_PROJECT_SECRET_KEY='6!+6^-1y(i08v$26z26v7kd#q3iop9hikh$+91pz=$qv_prg8i'
	export TEST_PROJECT_ALLOWED_HOSTS='localhost'
	export TEST_PROJECT_DB_NAME='testproject_db'
	export TEST_PROJECT_DB_PASSWORD='9876'
	export TEST_PROJECT_DB_USER='testproject_dba'

*To Run:
	1. Activate testproject_env
	2. source local.env
	3. python manage.py runserver
*admin interface : /admin
*super user:
 python manage.py createsuperuser
 
 project
 --------
 * In the dashboard you can upload data (xlsx file is used, sample file is attached with email)
 * In Home page you can choose seasons and get corresponding results.
