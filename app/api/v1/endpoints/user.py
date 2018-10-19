from flask import Flask, make_response, jsonify, request
from ..models.user_model import UserModel
from flask_restful import Resource, reqparse

# request data validation
parser =reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('email')
parser.add_argument('role', type =int)
parser.add_argument('password')

class Users(Resource):   
    def post_user(self):
            '''Posting items to Users'''        
            args = parser.parse_args()
            username = args['username']
            first_name = args['first_name']
            last_name = args['last_name']
            email = args['email']
            role = args['role']
            password = ['password']           
            
            store_user = UserModel(username,first_name,last_name,email,role,password)
            new_user = store_user.post_users()
            return make_response(jsonify({
                    'puser': new_user
                }), 201)

   
class Login(Resource):
    def post(self):
        data = request.get_json(force=True)
        email=data['email']
        get_password=data['password']
        cur_user=[c_user for c_user in current_user if c_user['email']==email]

        if  len(cur_user) > 0:		
            password =cur_user[0]['password']
            if sha256_crypt.verify(get_password, password):
                exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
                token = jwt.encode({'user_id': cur_user[0]['user_id'],'exp': exp_time},"secret")
                result={"message":"Login succesful","token":token.decode('utf-8')}
                
            else:
                return make_response(jsonify({"message":"Invalid Password"}))
        else:
            return make_response(jsonify({"message":"Invalid Email"}))

        return result,200
