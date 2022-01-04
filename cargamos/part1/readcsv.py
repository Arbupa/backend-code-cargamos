from address import Address
from order import Order
from package import Package
from pprint import pprint
import csv

# global variables just to avoid duplicates and store
# things with higher difference in Orders.
sku_list = []
higher_difference = []
best_order_diff = []


class Bundle:
    def __init__(self) -> None:
        self.orders_loaded = []


# function to check if sku is unique or not.
def check_if_sku_exists(sku: str) -> bool:

    if sku in sku_list:
        return True

    # print("sku added: ", sku)
    sku_list.append(sku)
    return False


# function to compare each order received and stores inside "best_order_diff"
# the order with higher difference between "created_at" and "expired_at".
def higher_difference_order(order: Order) -> None:
    print("Order ID processing is: ", order.SKU)
    difference = order.expired_at - order._Package__created_at

    if len(higher_difference) == 0 and str(order.time_of_package_expiration()) > "0" and order.delivered_at != True:
        higher_difference.append(difference)
        best_order_diff.append(order)
        return

    # print("higher_difference is: ", len(higher_difference))
    package_time_life = str(order.time_of_package_expiration())
    print("package_time_life es: ", package_time_life)

    if difference > higher_difference[0] and package_time_life > "0" and order.delivered_at != True:

        higher_difference.pop()
        best_order_diff.pop()
        higher_difference.append(difference)
        best_order_diff.append(order)

    return


# function to read CSV file and returns a Bundle class with all the orders loaded.
def read_csv(csv_path: str):

    bundle = Bundle()

    try:
        with open(csv_path, newline='') as File:
            reader = csv.reader(File)

            for row in reader:

                try:
                    new_address = Address(
                        row[0], int(row[1]), row[2], row[3], row[4], row[5])

                except:

                    print("Error trying to create Address instance.")
                    continue
                    # this is because I wanted to test different instances passing sku property
                    # and others without passing sku in CSV file.
                try:
                    new_order = Order(float(row[6]), int(
                        row[7]), new_address, row[8])
                    new_order.SKU = row[8]

                    if check_if_sku_exists(new_order.SKU) == False:

                        higher_difference_order(new_order)
                        bundle.orders_loaded.append(new_order)

                    else:
                        continue

                except:
                    new_order = Order(float(row[6]), int(row[7]), new_address)

                    if check_if_sku_exists(new_order.SKU) == False:

                        higher_difference_order(new_order)
                        bundle.orders_loaded.append(new_order)
    except:

        print("File's path not found.")

        return "File's path not found."

    return bundle


if __name__ == "__main__":

    bundle = read_csv('data_file.csv')
    print()
    pprint(vars(best_order_diff[0]))
    print()
    print("higher difference is: ", higher_difference[0])
    # print(bundle.orders_loaded)
    # add = Address("1", 2, "3", "Saltiyork", "5", "6")
    # order = Order(10, 3, add)
    # higher_difference_order(order)
    print("Number of orders ready inside bundle: ", len(bundle.orders_loaded))
