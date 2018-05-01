import pytest
import prompts

def test__get_low_price():
  # method should throw error if medium_price is higher than high_price
  #self.assertRaises(ValueError, _get_low_price, 3, 2)
  
  # method should give expected result for integers
  assert prompts._get_low_price(4,6) == 2

  # method should give expected result for floats
  assert prompts._get_low_price(.04,.06) == 0.020000000000000004

  with pytest.raises(ValueError):
    prompts._get_low_price(5,4)
