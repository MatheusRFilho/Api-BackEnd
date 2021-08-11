from db import dbp
from typing import List


class ProductModel(dbp.Model):
	__tablename__ = "products"

	id = dbp.Column(dbp.Integer, primary_key=True)
	title = dbp.Column(dbp.String(50), nullable=False)
	price = dbp.Column(dbp.String(20), nullable=False)
	description = dbp.Column(dbp.String(200), nullable=False)


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
		dbp.session.add(self)
		dbp.session.commit()

	def delete_to_db(self) -> None:
		dbp.session.delete(self)
		dbp.session.commit()
