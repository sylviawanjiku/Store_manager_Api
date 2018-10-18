class Sale():
    sales = []
    def __init__(self,sale_record_id,user_id,username,cart_id,sale_date,total):
        """Instansiating the variables for my methods"""
        self.sale_record_id =sale_record_id 
        self.user_id = user_id
        self.username =username
        self.cart_id =cart_id
        self.sale_date = sale_date
        self.total =total

    def post_sale(self):
        sale_data=dict(
            id = len(Sale.sales),
            sale_record_id = self.sale_record_id,
            user_id = self.user_id,
            username =self.username,
            cart_id =self.cart_id,
            sale_date = self.sale_date,
            total =self.total
        )
        self.sales.append(sale_data)
        return(sale_data)

    def get_sales(self):
        # fetch all sales
        return  Sale.sales
        
    def get_single_sale(self,sale_id):
        single_sale= [sale for sale in Sale.sales if int(sale['id']) == int(sale_id)]
        if single_sale:
            return single_sale
