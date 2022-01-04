from address import *
import unittest


class TestAddress(unittest.TestCase):

    # this function will raise an exception just for the int property
    # otherwise does not care
    def test_badtypes_in_constructor(self):

        types_to_test = [True, "", [], {}, False, None, "nil", "!",
                         "#", "$", "34 % 2", '&', "(", ")", "666.4", "* 23", "+", "-", "/"]

        for elem in types_to_test:

            with self.assertRaises(TypeError):
                address = Address(2, elem, True, False, None, {}, [])

    # this function will raise an exception just for the int property
    # otherwise does not care
    def test_badtypes_in_constructor2(self):

        types_to_test = [True, "", [], {}, False, None, "nil", "!",
                         "#", "$", "34 % 2", '&', "(", ")", "666.4", "* 23", "+", "-", "/"]

        for elem in types_to_test:

            with self.assertRaises(TypeError):
                address = Address(elem, elem, elem, elem, elem, elem, elem)

    # this will raise a TypeError because of missing arguments
    def test_no_arguments_in_constructor(self):
        with self.assertRaises(TypeError):
            address = Address()

    # func to test the properties we have specified
    def test_properties_given_in_address(self):

        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")

        assert address.address_line_1 == "first"
        assert address.locality == "locality"
        assert address.city == "my city"
        assert address.state == "my state"
        assert address.country == "cococountry"

    # sample test of get_full_address func
    def test_get_full_address(self):

        address = Address("first", 2, "locality", "my city",
                          "my state", "cococountry")

        self.assertEqual(address.get_full_address(),
                         "first,2,locality,my city,my state,cococountry,,")


if __name__ == '__main__':
    unittest.main()
