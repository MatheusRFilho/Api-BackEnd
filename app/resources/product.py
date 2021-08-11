from flask import request
from flask_restplus import Resource, fields

from models.product import ProductModel
from models.purchase import PurchaseModel

from schemas.product import ProductSchema
from schemas.purchase import PurchaseSchema

from server.instance import server


import subprocess
import os

product_ns = server.product_ns
purchase_ns = server.purchase_ns

ITEM_NOT_FOUND = "Product not found."


product_schema = ProductSchema()
purchase_schema = ProductSchema()

product_list_schema = ProductSchema(many=True)
purchase_list_schema = PurchaseSchema(many=True)

# Model required by flask_restplus for expect
item = product_ns.model('Product', {
	'title': fields.String('Product title'),
	'price': fields.String('Product price'),
	'description': fields.String('Product description'),
})

class Product(Resource):
	def get(self, id):
		product_data = ProductModel.find_by_id(id)
		if product_data:
			return product_schema.dump(product_data)
		return {'message': ITEM_NOT_FOUND}, 404

class ProductList(Resource):
	@product_ns.doc('Get all the Items')
	def get(self):
		process = subprocess.Popen('scrapy runspider productslist/productslist/spiders/products.py', shell=True)
		process.wait()
		return product_list_schema.dump(ProductModel.find_all()), 200