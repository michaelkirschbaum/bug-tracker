# Feature Requests

  Store client feature requests. Supports scheduling priorities and due dates.

## Dependencies

  Flask
  Flask-Migrate
  Flask-Script
  Gunicorn
  Python 2.7  
  SQLAlchemy  
  Werkzeug
  PostgreSQL

## Setup

  Building the application requires activating the Python virtual environment
  using the following command from the project root:

    '. venv/bin/activate'

  Ensure Postgres is running and the default 'Postgres' user and database exist.
  Setup the database with:

    'python setup.py'

  This creates the database 'feature_request_development' and
  'feature_request_test'. Next specify the location of the created database:

    'export DATABASE_URL="postgres://localhost/feature_request_development"'

  Generate and run database migrations with:

    'python manage.py db migrate'  
    'python manage.py db upgrade'

## Run

  To run the server in development mode flask needs to know the app location:

    'export FLASK_APP=app.py'
    'export FLASK_DEBUG=1'

  Then issue:

    'flask run'

  To run in production mode use:

    'python app.py'

  To use the app, direct your browser to http://localhost:5000.

## Testing

  To run the test suite, run the following script from the project root:

    'sh test.sh'
