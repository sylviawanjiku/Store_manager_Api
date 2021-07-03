from flask import Flask, make_response, jsonify, request
from ..models.product_model import Product
from ..models.sales_model import Sale
from flask_restful import Resource, reqparse
from datetime import datetime


# request data validation
parser =reqparse.RequestParser()

parser.add_argument('sale_record_id')
parser.add_argument('user_id')
parser.add_argument('username',type = str)
parser.add_argument('cart_id')
parser.add_argument('sale_date')
parser.add_argument('total', type =int)

class SalesRecord(Resource):
    def post(self):
        '''Posting items to sales'''        
        args = parser.parse_args()

        sale_record_id = args['sale_record_id']
        user_id = args['user_id']
        username = args['username']
        cart_id = args['cart_id']
        sale_date = args['sale_date']
        total =args['total']      
        
        my_new_sale = Sale(sale_record_id,user_id,username,cart_id,sale_date,total)
        new_sale = my_new_sale.post_sale()
        return make_response(jsonify({
                'sale': new_sale
            }), 201)

   
    def get(self,sale_id = None):
        # Get all sales in the list
        if sale_id is None:
            sale = Sale.get_sales(self)
            # If the list is empty
            if len(sale) == 0:
                return make_response(jsonify({
                'message': 'The sales record list is empty'
                }), 200)
            return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'success',
                    'sale': sale
                }
            ), 200) 
