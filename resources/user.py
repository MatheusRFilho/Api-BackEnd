from flask import request
from flask_restplus import Resource, fields

from models.user import UserModel
from schemas.user import UserSchema

from server.instance import server

user_ns = server.user_ns

ITEM_NOT_FOUND = "User not found."


user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

# Model required by flask_restplus for expect
item = user_ns.model('User', {
    'name': fields.String('User name'),
    'email': fields.String('User email'),
    'passwd': fields.String('User passwd'),
    'status': fields.Integer(required=False),

})

class User(Resource):
	def get(self, id):
		user_data = UserModel.find_by_id(id)
		if user_data:
			return user_schema.dump(user_data)
		return {'message': ITEM_NOT_FOUND}, 404

class UserList(Resource):
	@user_ns.doc('Get all the Items')
	def get(self):
		return user_list_schema.dump(UserModel.find_all()), 200

	@user_ns.expect(item)
	@user_ns.doc('Create an Item')
	def post(self):
		user_json = request.get_json()
		user_data = user_schema.load(user_json)

		user_data.save_to_db()

		return user_schema.dump(user_data), 201

class LoginUser(Resource):
	def post(self):
		user_json = request.get_json()
		email = UserModel.find_by_email(user_json['email'])
		passwd = UserModel.find_by_passwd(user_json['passwd'])
		user_data = UserModel.login_user(user_json['email'], user_json['passwd'])
		if(user_data):
			if(user_data.status == 1):
				return "Bem Vindo " + user_json['email'], 200
			elif(user_data.status == 0):
				return "Bem Vindo", 200
		else:
			return "Usuário e senha inválidos"