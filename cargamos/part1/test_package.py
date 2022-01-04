from package import *
import time
import unittest


class TestPackage(unittest.TestCase):

    # testing with expired time = current time
    def test_time_of_package_expiration_now(self):

        my_package = Package(19.5, 0)
        my_package2 = Package(20, 0)
        my_package3 = Package(119.5, 0)
        my_package4 = Package(199.5, 0, "1")
        my_package5 = Package(196.5, 0, "5")
        my_package6 = Package(193.5, 0)
        my_package7 = Package(199.5, 0, "89")

        packages_to_test = [my_package, my_package2, my_package3,
                            my_package4, my_package5, my_package6, my_package7]

        for package in packages_to_test:
            self.assertEqual(package.time_of_package_expiration(), -1)

    #
    def test_time_of_package_expiration(self):

        my_package = Package(19.5, 1)
        my_package2 = Package(20, 2)
        my_package3 = Package(119.5, 3)
        my_package4 = Package(199.5, 4, "1")
        my_package5 = Package(196.5, 5, "5")
        my_package6 = Package(193.5, 6)
        my_package7 = Package(199.5, 7, "89")

        packages_to_test = [my_package, my_package2, my_package3,
                            my_package4, my_package5, my_package6, my_package7]

        expected_results = ["0 day, 23:59:59.899999", "1 day, 23:59:59.898982", "2 days, 23:59:59.898091",
                            "3 days, 23:59:59.898091", "4 days, 23:59:59.898091", "5 days, 23:59:59.898091", "6 days, 23:59:59.898091"]

        counter = 0

        for package in packages_to_test:
            self.assertGreaterEqual(str(package.time_of_package_expiration()),
                                    expected_results[counter])
            counter += 1

    #
    def test_instance_error__argument1_types(self):

        types_to_test = [True, "", [], {}, False, None, "nil"]

        for elem in types_to_test:

            with self.assertRaises(TypeError):
                my_package = Package(elem, 1)

    #
    def test_instance_error__argument2_types(self):

        types_to_test = [True, "", [], {},
                         False, None, "nil", "900.9292", "&",
                         "27/2"]

        for elem in types_to_test:

            with self.assertRaises(TypeError):
                my_package = Package(10.2, elem)

        # def test_sum_tuple(self):
        #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    #
    def test_elapsed_time(self):

        num_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for num in num_days:

            my_package = Package(20, num)
            my_package._Package__created_at = my_package._Package__created_at - \
                timedelta(days=num)
            time.sleep(1)
            res = my_package.elapsed_time()

            self.assertGreater(str(res), f"{num} day, 0:00:00")


if __name__ == '__main__':
    unittest.main()
