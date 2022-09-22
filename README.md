# This is the squareMakers test with fastapi

## About the project

This is a squareMakers test using fastapi for create an api

### Structure

* db 📂 // all necessary for db
  * models 📂 // has files make queries
    * `joke.py` // quieres for "joke" collection, post, get...
  * `conexion.py` // conexion for db, and function for create it
* routes 📂 // all routes
  * `joke.py` // all enpoints about jokes
  * `math.py` // all endpoints about math
* `main.py` // has the index route, and add all routes to the app
* `.gitignore` // all info don't upload to git
* `pyproject.toml` // poetry file has dependencies
* `README.md` // documentation (this file)

## How to run this project
### Python requirements (step 1)

* Install **["poetry"](https://python-poetry.org/docs/)** 
* Clone this repository
* Enter folder (cloned)
* Execute in terminal the comand **"poetry shell"** for create the develoment enviorement
* Execute in terminal the comand **"poetry install"** for install dependencies

### For run the project (step 2)

* Execute in terminal the comand **"uvicorn main:app"**
* Go to **[localhost:8000](http://localhost:8000/)**, there is you can look next dictionary: {"message": "Hi from my api"}
* Now your project is running

##### Aditonals steps for using the `post, put, and delete` endpoints

  * Uncomment lines 4, 14, and 15 in `main.py`
  * Make a request to **[localhost:8000](http://localhost:8000/)**
### Check documentation (step 3)

* Go to **[localhost:8000/docs](http://localhost:8000/docs)**
* Check all endpoints there are
