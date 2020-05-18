# NOTEBOOK
Notebook is a flask app designed to keep track of notes and categorize notes for record purposes. This project is also the Capstone Project for Full-Stack Nanodegree at Udacity.

## Database structure
< TODO: quickDBD pic here>

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
< TODO: base URL here>
### Error Handling
Errors are returned as JSON objects with "success" set to False, "error" set to the error's number and a "message" describing the error

The API may return these error types when requests fail:
- 400: Bad Request
- 403: Forbidden
- 404: Resource Not Found
- 422: Request can not be processed
- 500: Internal Server Error

### Endpoints
< TODO: endpoints here>

## Getting started with local development

### Basic Requirements

In order to successfully set up the app, you need to have Python3, pip and PostgreSQL (12.1) already installed on your local machine

### Installing dependencies

Install dependencies by navigating to the project directory and running:

```bash
pip install -r requirements.txt
```

### Database Setup

<TODO: text here>

### Running the server

To run the server, execute these three lines from within the `/starter` directory:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Hosting instructions

<TODO: text here>

