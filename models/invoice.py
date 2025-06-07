class Invoice:
    def __init__(self, client, tax_rate: float,discount:int):
        self.client=client
        self.tax_rate=tax_rate
        self.discount=discount
        self.items=[]

    def add_item(self, item):
        return self.items.append(item)

    def subtotal(self):
        total=sum(item.total() for item in self.items)
        return total

    def tax(self):
        return self.subtotal() * self.tax_rate

    def total(self):
        return self.subtotal() + self.tax() - self.discount

    def generate_invoice(self):
        print(f"-------Invoice Generated-----\n"
              f"{self.client}\n")
        for item in self.items:
            print(f"- {item}")
        print(f"Subtotal - {self.subtotal()}")
        print(f"Tax(18%) - {self.tax():.2f}")
        print(f"Discount - {self.discount}")
        print(f"Total Payable - {self.total()}")
        return None


