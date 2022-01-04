from datetime import datetime, timedelta, date
from uuid import uuid1
# import time


class Package:
    _instances_created = 0

    def __init__(self, size: float, expired_at: int, sku="") -> None:
        Package._instances_created += 1

        if type(size) not in [float, int]:
            raise TypeError("The attribute size must be a number")

        if type(expired_at) not in [float, int]:
            raise TypeError("The attribute expired_at must be a number")

        self.SKU = sku = uuid1() if sku == "" else sku
        self.size = float(size)
        self.__created_at = datetime.now()
        # here I added time in days just to test the difference worked.
        self.expired_at = self.__created_at + \
            timedelta(days=int(expired_at))

    def print_private(self):
        print(self.__created_at)

    # returns how much time is left before the package expires
    # or returns -1 if the package has already expired.
    def time_of_package_expiration(self):

        result = self.expired_at - datetime.today()
        result_in_seconds = result.total_seconds()
        # print("resul en seconds", result.total_seconds())
        expired_at_in_seconds = self.expired_at.timestamp()
        # print(self.expired_at.timestamp())

        if result_in_seconds < expired_at_in_seconds and result_in_seconds > 0:
            print("Time remaining before package expires: \n", result)
            return result

        else:
            print("Expired package :(")
            return -1

    # returns elapsed time between package's creation and the current datetime.
    def elapsed_time(self) -> timedelta:

        result = datetime.now() - self.__created_at
        print("Time elapsed since package creation: \n", result)
        return result


p = Package(1, 2)
p2 = Package(2, 12, "skuuuu")
p3 = Package(3, 12)
p4 = Package(4, 12)
p5 = Package(1, 12)
p6 = Package(2, 12)
p7 = Package(3, 12)
p8 = Package(4, 12)
p9 = Package(1, 12)
p10 = Package(2, 12)
p11 = Package(3, 12)
p12 = Package(4, 12)


# print(p2.SKU)
# print(p3.SKU)
# print(p4.SKU)
# print(p5.SKU)
# print(p6.SKU)
# print(p7.SKU)
# print(p8.SKU)
# print(p9.SKU)
# print(p10.SKU)
# print(p11.SKU)
# print(p12.SKU)
# p.print_private()
# print("Actual num is: ", Package._instances_created)
# print(p.expired_at)

# time.sleep(120)

# p.time_of_package_expiration()
# p2.time_of_package_expiration()
# p.elapsed_time()
# time.sleep(60)
# p.elapsed_time()
