"""
This module defines the user model and associated functions
"""
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import pbkdf2_sha256 as sha256
import datetime


users = []

class UserModel():
   
    # def __init__(self,username,first_name,last_name,role,email,password):
    #     """initialize the user model"""
    #     self.username = username
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.role = role
    #     self.password = generate_password_hash(password)

    # def post_users(self):      
    #     user_data = dict(
    #         id =  len(UserModel.users),
    #         username = self.username,
    #         first_name= self.first_name,
    #         last_name = self.last_name,
    #         password =self.password,
    #         email = self.email,
    #         role = self.role               
    #     )
    #     self.users.append(user_data)
    #     return user_data

        # def get_all_users(self):
        # # fetch all users
        # return  users

    # start here
    @staticmethod
    def create_user(username,first_name,last_name,password,email):      
        user_data = dict(
            id =  len(users),
            username = username,
            first_name= first_name,
            last_name = last_name,
            password = password,
            email = email
                       
        )
        users.append(user_data)
        return users


    @staticmethod
    def get_all_users():
        # fetch all users
        return  users

# checks if user  with the email exists
    @staticmethod
    def find_by_email(email):
        # fetch all users
        for x in users :
            listOfKeys =[key for (key,value) in x.items() if value == email]
            if listOfKeys :
                return 1

        return 0

# hash user password
    @staticmethod
    def hash_password(raw_password):
         
        return  sha256.hash(raw_password)


# verify if password provided by user matches the hashed password stored in users
    @staticmethod
    def verify_password(password,email):
        for x in users:
            listOfKeys =[key for (key,value) in x.items() if value == email]
            if listOfKeys :
                result = list(filter(lambda person:person['email'] == email,users))
                return sha256.verify(password, result[0]['password'])
        

    # end here
    
