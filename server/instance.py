from flask import Flask, Blueprint
from flask_restplus import Api
from ma import ma
from db import db
from flask_cors import CORS
from marshmallow import ValidationError


class Server():
	def __init__(self):
		self.app = Flask(__name__)
		cors = CORS(self.app)
		
		self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
		self.api = Api(self.bluePrint, doc='/doc', title='Sample Flask-RestPlus Application')
		self.app.register_blueprint(self.bluePrint)

		self.app.config['CORS_HEADERS'] = 'Content-Type'
		self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Nubia-2008@localhost:3306/visionBD'
		self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
		self.app.config['PROPAGATE_EXCEPTIONS'] = True
		self.app.config['SECRET_KEY'] = 'secret'

		self.user_ns = self.user_ns()
		self.product_ns = self.product_ns()
		self.purchase_ns = self.purchase_ns()


		super().__init__()

	def user_ns(self,):
		return self.api.namespace(name='Users', description='user related operations', path='/')

	def product_ns(self,):
		return self.api.namespace(name='Product', description='product related operations', path='/')
        
	def purchase_ns(self,):
		return self.api.namespace(name='Purchase', description='product related operations', path='/')

	def run(self, ):
		self.app.run(
			port=5000,
			debug=True,
			host='127.0.0.1',
		)
server = Server()
