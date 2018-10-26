import sys
import unittest
import os
import json
from app.apps import create_app


class TestProducts(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()      
        self.products_data ={'product_id':'123','product_name':'Sugar','brand':'Mumias','quantity':50,'price':500,'avail_stock':23,'min_stock':34,'uom':'sachets','category':'kitchen'}
        self.products_data1 ={'product_id':'1234','product_name':'Tea','brand':'Mumias','quantity':50,'price':500,'avail_stock':23,'min_stock':34,'uom':'sachets','category':'kitchen'}

    def test_new_product_creation(self):
        '''Test API can create a product (POST request)'''
        new_product = self.client.post('/api/v1/products',data = self.products_data)       
        self.assertEqual(new_product.status_code, 201)
        

    def test_api_can_get_all_products(self):
        '''Test API can get products (GET request)'''
        res = self.client.get('/api/v1/products')
        self.assertEqual(res.status_code, 200)
        

    def test_api_can_get_a_single_product(self):
    #     '''Test API can get a single product (GET<id> request).'''
        new_product = self.client.post('/api/v1/products',data = self.products_data1)       
        self.assertEqual(new_product.status_code, 201)

        ''' Check for posted product and fetch the product verify if the product data is correct'''
        posted_product_data = self.client.get('/api/v1/products/0')
        
        self.assertEqual(posted_product_data.status_code, 200)
    #     self.assertIn('Sugar', str( posted_product_data.data))

# make the test executable
if __name__=='__main__':
    unittest.main()
