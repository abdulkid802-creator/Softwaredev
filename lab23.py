import unittest
from shipping import Shipping


class ShippingTest(unittest.TestCase):

    def setUp(self):
        self.standard_shipment = Shipping(4, False, False)
        self.express_international_shipment = Shipping(10, True, True)
        self.invalid_shipment = Shipping(-2, False, False)

    def test_valid_shipment(self):
        self.assertTrue(self.standard_shipment.is_valid())

    def test_invalid_shipment(self):
        self.assertFalse(self.invalid_shipment.is_valid())

    def test_base_cost_under_5(self):
        self.assertEqual(self.standard_shipment.base_cost(), 8)

    def test_base_cost_mid_range(self):
        self.assertEqual(self.express_international_shipment.base_cost(), 15)

    def test_base_cost_over_20(self):
        large_shipment = Shipping(25)
        self.assertEqual(large_shipment.base_cost(), 30)

    def test_total_cost_standard(self):
        self.assertEqual(self.standard_shipment.total_cost(), 8)

    def test_total_cost_express_only(self):
        express_shipment = Shipping(9, express=True, international=False)
        self.assertEqual(express_shipment.total_cost(), 27)

    def test_total_cost_international_only(self):
        international_shipment = Shipping(25, express=False, international=True)
        self.assertEqual(international_shipment.total_cost(), 50)

    def test_total_cost_express_and_international(self):
        self.assertEqual(self.express_international_shipment.total_cost(), 47)

    def test_total_cost_invalid(self):
        self.assertEqual(self.invalid_shipment.total_cost(), None)

    def test_no_express_surcharge(self):
        self.assertFalse(self.standard_shipment.express)
        self.assertEqual(self.standard_shipment.express_surcharge(), 0)

    def test_no_international_surcharge(self):
        self.assertFalse(self.standard_shipment.international)
        self.assertEqual(self.standard_shipment.international_surcharge(), 0)

if __name__ == "__main__":
    unittest.main()