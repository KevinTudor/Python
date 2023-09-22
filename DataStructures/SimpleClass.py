# -*- coding: utf-8 -*-
"""
Problem 3.2

Kevin Tudor

class/subclass
"""

class Product:
    def __init__(self, name, price, mass, stock):
        self.na = name
        self.pr = price
        self.mass = mass
        self.stock = stock

    def set_price(self, price):
        self.pr = price

    def name(self):
        #print(self.na)
        return self.na

    def price(self):
        #print(self.pr)
        return self.pr

    def __str__(self):
        return "{}, ${}, {} kg, {} in stock".format(self.na, self.pr, self.mass, self.stock)


class DiscountedProduct:
    def __init__(self, d, p):
        self.d = d
        self.p = p

    def price(self):
        price = self.p.price()
        sub = float(price * self.d)
        self.d_price = price - sub
        
        return self.d_price

    def __str__(self):
        return "Discounted {}%: {}, ${}, {} kg, {} in stock".format(self.d * 100, self.p.na, self.price(), self.p.mass, self.p.stock)


def main():
    # create a product object for Lavalamps, priced at $100, and with 123 of them in stock:
    p = Product(name="Lavalamp", price=30, mass=0.8, stock=123)
    print(p) # prints "Lavalamp, $30, 0.8 kg, 123 in stock"
    
    #print(p.name())
    print(p.price())  #print returned value: 30.0
    
    # create a discounted product of p, with a 20% discount:
    disc_p = DiscountedProduct(0.2, p)
    print(int(disc_p.price()))  # prints "24" (24 == 30 - 20% * 30)
    print(disc_p)  # prints "discounted 20%: Lavalamp, $24, 0.8 kg, 123 in stock"
    
    
    p.set_price(20) # now, we change the product p:
    print(p.price()) # prints "20"
    
    # the price change also affects the discounted product object that embeds p:
    print(disc_p)  # prints "discounted 20%: Lavalamp, $16, 0.8 kg, 123 in stock"
    print(int(disc_p.price()))  # returns 16 (16 == 20 - 20% * 20)

print("-----------------------------------------------------")
 
if (__name__=="__main__"):
    main()
    
print("-----------------------------------------------------")

