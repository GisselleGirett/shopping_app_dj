
from cart import Cart
from user import User

class Customer(User):

    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)  # Customerインスタンスは生成されると、自身をオーナーとするカートを持ちます。
