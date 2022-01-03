from address import Address
from order import Order
from package import Package
from pprint import pprint
# import order
import csv
# import sys
# sys.path.append('C:\Users\juana\OneDrive\Escritorio\teststests\cargamos\part1')
# import Order
# import cargamos.part1.order
# sys.path.append('../')
# sys.path.insert(0, 'C:\Users\juana\OneDrive\Escritorio\teststests\cargamos\part1\order.py')
# from part1 import *
# from part1 import address

SKU = []
higher_difference = []
best_order_diff = []


class Bundle:
    def __init__(self) -> None:
        self.orders_loaded = []


def check_if_sku_exists(sku: str) -> bool:

    if sku in SKU:
        return True

    SKU.append(sku)
    return False


def higher_difference_order(order: Order) -> None:
    print("ID que llega es: ", order.SKU)
    difference = order.expired_at - order._Package__created_at

    if len(higher_difference) == 0 and str(order.time_of_package_expiration()) > "0" and order.delivered_at != True:
        higher_difference.append(difference)
        best_order_diff.append(order)
        return

    print("higher_difference is: ", len(higher_difference))
    package_time_life = str(order.time_of_package_expiration())
    print("package_time_life es: ", package_time_life)
    if difference > higher_difference[0] and package_time_life > "0" and order.delivered_at != True:
        higher_difference.pop()
        best_order_diff.pop()
        higher_difference.append(difference)
        best_order_diff.append(order)

    return
    # diff2 = order.expired_at - order.expired_at
    # print(order.expired_at)
    # print(order._Package__created_at)
    # print(diff2)
    # if difference > diff2:
    #     print("Es mayoooooor")


def read_csv(csv_path: str):

    with open(csv_path, newline='') as File:
        reader = csv.reader(File)

        print("El largo de la lista es: ", len(higher_difference))
        for row in reader:
            print(len(row))
            # print(type(row[0]))
            new_address = Address(
                row[0], row[1], row[2], row[3], row[4], row[5])

            try:
                new_order = Order(row[6], row[7], new_address, row[8])
                higher_difference_order(new_order)

            except:
                new_order = Order(float(row[6]), int(row[7]), new_address)
                higher_difference_order(new_order)
            # higher_difference_order(new_order)


if __name__ == "__main__":
    # print(check_if_sku_exists("1"))
    # print(check_if_sku_exists("3"))
    # print(check_if_sku_exists("3"))
    read_csv('data_file.csv')
    pprint(vars(best_order_diff[0]))
    print(higher_difference)

    # add = Address("1", 2, "3", "Saltiyork", "5", "6")
    # order = Order(10, 3, add)
    # higher_difference_order(order)
# import csv

# myData = [["first_name", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]

# myFile = open('data_file.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)

# print("Writing complete")
