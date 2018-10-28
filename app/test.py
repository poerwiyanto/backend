from app import app
import json
import unittest

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_bill(self):
        response = self.app.get('/')
        expected_response = {
            "grand_total": 2280.5,
            "price_subtotal": 2150,
            "tax_subtotal": 130.5,
            "taxes": [
                {
                    "amount": 1030,
                    "name": "Lucky Stretch",
                    "price": 1000,
                    "refundable": "no",
                    "tax": 30,
                    "tax_code": "2",
                    "type": "Tobacco"
                },
                {
                    "amount": 1100,
                    "name": "Big Mac",
                    "price": 1000,
                    "refundable": "yes",
                    "tax": 100,
                    "tax_code": "1",
                    "type": "Food"
                },
                {
                    "amount": 150.5,
                    "name": "Movie",
                    "price": 150,
                    "refundable": "no",
                    "tax": 0.5,
                    "tax_code": "3",
                    "type": "Entertainment"
                }
            ]
        }
        self.assertEqual(json.loads(response.data.decode('utf-8')), expected_response)

    def test_add_tax_object_1(self):
        response = self.app.post('/', data=json.dumps(dict(
            name='Pepsi',
            tax_code='1',
            price=100)))
        response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(type(response['response']), type(1))

    def test_add_tax_object_2(self):
        response = self.app.post('/', data=json.dumps(dict(
            name='Pepsi')))
        response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response['response'], 'Error while creating tax object.')

if __name__ == '__main__':
    unittest.main()
