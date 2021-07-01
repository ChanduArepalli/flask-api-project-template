import os
import datetime


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Development-Secret-Key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TIMEZONE = os.environ.get('TIMEZONE', 'Asia/Kolkata')  # default Indian timezone
    DATETIME_FORMAT = os.environ.get('DATETIME_FORMAT', '%d-%m-%Y %H:%M:%S')  # default format DD-MM-YYYY HH:MM:SS

    # # Postgres
    DB_DATABASE = os.environ.get('DB_DATABASE', '')
    DB_USERNAME = os.environ.get('DB_USERNAME', '')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    # dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'

    # # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'Development-JWT-Key')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=7)


