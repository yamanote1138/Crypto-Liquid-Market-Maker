class TradingTerms():

  supported_pairs = ["BTC-USD", "ETH-USD", "LTC-USD", "BCH-USD", "BTC-ETH", "LTC-BTC", "BCH-BTC"]
  default_pair_index = 6
  
  # add definition of pair property here
  @property
  def pair(self): return self._pair

  @pair.setter
  def pair(self, value):
    if value not in self.supported_pairs:
      raise ValueError("supplied pair '{}' is not supported".format(value))
    self._pair = value

    # split pair into pertinent parts
    self._pair_from = self._pair[:3]
    self._pair_to = self._pair[4:]

    if self._pair_to == 'USD':
      self._p_round = 2
    else:
      self._p_round = 5

  # add definition of pair_from property here
  @property
  def pair_from(self): return self._pair_from

  # add definition of pair_to property here
  @property
  def pair_to(self): return self._pair_to

  # add definition of budget property here
  @property
  def budget(self): return self._budget

  @budget.setter
  def budget(self, value):
    self._budget = value

  # add definition of first_size property here
  @property
  def first_size(self): return self._first_size

  @first_size.setter
  def first_size(self, value):
    self._first_size = value

  # add definition of size_change property here
  @property
  def size_change(self): return self._size_change

  @size_change.setter
  def size_change(self, value):
    self._size_change = value
    
  # add definition of low_price property here
  @property
  def low_price(self): return self._low_price

  @low_price.setter
  def low_price(self, value):
    self._low_price = round(value, self._p_round)
    
  # add definition of mid_price property here
  @property
  def mid_price(self): return self._mid_price

  @mid_price.setter
  def mid_price(self, value):
    self._mid_price = round(value, self._p_round)

  # add definition of high_price property here
  @property
  def high_price(self): return self._high_price

  @high_price.setter
  def high_price(self, value):
    self._high_price = round(value, self._p_round)

  # add definition of high_price property here
  @property
  def computed_high_price(self):
    if (self._low_price is None):
      raise ValueError('cannot compute high price, low price not set')
    if (self._mid_price is None):
      raise ValueError('cannot compute high price, mid price not set')
    return (2 * self.mid_price) - self._low_price


  def __init__(self):
    return
    # self.n = n_from_budget(
    #   budget, first_size, size_change, low_price, self.high_price) 
    # self.price_change = round(
    #   (self.high_price - mid_price ) /(self.n/2), self.p_round)
    
    # # Variables that will change for buy and sell sequences
    # f_b_size = first_size + size_change 
    # f_b_price = mid_price - self.price_change
    # f_s_price = mid_price + self.price_change
    
    # # trading_sequences gives the variable info for each sequence to be 
    # # traded, sequences will be added as trades execute. 
    # self.trading_sequences = []
    # self.trading_sequences.append(
    #   {'side': 'sell', 'first_size': first_size,'first_price': f_s_price,
    #     'n': self.n/2})
    # self.trading_sequences.append(
    #   {'side': 'buy', 'first_size': f_b_size, 'first_price': f_b_price, 
    #     'n': self.n/2})
      
    # self.new_sequences = self.trading_sequences
    # self.book = []
  
  def toString(self):
    print(
      " from: \t\t\t{}\n".format(self.pair_from),
      "to: \t\t\t{}\n".format(self.pair_to),
      "budget: \t\t{}\n".format(self.budget),
      "first_size: \t\t{}\n".format(self.first_size),
      "size_change: \t\t{}\n".format(self.size_change),
      # "low_price: \t\t{}\n".format(self.low_price),
      "mid_price: \t\t{}\n".format(self.mid_price),
      "high_price: \t\t{}\n".format(self.high_price)
    )


  # def print_trades(self):
  #   print_review_of_trades(self)

  # def list_trades(self):
  #   """Used to send trading sequences in new_sequences to be listed"""
    
  #   # Send each sequence in new_squences to GDAX and return orders to book
  #   for i in self.new_sequences:
  #     self.book += trading.send_trade_list(
  #       self.pair, # pair
  #       i['side'], # side
  #       i['first_size'], # first_trade_size
  #       self.size_change*2, # size_increase
  #       i['first_price'], # first_trade_price
  #       self.price_change, #price_increase
  #       self.n/2 # trade_count
  #     ) 
        
  #   # Empty new_sequence for future use
  #   self.new_sequences = []
    
  #   start_websocket()
    

