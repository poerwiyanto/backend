from .model import TaxObject
from app import db
from flask import Blueprint, jsonify, request
import json

mod_tax = Blueprint('tax', __name__, url_prefix='/')


@mod_tax.route('/', methods=['GET'])
def get_bill():
    """User's bill."""
    bill = {
        'taxes': [],
        'price_subtotal': 0,
        'tax_subtotal': 0,
        'grand_total': 0
    }

    # For additional information.
    types = {
        '1': {
            'lambda': lambda x: 0.1 * x,
            'refundable': 'yes',
            'type': 'Food'
        },
        '2': {
            'lambda': lambda x: 0.02 * x + 10,
            'refundable': 'no',
            'type': 'Tobacco'
        },
        '3': {
            'lambda': lambda x: 0 if x < 100 and x > 0 else 0.01 * (x - 100),
            'refundable': 'no',
            'type': 'Entertainment'
        }
    }

    tax_objects = TaxObject.query.all()
    for item in tax_objects:
        tax = types[item.tax_code]['lambda'](item.price)
        bill['taxes'].append({
            'name': item.name,
            'tax_code': item.tax_code,
            'type': types[item.tax_code]['type'],
            'refundable': types[item.tax_code]['refundable'],
            'price': item.price,
            'tax': tax,
            'amount': item.price + tax
        })
        bill['price_subtotal'] += item.price
        bill['tax_subtotal'] += tax
        bill['grand_total'] += item.price + tax

    return jsonify(bill)

@mod_tax.route('/', methods=['POST'])
def set_bill():
    """Add tax object."""
    try:
        bill = json.loads(request.data.decode('utf-8'))

        tax_object = TaxObject(
            name=bill['name'],
            tax_code=bill['tax_code'],
            price=bill['price'])
        db.session.add(tax_object)
        db.session.commit()
        response = tax_object.id
    except:
        response = 'Error while creating tax object.'

    return jsonify({'response': response})
