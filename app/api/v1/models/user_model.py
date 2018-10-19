"""
This module defines the user model and associated functions
"""
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class UserModel():
    users = []
    def __init__(self,username,first_name,last_name,email,role,password):
        """initialize the user model"""
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.password = generate_password_hash(password)

    def post_users(self):      
        user_data = dict(
            id =  len(UserModel.users),
            username = self.username,
            first_name= self.first_name,
            last_name = self.last_name,
            password =self.password,
            email = self.email,
            role = self.role               
        )
        self.users.append(user_data)
        return user_data

    def get_all_users(self):
        # fetch all users
        return  UserModel.users
