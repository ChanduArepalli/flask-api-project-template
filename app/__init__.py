from flask import Flask, Blueprint
from .extensions import db
from flask_migrate import Migrate
from .accounts.views import account
from .settings import Config


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(account)
    migrate = Migrate(app, db)
    return app
