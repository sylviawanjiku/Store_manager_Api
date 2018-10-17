import sys
import unittest
import os
import json
from app.apps import create_app


class TestProducts(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.products_data ={'product_name':'Sugar','brand':'Mumias','quantity':50,'price':500}

    def test_new_product_creation(self):
        # Test API can create a product (POST request)
        new_product = self.client().post('/api/v1/products',data = self.products_data)
        product_data = json.loads(new_product.data.decode())
        self.assertEqual((product_data['message']), 'product success')
        self.assertIn(product_data.status_code, 201)  
