from db import db
from typing import List


class PurchaseModel(db.Model):
	__tablename__ = "purchase"

	id = db.Column(db.Integer, primary_key=True)
	userId = db.Column(db.Integer, nullable=False)
	id_list_product = db.Column(db.String(200), nullable=False)
	quantity = db.Column(db.String(200), nullable=False)


	def __init__(self, userId, id_list_product, quantity):
		self.userId = userId
		self.id_list_product = id_list_product
		self.quantity = quantity

	def __repr__(self):
		return f'PurchaseModel(userId={self.userId}, id_list_product={self.id_list_product}, quantity={self.quantity} )'

	def json(self):
		return {'userId': self.userId, 'id_list_product': self.id_list_product, 'quantity': self.quantity}

	def save_to_db(self) -> None:
		db.session.add(self)
		db.session.commit()