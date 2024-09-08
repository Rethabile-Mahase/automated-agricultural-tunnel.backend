import os
from flask import Flask, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return redirect('/api/v1')


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    if test_config is not None:
        app.config.from_object(os.environ['TEST_CONFIG'])
    else:
        app.config.from_object(os.environ['CONFIG'])
    try:
        db.init_app(app)
        migrate.init_app(app, db)
    except Exception as e:
        # Catch any exceptions that occur
        print(f"An error occurred: {e}")

    from . import resources

    app.register_blueprint(resources.api_bp)
    app.app_context().push()

    return app
