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

        return product_data

        
    def get_products(self):
        # fetch all products
        return  Product.products
        
    def get_single_product(self,product_id):
        single_product= [product for product in Product.products if int(product['id']) == int(product_id)]
        if single_product:
            return single_product 
        # return{'message':'product not found'}
