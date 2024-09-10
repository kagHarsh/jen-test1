import unittest
from parameterized import parameterized
# parametrized-- pass parameters to the test case
def tax_calc(cost, tax):
    if cost < 0 or tax < 0:
        return "Invalid"
    return (cost*(tax/100)) + cost
 
class TestMultiplyFunction(unittest.TestCase):
# annotation/ decorators-->  pass metadata
    @parameterized.expand([
        ("pen", 10, 1, 10.1),
        ("car", 100, 10, 110.0),
        ("food", 100, 28, 128.0),
        ("Book", 100, -28, "Invalid"),
        ("Bike", -100, 28, "Invalid"),
        ("Bag", -100, -28, "Invalid"),
    ])
    def test_multiply(self, name, x, y, expected):
        self.assertEqual(tax_calc(x, y), expected)
 
if __name__ == '__main__':
    unittest.main()