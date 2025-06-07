from models.client import Client
from models.item import Item
from models.invoice import Invoice
from models.client import Client
from models.invoice import Invoice

client=Client("Ayan",90345678,"ayan@email.com")

invoice=Invoice(client,0.18,100)

invoice.add_item(Item("Fridge",23000,2))
invoice.add_item(Item("Washing machine",15000,2))
invoice.add_item(Item("Cooler",40000,2))

invoice.generate_invoice()