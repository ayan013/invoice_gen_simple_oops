class Item:
    def __init__(self,name:str,price:int,quantity:float):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name} {self.quantity} x {self.total()}"
