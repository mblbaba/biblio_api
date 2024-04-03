import datetime
from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token



from src.models.user import User
from src.serializers.users import serialize_user
from utils import make_response_if_unknown_params_or_missing_params


def register_login_route(app, db):
    @app.route('/auth/login', methods = ['POST'])
    def login():
        data = request.get_json()
        params = ["username", "password"]
        err = make_response_if_unknown_params_or_missing_params(params, data)
        if err :
            return err
        user = User.query.filter_by(username = data['username']).first()
        if user and user.password == data['password']:
            # algorithm="HS256"
            token = create_access_token({"user_id": user.id}, expires_delta=datetime.timedelta(days=1))
            
            response = {
                "success" : 1,
                "message" : "User logged in successfully",
                "access_token": token
            }
            return make_response(response, 200)
        else:
            return make_response(jsonify({"success": -1, "message": "Invalid username or password"}), 401)
