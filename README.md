# ChessApp

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Simple application for chess players to list available moves and validate them. App was created with Flask, 
Flask-RESTful. Application was also dockerized and deployed via Heroku platform. In order to test app, PyTest was 
used. Also libraries like Black and Flake8 was used to check coding style.

## Technologies
* Python: 3.9.2
* Flask: 2.0.3
* Flask-RESTful: 0.3.9
* PyTest: 7.0.1
* Docker
* Heroku platform


## Setup
First of all, it is needed to install Python. To install it, visit this site:
https://www.python.org/downloads/


After installation of Python and activating virtual environment,
requirements must be install. Install from requirements.txt:
```
pip install -r requirements.txt 
```

Install from Pipfile (with pipenv):
```
pipenv install
```

Testing app:
```
pytest
```



### Standard run
Running application:
```
py main.py 
```

### Docker build and run (example)
To install Docker, visit: https://www.docker.com/       
Build:
```
docker build -t chess-app .
```

Run:
```
docker run -it -p 5000:5000 chess-app
```


## Usage
To use app, you need to enter a specific URL address. The pattern to list possible 
move is:
```
http://localhost:{PORT}/api/{version}/{figure}/{current-field}
```

To validate move:
```
http://localhost:{PORT}/api/{version}/{figure}/{current-field}/{dest-field}
```

If given fields and URL are valid, in term of listing possible moves, JSON is return with available moves, 
error with null value, current field and figure. On the other hand, validation method return whether move 
is valid, figure, error with null value or error message, current field and destination field.

Both methods does not recognize other figures on the board!

If there is not given field or there is not such URL, proper response appears.

The version field in the URL address defines in which direction the pawn can move. If it is v1 the pawn 
can move "down", if v2 the pawn can move "up".

You can also use application via Heroku platform on this site:  
http://chess-helper-app.herokuapp.com/

404 appears if you enter site. Build proper URL address to test app e.g.
```
https://chess-helper-app.herokuapp.com/api/v1/king/a2
https://chess-helper-app.herokuapp.com/api/v1/king/a2/a3
```