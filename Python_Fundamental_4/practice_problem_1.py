class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Product Name: {self.name} | Price: Rs. {self.price}")
    
    @classmethod
    def get_count(cls):
        print("Total Products:", cls.count)

    @staticmethod
    def calc_discount(price, discount):
        print(f"Discounted Price:, {price-(price*discount/100)}")

p1 = Product("Laptop", 50000)
p2 = Product("Smartphone", 20000)

p1.get_info()
p1.calc_discount(50000, 10)
Product.get_count()