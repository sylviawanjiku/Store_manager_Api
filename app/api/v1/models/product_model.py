from flask_restful import reqparse
# request data validation

class Product():
    products = []
    def __init__(self,product_name,brand,quantity,price):
        self.product_name = product_name
        self.brand = brand
        self.quantity =quantity
        self.price =price
        
    def post_product(self):
      
        product_data = dict(
            id =  len(Product.products),
            product_name= self.product_name,
            brand = self.brand,
            quantity =self.quantity,
            price = self.price
           )
        self.products.append(product_data)

        return {'products' : self.products, 'message' : 'Posted successfully'}

        
    def get_products(self):
        # fetch all products
        return {'products' : self.products, 'message' : 'Products retrieved successfully'}
        