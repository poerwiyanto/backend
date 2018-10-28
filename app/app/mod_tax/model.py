from app import app, db


class TaxObject(db.Model):
    __tablename__ = 'tax_objects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    codes = ['1', '2', '3']
    tax_code = db.Column(db.Enum(*codes), nullable=False)
    price = db.Column(db.BigInteger, nullable=False)
