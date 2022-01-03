from package import Package
from address import Address
from pprint import pprint
from uuid import uuid1


class Order(Package):

    def __init__(self, size: float, expired_at: int, delivery_address: Address, sku="") -> None:
        super().__init__(size, expired_at, sku=sku)
        self.delivery_address = delivery_address
        self.delivered_at = None
        # self.SKU = sku = uuid1() if sku == "" else sku

    def order_delivered(self) -> str:

        package_expiration_time = self.time_of_package_expiration()

        if package_expiration_time != -1:
            self.delivered_at = True
            # print("Order's 'delivered_at' property modified successfully.")
            return "Order's 'delivered_at' property modified successfully."

        # print("Order not delivered. Package has expired.")
        return "Order not delivered. Package has expired."


# add = Address("1", 2, "3", "Saltiyork", "5", "6")
# order = Order(10, 3, add, "aaaa")
# pprint(vars(order))
# print(order.SKU)
# order.SKU = "a"
# print(order.SKU)
# print(order.expired_at)
# print(order._Package__created_at)
# a = ["1"]
# a[0] = "2"
# a.pop()
# # a.pop()
# print(a)
# a.append("Miau")
# print(a)

# print(order.delivery_address.city)
