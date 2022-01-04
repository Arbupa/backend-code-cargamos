from locations import Locations
import random
import unittest


class TestLocations(unittest.TestCase):

    # testing create_cube with random positive numbers.
    def test_create_cube(self):

        for num in range(50):

            location = Locations(random.randint(1, 10), random.randint(
                1, 100), random.randint(1, 1000))

            self.assertEqual(location.create_cube(),
                             "Cube created succesfully")

    # testing create_cube with random negative numbers.
    def test_create_cube2(self):

        for num in range(50):

            location = Locations(random.randint(-10, 0), random.randint(
                -100, 0), random.randint(-1000, 0))

            self.assertEqual(location.create_cube(),
                             "Cube not created due to 0 property")

    # test to know if the length is calculated correct
    def test_cube_length(self):

        for num in range(50):
            location = Locations(random.randint(-10, 0), random.randint(
                -100, 0), random.randint(-1000, 0))

            self.assertEqual(location.cube_length, (location.x_position *
                                                    location.y_position * location.z_position))

    # func to obtain not stored values
    def test_get_value(self):

        numbers_list = [num for num in range(1, 100)]

        for num in numbers_list:
            location = Locations(num, num, num)
            location.create_cube()

            self.assertEqual(location.get_value(
                num, num, num), "Value not found.")

    # test a sample save value inside our list.
    def test_save_value(self):

        location = Locations(3, 4, 7)
        location.create_cube()

        self.assertEqual(location.save_value("Hello, World",
                                             1, 3, 7), "Value saved successfully")

    # func to storage values in coordinates not found.
    def test_save_value2(self):

        location = Locations(3, 3, 3)
        location.create_cube()
        location2 = Locations(4, 4, 4)
        location2.create_cube()
        location3 = Locations(5, 5, 5)
        location3.create_cube()
        location4 = Locations(6, 6, 6)
        location4.create_cube()
        location5 = Locations(7, 7, 7)
        location5.create_cube()
        location5 = Locations(8, 8, 8)
        location5.create_cube()
        location5 = Locations(9, 9, 9)
        location5.create_cube()

        self.assertEqual(location.save_value(
            "arremangala", 10, 10, 10), "Coordinates not found. Value not saved")
        self.assertEqual(location2.save_value(
            "arrempujala", 11, 11, 11), "Coordinates not found. Value not saved")
        self.assertEqual(location3.save_value(
            "arremangala", 12, 12, 12), "Coordinates not found. Value not saved")
        self.assertEqual(location4.save_value(
            "arrempujala", 13, 13, 13), "Coordinates not found. Value not saved")
        self.assertEqual(location5.save_value(
            "arremangala", 14, 14, 14), "Coordinates not found. Value not saved")
        self.assertEqual(location.save_value(
            "arrempujala", 15, 15, 15), "Coordinates not found. Value not saved")
        self.assertEqual(location.save_value(
            "si...", 16, 16, 16), "Coordinates not found. Value not saved")

    # test save_value, get_value and get all in the same test.
    def test_save_value3(self):

        location = Locations(3, 4, 7)
        location.create_cube()

        self.assertEqual(location.save_value("Hello, World",
                                             2, 2, 2), "Value saved successfully")

        self.assertEqual(location.get_value(2, 2, 2), "Hello, World")
        self.assertEqual(location.get_all(), ["Hello, World"])

    # test get_all func with no values saved
    def test_get_all(self):

        for num in range(20):
            location = Locations(random.randint(1, 10), random.randint(
                1, 100), random.randint(1, 1000))

            self.assertEqual(location.get_all(),
                             [])


if __name__ == '__main__':
    unittest.main()
