# Running Locally

Tools Needed: mysql, python, gulp, mysql-connector, virtual env

1. Clone project
2. Make sure mysql server is running
3. create virtual enviornment inside api folder with the command
	"virtualenv env"
4. install dependencies using "pip install -r requirements.txt"
5. install mysql-connector-python
	git clone https://github.com/mysql/mysql-connector-python.git
	cd mysql-connector-python
	python ./setup.py build
	sudo python ./setup.py install
6. Run createWriteOperations.sql file in mysql to create table
7. UPDATE databaseConfig.py file with user and password for using mysql server
8. run "python getDataScript.py" to update database with today's data
9. run "python api.py" to start api server
10. cd into app folder and run "npm install" to install dependencies
11. Run command "gulp" to open web app