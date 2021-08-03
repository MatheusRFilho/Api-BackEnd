from db import db
from typing import List


class UserModel(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False, unique=True)
	email = db.Column(db.String(100), nullable=False)
	passwd = db.Column(db.String(200), nullable=False)


	def __init__(self, name, email, passwd):
		self.name = name
		self.email = email
		self.passwd = passwd

	def __repr__(self):
		return f'UserModel(name={self.name}, email={self.email}, passwd={self.passwd})'

	def json(self):
		return {'name': self.name, 'email': self.email, 'passwd': self.email}

	@classmethod
	def find_by_name(cls, name) -> "UserModel":
		return cls.query.filter_by(name=name).first()

	@classmethod
	def find_by_id(cls, _id) -> "UserModel":
		return cls.query.filter_by(id=_id).first()

	@classmethod
	def find_all(cls) -> List["UserModel"]:
		return cls.query.all()

	def save_to_db(self) -> None:
		db.session.add(self)
		db.session.commit()

    
	@classmethod
	def login_user(cls, email, passwd) -> "UserModel":
		if(cls.query.filter_by(email=email).first()):
			return cls.query.filter_by(passwd=passwd).first()
