from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager


app = Flask(__name__)

db = SQLAlchemy()


# if timezone required
# import pytz
#
# # assuming now contains a timezone aware datetime
# tz = pytz.timezone('Asia/Kolkata')
# your_now = datetime.now.astimezone(tz)
