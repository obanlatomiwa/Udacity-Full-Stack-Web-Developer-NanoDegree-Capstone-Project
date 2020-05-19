# NOTEBOOK
Notebook is a flask app designed to keep track of notes and categorize notes for record purposes. This project is also the Capstone Project for Full-Stack Nanodegree at Udacity.

## Database structure
PostgreSQL

## Role Based Access Control

##### Reader that is logged in through Auth0 is allowed to:
- view all notes
- view all categories
- search through notes

##### Author that is logged in through Auth0 is allowed to:
- view all notes
- search through notes
- add new notes
- edit notes
- delete notes
- view all categories
- add new categories
- edit categories
- delete categories

## API Reference

### Base URL
This app is currently hosted at https://wayne-notebook.herokuapp.com/ 

### FOR AUTHORIZATION
To login or set up an account, go to the following url: 

https://tomiwaobanla.auth0.com/authorize?audience=notebook&response_type=token&client_id=dadGT1E45otj6iXpY97feCfOG6GAU6Oc&redirect_uri=https://wayne-notebook.herokuapp.com

### Error Handling
Errors are returned as JSON objects with "success" set to False, "error" set to the error's number and a "message" describing the error

The API may return these error types when requests fail:
- 400: Bad Request
- 403: Forbidden
- 404: Resource Not Found
- 422: Request can not be processed
- 500: Internal Server Error

### Endpoints
GET  '/notes'
    This endpoint fetches all the notes in the database and displays them as json.

GET  '/categories'
    This endpoint fetches all the categories in the database and displays them as json.

POST '/notes'
    This endpoint will create a new note in the database based on the json that is in the body of the request.

POST '/categories'
    This endpoint will create a new category in the database based on the json that is in the body of the request.

PATCH  '/notes/<int:note_id>'
    This endpoint will modify the note that corresponds to the note ID that is passed into the url based on the json that is passed into the body of the request.

PATCH  '/categories/<int:category_id>'
    This endpoint will modify the category that corresponds to the category ID that is passed into the url based on the json that is passed into the body of the request.

DELETE  '/notes/int:<note_id>'
    This endpoint will delete the note that corresponds to the note ID that is passed into the url.

DELETE  '/categories/int:<category_id>'
    This endpoint will delete the category that corresponds to the category ID that is passed into the url.


## Getting started with local development

### Basic Requirements

In order to successfully set up the app, you need to have Python3, pip and PostgreSQL (12.1) already installed on your local machine

### Installing dependencies

Install dependencies by navigating to the project directory and running:

```bash
pip install -r requirements.txt
```

### Database Setup

If you want to run the app locally, you will have to comment out line 5 and uncomment line 9 in models.py, providing path to your local database.

### Running the server

To run the server, execute these three lines from within the `/starter` directory:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Running the tests
To run the tests you will also need to change TEST_DB_PATH (line 9 and 10) in test_app.py to match the path to your database. Note that running the tests will affect your database.
To run the tests, execute this line from the project directory:
```bash
python test_app.py
```

### Hosting instructions

The app is prepared to be deployed to Heroku.
You need to have a Heroku account and Heroku CLI installed on your machine.

Log in to your Heroku account
```bash
heroku login
```
Create Heroku app
```
heroku create app_name
```
The output will include a git url. Copy it and add git remote for Heroku to your local repository
```
git remote add heroku heroku_git_url
```
Add postgresql add-on 
```
heroku addons:create heroku-postgresql:hobby-dev --app app_name
```
Push the app to Heroku
```
git push heroku master
```


