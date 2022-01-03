from datetime import datetime, timedelta, date
from uuid import uuid1
import time


class Package:
    _instances_created = 0

    def __init__(self, size: float, expired_at: int, sku="") -> None:
        Package._instances_created += 1

        self.SKU = sku = uuid1() if sku == "" else sku
        # self.SKU = sku
        self.size = size
        self.__created_at = datetime.now()
        self.expired_at = self.__created_at + \
            timedelta(days=expired_at)

    def print_private(self):
        print(self.__created_at)

    def time_of_package_expiration(self):
        # checar cuando le paso un 0 o número negativo
        result = self.expired_at - datetime.today()
        result_in_seconds = result.total_seconds()
        print("resul en seconds", result.total_seconds())
        expired_at_in_seconds = self.expired_at.timestamp()
        print(self.expired_at.timestamp())
        # print(date_a)
        print()
        # if str(result) < str(self.expired_at) and result_in_seconds > 0:
        if result_in_seconds < expired_at_in_seconds and result_in_seconds > 0:
            print("Time remaining before package expires: \n", result)
            return result

        else:
            print("Expired package :(")
            return -1

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
# print(p.__created_at)

print(p2.SKU)
print(p3.SKU)
print(p4.SKU)
print(p5.SKU)
print(p6.SKU)
print(p7.SKU)
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

# time.sleep(60)
# p.elapsed_time()
