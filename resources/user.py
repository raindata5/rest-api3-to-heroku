import sqlite3
from flask_restful import Resource
from flask_restful import reqparse
from models.user import UserModel




class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', help='The username is requied and must be a string', required=True, type=str)
    parser.add_argument('password', help='The username is requied and must be a string', required=True, type=str)


    def post(self):
        user_info = UserRegister.parser.parse_args()
        if UserModel.get_user_by_username(user_info['username']):
            return {'message': '{} already taken'.format(user_info['username'])}, 400
        else:
            new_user = UserModel(**user_info)
            new_user.save_to_database()
            return {"message": 'user created'}, 201
