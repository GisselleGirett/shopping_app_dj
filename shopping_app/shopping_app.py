
from customer import Customer
from item import Item
from seller import Seller
from wallet import __init__


seller = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("MEMORIA", 13880, seller)
    Item("TARJETA MADRE", 28980, seller)
    Item("UNIDAD DE FUENTE DE ALIMENTACIÓN", 8980, seller)
    Item("PC", 8727, seller)
    Item("3.5 HDD", 10980, seller)
    Item("2.5 SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU", 13400, seller)
    Item("TABLERO GRAFICO", 23800, seller)

print("🤖 POR FAVOR DIME TU NOMBRE")
customer = Customer(input())

print("🏧 POR FAVOR INGRESA EL MONTO A CARGAR EN TU BILLETERA")
customer.wallet.deposit(int(input()))

print("🛍️ EMPIEZA A COMPRAR")
end_shopping = False
while not end_shopping:
    print("📜 LISTA DE PRODUCTOS")
    seller.show_items()

    print("️️⛏ INGRESE EL NUMERO DEL PRODUCTO")
    number = int(input())

    print("⛏ INGRESE LA CANTIDAD DEL PRODUCTO")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 CONTENIDO DEL CARRITO")
    customer.cart.show_items()
    print(f"🤑 CANTIDAD TOTAL: {customer.cart.total_amount()}")

    print("😭 QUIERES TERMINAR DE COMPRAR？(yes/no)")
    end_shopping = input() == "yes"

print("💸 QUIERES CONFIRMAR TU COMPRA？(yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈RESULTADO┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️PROPIEDAD DE {customer.name}")
customer.show_items()
print(f"😱👛  {customer.wallet.balance} SALDO DE CARTERA DE: {customer.name}")

print(f"📦 ESTADO DE LAS RESERVAS DE {seller.name}")
seller.show_items()
print(f"😻👛 SALDO DE CARTERA DE: {seller.name} {seller.wallet.balance}")

print("🛒 CONTENIDO DE LA CESTA")
customer.cart.show_items()
print(f"🌚 IMPORTE TOTAL: {customer.cart.total_amount()}")

print("🎉 FIN")