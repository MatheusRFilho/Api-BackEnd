from db import db
from typing import List


class UserModel(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False, unique=True)
	email = db.Column(db.String(100), nullable=False)
	passwd = db.Column(db.String(200), nullable=False)
	status = db.Column(db.Integer, nullable=True)


	def __init__(self, name, email, passwd, status):
		self.name = name
		self.email = email
		self.passwd = passwd
		self.status = status

	def __repr__(self):
		return f'UserModel(name={self.name}, email={self.email}, passwd={self.passwd}, status={self.status})'

	def json(self):
		return {'name': self.name, 'email': self.email, 'passwd': self.email, 'status': self.status}

	@classmethod
	def find_by_email(cls, email) -> "UserModel":
		return cls.query.filter_by(email=email).first()

	@classmethod
	def find_by_id(cls, _id) -> "UserModel":
		return cls.query.filter_by(id=_id).first()

	@classmethod
	def find_by_passwd(cls, passwd) -> "UserModel":
		return cls.query.filter_by(passwd=passwd).first()

	@classmethod
	def find_all(cls) -> List["UserModel"]:
		return cls.query.all()

	def save_to_db(self) -> None:
		db.session.add(self)
		db.session.commit()

    
	@classmethod
	def login_user(cls, email, passwd) -> "UserModel":
		return cls.query.filter_by(passwd=passwd).first()
