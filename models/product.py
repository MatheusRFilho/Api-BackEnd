from db import db
from typing import List


class ProductModel(db.Model):
	__tablename__ = "products"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False)
	price = db.Column(db.String(20), nullable=False)
	description = db.Column(db.String(200), nullable=False)
	image = db.Column(db.String(400), nullable=True)


	def __init__(self, title, price, description):
		self.title = title
		self.price = price
		self.description = description

	def __repr__(self):
		return f'ProductModel(title={self.title}, price={self.price}, description={self.description})'

	def json(self):
		return {'title': self.title, 'price': self.price, 'description': self.description}

	@classmethod
	def find_by_name(cls, name) -> "ProductModel":
		return cls.query.filter_by(name=name).first()

	@classmethod
	def find_by_id(cls, _id) -> "ProductModel":
		return cls.query.filter_by(id=_id).first()

	@classmethod
	def find_all(cls) -> List["ProductModel"]:
		return cls.query.all()

	def save_to_db(self) -> None:
		db.session.add(self)
		db.session.commit()

	def delete_to_db(self) -> None:
		db.session.delete(self)
		db.session.commit()
