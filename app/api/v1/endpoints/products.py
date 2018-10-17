from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource ,reqparse
from ..models.product_model import Product

parser =reqparse.RequestParser()

parser =reqparse.RequestParser()
parser.add_argument('product_name')
parser.add_argument('brand',type =str)
parser.add_argument('quantity',type = int)
parser.add_argument('price', type =int)
class Products(Resource):
    products = []
    def post(self):
        # Posting items to products
        
        args = parser.parse_args()
        product_name = args['product_name']
        brand = args['brand']
        quantity = args['quantity']
        price = args['price']     
        
        my_product = Product(product_name,brand,quantity,price)
        new_product = my_product.post_product()
        return make_response(jsonify({
                'product': new_product
            }), 201)

    def get(self,product_id = None):
            # Get all products in the list
            if product_id is None:
                # If the list is empty
                if len(Products.products) == 0:
                    return make_response(jsonify({
                    'message': 'The product list is empty'
                    }), 200)
                # If the list is not empty
                
                return make_response(jsonify(
                    {
                        'status': 'Ok',
                        'Message': 'success',
                        'product': Products.products
                    }
                ), 200)
            