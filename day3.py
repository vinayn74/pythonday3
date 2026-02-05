class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
    def display_product(self):
        print("product name", self.product_name)
        print("price", self.price)
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty
    def display_electronic_product(self):
        super().display_product()
        print("brand", self.brand)
        print("warranty" ,self.warranty)
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage
    def display_mobile_details(self):
        super().display_electronic_product()
        print("ram", self.ram)
        print("storage:", self.storage)
oppo = MobilePhone("oppof23","23k","oppo","1 year","8gb","256gb")
oppo.display_mobile_details()  
oppo.display_electronic_product()


