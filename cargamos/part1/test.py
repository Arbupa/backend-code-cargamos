from datetime import datetime
from datetime import date, datetime, timedelta, time
# import datetime
# a = datetime.now()
# if a > 0:
#     print("alalklaskd")

# a = datetime.now()
# print(a)
# b = datetime.today()
# print(b)
# c = a +

# timeobj = time(12, 45)
# print()
# print(datetime.combine(date.min, timeobj) - datetime.min)
# datetime.timedelta(0, 45900)

# a = datetime.now()
# # print(type(a))
# # print(a)
# b = a + timedelta(days=0)
# # print(type(a))
# print(a)
# print(b)
# c = "2023-01-01 14:05:59.045730"
# d = "2032-02-01 14:05:59.045731"
# print(c < d)


class A:
    def __init__(self) -> None:
        self.a = "a"


class B:
    def __init__(self, a_class: A) -> None:
        self.b = "b"
        self.instan = a_class


# a = A()
# b_instance = B(a)
# print(b_instance.b)
# print(b_instance.instan.a)


# then = datetime(2012, 3, 5, 23, 8, 15)        # Random date in the past
now = datetime.now()
now2 = datetime.now()
tomo = now + timedelta(seconds=40)
print(now)
print(tomo)
print("\n")
print(now.timestamp())
print(tomo.timestamp())
if tomo > now2:
    print("baia baia")
# duration = now - then                         # For build-in functions
# duration_in_s = duration.total_seconds()
# print(duration_in_s)
# minutes = divmod(duration_in_s, 60)[0]
# print(minutes)
# num = 0.000001
# if num > 0:
#     print("wasaaaaaaaaaaa")

# print("Order's 'delivered_at' property modified successfully.")
# full_address = f"""
#        Address 1: 123
#        Postal code: 123
#        Locality: 123
#        City: 123
#        State: 123
#        Country: 123
#        Address 2: 123
#        Notes: 123
#         """
full_address = f"{1},{2},{4}"
print(full_address)
a = None
a = True
print(a)


def a_b():
    print("func work")
    return

    print("no llega")


a_b()
