import unittest
from prompts import _get_low_price

class BasicTestCase(unittest.TestCase):
  """Tests for `basic.py`."""

  def test__get_low_price(self):
    """does 2+3=5?"""
    # method should throw error if medium_price is higher than high_price
    self.assertRaises(ValueError, _get_low_price, 3, 2)
    # method should give expected result for integers
    self.assertEqual(_get_low_price(4,6), 2)
    # method should give expected result for floats
    self.assertEqual(_get_low_price(.04,.06), 0.020000000000000004)

if __name__ == '__main__':
  unittest.main()
