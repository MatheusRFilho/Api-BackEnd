from flask import request
from flask_restplus import Resource, fields

from models.purchase import PurchaseModel

from schemas.purchase import PurchaseSchema

from server.instance import server

purchase_ns = server.purchase_ns

ITEM_NOT_FOUND = "Purchae not found."


purchase_schema = PurchaseSchema()

purchase_list_schema = PurchaseSchema(many=True)

# Model required by flask_restplus for expect
item = purchase_ns.model('Purchase', {
    'userId': fields.String('Purchase userId'),
    'id_list_products': fields.String('Purchase id_list_products'),
    'quantity': fields.String('Purchase id_list_products'),
})

class BuyProduct(Resource):
    @purchase_ns.expect(item)
    @purchase_ns.doc('Create an Item')
    def post(self):
        purchase_json = request.get_json()
        purchase_data = purchase_schema.load(purchase_json)

        purchase_data.save_to_db()

        return purchase_schema.dump(purchase_data), 201

