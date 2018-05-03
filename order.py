class Order:
  # add definition of side property here
  @property
  def side(self): return self._side

  @budget.setter
  def side(self, value):
    if value != "buy" and value != "sell":
      raise ValueError("side must be 'buy' or 'sell'")
    self._side = value

  {'side': 'sell', 'min_size': min_size,'first_price': f_s_price,
    #     'n': self.n/2})
