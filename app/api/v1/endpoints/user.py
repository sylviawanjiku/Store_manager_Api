from flask import Flask, make_response, jsonify, request
from ..models.user_model import UserModel
from flask_restful import Resource, reqparse
import datetime
import re
from passlib.hash import sha256_crypt
import jwt
from functools import wraps

# request data validation
parser =reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('email')
parser.add_argument('role', type =int)
parser.add_argument('password')

"""Create a user account"""
class User(Resource):   
    def post(self):
            '''Posting items to Users'''        
            args = parser.parse_args()
            username = args['username']
            first_name = args['first_name']
            last_name = args['last_name']
            email = args['email']
            role = args['role']
            password = args['password']              
            store_user = UserModel(username,first_name,last_name,email,role,password)
            new_user = store_user.post_users()
            return make_response(jsonify({
                    'user': new_user
                }), 201)

   
t
