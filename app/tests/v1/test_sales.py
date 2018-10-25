import sys
import unittest
import os
import json
from app.apps import create_app


class TestSales(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name="testing")
        """make app testable"""
        self.client = self.app.test_client
        self.products_data ={'product_id':'1267','product_name':'Sugar','brand':'Mumias','quantity':50,'price':500,'avail_stock':23,'min_stock':34,'uom':'sachets','category':'kitchen'}
        self.sales_data ={'attendant_name':'mary','product_name':'Sugar','price':'500','total_price':5000,'quantity' :10}

    
    def test_new_sale_creation(self):
        '''Test API can create a sale record (POST request)'''
        # Create a product
        new_product = self.client().post('/api/v1/products',data = self.products_data)
        self.assertEqual(new_product.status_code, 201)new_sale = self.client().post('/api/v1/sales',data = self.sales_data)  
        sale = json.loads(new_sale.data.decode('utf-8'))     
        self.assertEqual(new_sale.status_code, 201)
    
    def test_api_can_get_all_sales(self):
        '''Test API can get sales record (GET request)'''
        added_sale = self.client().post('/api/v1/sales',data = self.sales_data)
        self.assertEqual(added_sale.status_code, 201)
        res = self.client().get('/api/v1/sales')
        self.assertEqual(res.status_code, 200)
        
    def test_api_can_get_a_single_sale(self):
        '''Test API can get a single sale record (GET<id> request).'''
        added_sale = self.client().post('/api/v1/sales',data = self.sales_data)
        self.assertEqual(added_sale.status_code, 201)
        added_sale_id = json.loads(added_sale.data.decode())

        ''' Check for posted sale and fetch the sale verify if the sales data is correct'''
        posted_sale_data = self.client().get('/api/v1/sales/{}'.format(added_sale_id['sale'] ['id']))
        self.assertEqual(posted_sale_data.status_code, 200)
        
    """make the test executable"""
if __name__=='__main__':
    unittest.main()
