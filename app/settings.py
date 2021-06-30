import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Development-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # # Postgres
    DB_DATABASE = os.environ.get('DB_DATABASE', '')
    DB_USERNAME = os.environ.get('DB_USERNAME', '')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    # dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
