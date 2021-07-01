from flask import Flask
from .extensions import db, jwt, migrate
from .accounts.views import account
from .settings import Config


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    # Routes
    app.register_blueprint(account)
    return app
