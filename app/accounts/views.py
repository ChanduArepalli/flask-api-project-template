from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, current_user, get_jwt_identity
import re
from ..extensions import db, jwt
from ..common import dt_format
from .models import User
account = Blueprint('accounts', __name__, url_prefix='/accounts')


def check_email_or_not(email: str):
    EMAIL_REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'
    result = re.search(EMAIL_REGEX, email)
    return True if result else False


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data.get("user_id", None)
    # print(jwt_data)
    # print(f'_jwt_header {_jwt_header}')
    if identity:
        return User.query.filter_by(id=identity).one_or_none()
    return None


@account.route('/signup', methods=['POST'])
def create_account():
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if email and password:
        is_email = check_email_or_not(email)
        if not is_email or len(password) < 8:
            context = {
                "message": "Please provide valid email/ password",
            }
            return jsonify(**context), 400

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
            return jsonify(**context), 201
    else:
        context = {
            "message": "Please provide email/ password"
        }
        return jsonify(**context), 400


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
                    "access_token": create_access_token(identity=user, additional_claims={'user_id': user.id}, fresh=True),
                    "refresh_token": create_refresh_token(identity=user, additional_claims={'user_id': user.id})
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


@account.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    # print(current_user)
    context = {
        "user_id": current_user.id,
        "email": current_user.email,
        "joined": dt_format(current_user.joined),
        "last_updated": dt_format(current_user.last_updated),
    }
    return jsonify(**context), 200


@account.route("/refresh", methods=["GET"])
@jwt_required(refresh=True)
def refresh():
    identity = current_user
    access_token = create_access_token(identity=identity, additional_claims={'user_id': identity.id}, fresh=True)
    context = {
        "access_token": access_token,
    }
    return jsonify(**context), 200
