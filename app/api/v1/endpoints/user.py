from flask import Flask, make_response, jsonify, request
from ..models.user_model import UserModel
from flask_restful import Resource, reqparse
import datetime
import re
from passlib.hash import sha256_crypt
from functools import wraps



parser =reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('first_name') 
parser.add_argument('last_name') 
parser.add_argument('email')
parser.add_argument('password') 

""" Create a function that generates authentication"""
# def required_token(f):
#     @wraps(f)
#     def decorator(*args,**kwargs):
#         token = None
#         if 'x-access-token' in request.headers:
#             token=request.headers['x-access-token']

#         if not token:
#             return make_response(jsonify({"message":"Token required to continue"}))
#         try:
#             data=jwt.decode(token,"SECRET_KEY")            
#             current_user=[user for user in user if int(user['user_id'])==int('user_id')]

#         except:
#             return make_response(jsonify({"message":"Invalid token"}),401)
        
#         return f(current_user,*args, **kwargs)
#     return decorator

class User(Resource):  

   
    def post(self):
            '''Posting items to Users'''        
            # args = parser.parse_args()
            # username = args.get('email')
            # first_name= args.get('first_name')
            # last_name = args.get('last_name')
            # email = args.get('email')
            # password = args.get('password') 
            # role = args.get('role')          
            # store_user = UserModel(username,first_name,last_name,role,email,password)
            # new_user = store_user.post_users()
            # return make_response(jsonify({
            #         'user': new_user
            #     }), 201)

            # start here
            args = parser.parse_args()
            username = args.get('username')
            first_name= args.get('first_name')
            last_name = args.get('last_name')
            email = args.get('email')
            raw_password = args.get('password')  
  

# validate user input

            if not username:
                return {"message":"username cannot be null"}

            if not first_name:
                return {"message":"first_name cannot be null"}

            if not last_name:
                return {"message":"last_name cannot be null"}

            if not email:
                return {"message":"email cannot be null"}

           
            if not raw_password:
                return {"message":"password cannot be null"}

# generate hash
            password = UserModel.hash_password(raw_password)

            user = UserModel.create_user(username,first_name,last_name,password,email)


            all_users = UserModel.get_all_users()
            return {"data": all_users}
            # new_user = store_user.post_users()
            # return make_response(jsonify({
            #         'user': new_user
            #     }), 201)


            # endhere

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
                return {"message":" user logged in succcessfuly "}
            return {"message":"wrong credential"}

    


        #  Store_user = UserModel()
        # c_user=store_user.get_all_users()

        # return {"users": c_user}
        # current_user=[user for user in c_user if user['email']==email)]
        # if len(current_user > 0):
        #     password =current_user[0]['password']
        #     if sha256_crypt.verify(get_password, password):
        #         expiry_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
        #         token = jwt.encode({'user_id': current_user[0]['user_id'],'expiry':expiry_time},"secret")
        #         result = {"message":"Logged in successfully","token":token.decode('utf-8')}
        #     else:  
        #        return make_response(jsonify({"message":"Invalid Login"}))
        # else:  
        #        return make_response(jsonify({"message":"Invalid email address"}))

        # return result,200

class SecretResource(Resource):

    def get(self):
        
        return {
            'answer': 42
        }
