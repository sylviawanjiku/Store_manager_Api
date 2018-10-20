from flask import Flask, make_response, jsonify, request
from ..models.user_model import UserModel
from flask_restful import Resource, reqparse
from datetime import date, datetime, timedelta
import re
from passlib.hash import sha256_crypt
from functools import wraps
# import jwt
# from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity,get_raw_jwt)



parser =reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('first_name') 
parser.add_argument('last_name') 
parser.add_argument('email')
parser.add_argument('password') 



""" Create a function that generates authentication"""
# def token_required(f):
#     # view function
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None

#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']

#         if not token:
#             return jsonify({'message' : 'Token is missing!'}), 401

#         try: 
#             data = jwt.decode(token,'secret')            
#             current_user = UserModel.find_by_email(email)
#         except:
#             return jsonify({'message' : 'Token is invalid!'}), 401

#         return f(current_user, *args, **kwargs)

#     return decorated

class User(Resource):  

   
    def post(self):
            '''Posting items to Users'''        
            args = parser.parse_args()
            username = args.get('username')
            first_name= args.get('first_name')
            last_name = args.get('last_name')
            email = args.get('email')
            raw_password = args.get('password')  
  

# validate user input

            if not username:
                 return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'username cannot be null',
                    
                }
            ), 400)
               
            if not first_name:
                  return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'first_name cannot be null',
                    
                }
            ), 400)
               
             

            if not last_name:
                  return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'last_name cannot be null',
                    
                }
            ), 400)
               
               

            if not email:
                  return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'email cannot be null',
                    
                }
            ), 400)
            

           
            if not raw_password:
                  return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'password cannot be null',
                    
                }
            ), 400)
               
               


# generate hash
            password = UserModel.hash_password(raw_password)
            user = UserModel.create_user(username,first_name,last_name,password,email)
            all_users = UserModel.get_all_users()
            return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'User created successfully',
                    'product': all_users
                }
            ), 201)
            # return {"message":"",all_users}, 
           

class Login(Resource):
    
    parser =reqparse.RequestParser()
    parser.add_argument('email')
    parser.add_argument('password')
    def post(self):
            args = parser.parse_args()
            email = args.get('email')
            password = args.get('password')

            if not email:
                return {"message":"email cannot be null"}

            if not password:
                return {"message":"password cannot be null"}


# after validation check if user exists by email
            
            current_user = UserModel.find_by_email(email)
            if current_user == 0:
                  return {"message":"user with the email doesnt exist"}


# check if user password and stored hashed password match
            password_match = UserModel.verify_password(password,email)
            if password_match == True:
                # payload = {
                #     'exp': datetime.utcnow() + timedelta(minutes=7),
                #     'iat': datetime.utcnow(),
                #     'sub': email
                #     }                
                # token = jwt.encode(payload,"it's_a_secret")
                return {"message":"logged in successfully"}

            return {"message":"wrong credential"}
     
# # Test jwt
# class SecretResource(Resource):
#     @jwt_required
#     def get(self):        
#         return {
#             'answer': 42
#         }
