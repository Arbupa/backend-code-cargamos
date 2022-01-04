from readcsv import *
import unittest


class TestReadCSV(unittest.TestCase):

    # test check_if_sku_exists with different SKUs.
    def test_check_if_sku_exists(self):

        sku_list = [num for num in range(300)]

        for num in sku_list:
            self.assertEqual(check_if_sku_exists(num), False)

    # checks the return type of data with different SKUs.
    def test_type_in_check_if_sku_exists(self):

        sku_list = [num for num in range(300)]

        for num in sku_list:
            self.assertEqual(type(check_if_sku_exists(num)), bool)

    # checks the return type of data with different type of data
    def test_type_in_check_if_sku_exists2(self):

        types_to_test = [True, "", [], {},
                         False, None, "nil", "900.9292", "&",
                         "27/2", 234, 546, 23, 765, 876, 234, 4655.234242, 234.6546, 65.2, 565.234, 7676.2343,
                         ()]

        for num in types_to_test:
            self.assertEqual(type(check_if_sku_exists(num)), bool)

    # test passing different numbers as path
    def test_read_csv(self):

        list_of_paths = [str(num) for num in range(1, 300)]

        for path in list_of_paths:
            self.assertEqual(read_csv(path), "File's path not found.")


if __name__ == '__main__':
    unittest.main()
