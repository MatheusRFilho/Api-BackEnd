from ma import ma
from models.purchase import PurchaseModel


class PurchaseSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = PurchaseModel
		load_instance = True
