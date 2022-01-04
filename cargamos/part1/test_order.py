from datetime import datetime
from address import *
from package import Package
from address import Address
from order import Order
import unittest


class TestOrder(unittest.TestCase):

    # func to test the properties we have specified
    def test_properties_given_in_order(self):
        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")
        order = Order(99.9, 2, address)

        assert order.delivery_address.address_line_1 == "first"
        assert order.delivery_address.address_line_1 == "first"
        assert order.delivery_address.locality == "locality"
        assert order.delivery_address.city == "my city"
        assert order.delivery_address.state == "my state"
        assert order.delivery_address.country == "cococountry"
        assert order.delivered_at == None
        order.order_delivered()
        assert order.delivered_at == True
        assert type(order._instances_created) == int
        assert type(order._Package__created_at) == datetime
        assert type(order.expired_at) == datetime

    # func to test the properties we have specified
    def test_type_of_properties_in_order(self):

        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")
        order = Order(99.9, 2, address)

        assert type(order.delivery_address.address_line_1) == str
        assert type(order.delivery_address.address_line_1) == str
        assert type(order.delivery_address.locality) == str
        assert type(order.delivery_address.city) == str
        assert type(order.delivery_address.state) == str
        assert type(order.delivery_address.country) == str
        assert order.delivered_at is None
        order.order_delivered()
        assert type(order.delivered_at) == bool
        assert type(order._instances_created) == int
        assert type(order._Package__created_at) == datetime
        assert type(order.expired_at) == datetime

    # hi
    def test_instance_error__argument1_types(self):

        types_to_test = [True, "", [], {}, False, None, "nil", "()", (), "900.9292", "&",
                         "27/2"]

        for elem in types_to_test:

            with self.assertRaises(TypeError):
                address = Address("first", 2, "locality", "my city",
                                  "my state", "cococountry", "no address", "this is a note")
                my_package = Order(elem, 1, address)

    #
    def test_instance_error__argument2_types(self):

        types_to_test = [True, "", [], {}, False, None, "nil", "()", (), "900.9292", "&",
                         "27/2"]

        for elem in types_to_test:

            with self.assertRaises(TypeError):
                address = Address("first", 2, "locality", "my city",
                                  "my state", "cococountry", "no address", "this is a note")
                my_package = Order(290990.5, elem, address)

    # this will raise a TypeError exception because of missing arguments
    def test_no_arguments_in_constructor(self):

        with self.assertRaises(TypeError):
            order = Order()

    # testing order_delivered func with NOT expired packages.
    def test_order_delivered(self):

        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")

        different_days = [num for num in range(1, 500)]

        for day in different_days:

            order = Order(99.9, day, address)
            self.assertEqual(order.order_delivered(
            ), "Order's 'delivered_at' property modified successfully.")

    # testing order_delivered func with expired packages.
    def test_order_delivered_2(self):

        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")

        different_days = [num for num in range(-1000, -200)]

        for day in different_days:

            order = Order(99.9, day, address)
            self.assertEqual(order.order_delivered(
            ), "Order not delivered. Package has expired.")

    # testing if order_delivered func updates their value.
    def test_order_delivered_3(self):

        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")

        different_days = [num for num in range(1, 800)]

        for day in different_days:

            order = Order(99.9, day, address)
            assert order.delivered_at is None
            order.order_delivered()
            assert type(order.delivered_at) == bool

    # func to test if delivery_address property is an instance of Address.
    def test_is_instance_address(self):
        class Fake:
            def __init__(self) -> None:
                pass

        class Fake2:
            def __init__(self) -> None:
                pass

        class Fake3:
            def __init__(self) -> None:
                pass

        class Fake4:
            def __init__(self) -> None:
                pass

        class Fake5:
            def __init__(self) -> None:
                pass

        class Fake6:
            def __init__(self) -> None:
                pass

        class Fake7:
            def __init__(self) -> None:
                pass

        f = Fake()
        f2 = Fake2()
        f3 = Fake3()
        f4 = Fake4()
        f5 = Fake5()
        f6 = Fake6()
        f7 = Fake7()

        fake_instances = [f, f2, f3, f4, f5, f6, f7, ]

        for instance in fake_instances:

            with self.assertRaises(TypeError):
                order = Order(99.9, 3, instance)

    # func to test if delivery_address property is an instance of Address.
    def test_is_instance_address2(self):

        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")

        numbers_list = [num for num in range(1, 250)]

        for num in numbers_list:

            order = Order(num, num, address)
            assert isinstance(order.delivery_address, Address)


if __name__ == '__main__':
    unittest.main()
