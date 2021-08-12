from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from resources.user import User, UserList, LoginUser, user_ns
from resources.product import Product, ProductList, product_ns
from resources.purchese import BuyProduct


from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app

@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


api.add_resource(User, '/users/<int:id>')
api.add_resource(UserList, '/users')

#patch - add itens on database
api.add_resource(Product, '/add-product')
#delete - Delete itens on databse
api.add_resource(Product, '/product/<int:id>')

#put - uptade a product
api.add_resource(Product, '/product/<int:id>')

#get - Get all de products
api.add_resource(ProductList, '/product')


api.add_resource(BuyProduct, '/buy_products')

api.add_resource(LoginUser, '/login')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
