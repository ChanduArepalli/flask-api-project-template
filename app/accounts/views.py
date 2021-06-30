from flask import Blueprint, jsonify, request
from flask import current_app
from werkzeug.security import check_password_hash
from ..extensions import db
from .models import User

account = Blueprint('accounts', __name__, url_prefix='/accounts')


@account.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if email and password:
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password_hash, password):
                context = {
                    "message": "Logged Successfully",
                }
                return jsonify(**context), 200
        context = {
            "message": "Please provide valid email/ password",
        }
        return jsonify(**context), 400
    else:
        context = {
            "message": "Please provide email/ password",
        }
        return jsonify(**context), 400


@account.route('/signup', methods=['POST'])
def create_account():
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if email and password:
        check_users = User.query.filter_by(email=email).first()

        if check_users:
            context = {
                "message": "Email is already exist",
            }
            return jsonify(**context), 400
        else:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            context = {
                "message": "Account created successfully",
            }
            return jsonify(**context), 200
    else:
        context = {
            "message": "Please provide email/ password"
        }
        return jsonify(**context), 400
