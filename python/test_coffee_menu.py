import coffee_menu
import unittest

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = coffee_menu.CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('espresso'), 2.50)
        self.assertEqual(self.menu.get_price('latte'), 2.75)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(ValueError):
            self.menu.get_price('mocha')

    def test_add_item(self):
        self.menu.add_item('mocha', 3.00)
        self.assertEqual(self.menu.get_price('mocha'), 3.00)