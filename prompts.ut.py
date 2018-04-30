import unittest
from prompts import _get_low_price

class BasicTestCase(unittest.TestCase):
  """Tests for `basic.py`."""

  def test__get_low_price(self):
    """does 2+3=5?"""
    self.assertRaises(ValueError, _get_low_price, 3, 2)
    self.assertEqual(_get_low_price(4,6), 2)
    self.assertEqual(_get_low_price(.04,.06), 0.020000000000000004)

if __name__ == '__main__':
  unittest.main()
