class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance >= self.total_amount():
            if self.owner.wallet.balance >= self.total_amount():
                self.owner.wallet.withdraw(self.total_amount())

        for item in self.items:
                owner  = item.owner
                owner.wallet.deposit(item.price)
        #La propiedad de todos los artículos de la cesta se transferirá al propietario de la misma.
        for item in self.items:
            item.set_owner(self.owner)
        #Vaciar el contenido del carro.
        self.items.clear
