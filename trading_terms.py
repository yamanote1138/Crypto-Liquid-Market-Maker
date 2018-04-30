class TradingTerms():
  
  def __init__(self, pair, budget, low_price, mid_price, first_size, size_change):
    """Class initializes parameters to for building sequence of trades"""
    
    # Fixed variables for class
    self.pair = pair
    self.budget = budget
    
    self.first_size = first_size
    self.size_change = size_change
    
    if pair[4:] == 'USD':
      self.p_round = 2
    else:
      self.p_round = 5
    self.low_price = low_price
    self.mid_price = round(mid_price, self.p_round)
    self.high_price = 2*mid_price-low_price
    
    self.n = n_from_budget(
      budget, first_size, size_change, low_price, self.high_price) 
    self.price_change = round(
      (self.high_price - mid_price ) /(self.n/2), self.p_round)
    
    # Varibles that will change for buy and sell sequences
    f_b_size = first_size + size_change 
    f_b_price = mid_price - self.price_change
    f_s_price = mid_price + self.price_change
    
    # trading_sequences gives the variable info for each sequnce to be 
    # traded, sequences will be added as trades execute. 
    self.trading_sequences = []
    self.trading_sequences.append(
      {'side': 'sell', 'first_size': first_size,'first_price': f_s_price,
        'n': self.n/2})
    self.trading_sequences.append(
      {'side': 'buy', 'first_size': f_b_size, 'first_price': f_b_price, 
        'n': self.n/2})
      
    self.new_sequences = self.trading_sequences
    self.book = []
  
  def print_trades(self):
    print_review_of_trades(self)

  def list_trades(self):
    """Used to send trading sequences in new_sequences to be listed"""
    
    # Send each sequence in new_squences to GDAX and return orders to book
    for i in self.new_sequences:
      self.book += trading.send_trade_list(
        self.pair, # pair
        i['side'], # side
        i['first_size'], # first_trade_size
        self.size_change*2, # size_increase
        i['first_price'], # first_trade_price
        self.price_change, #price_increase
        self.n/2 # trade_count
      ) 
        
    # Empty new_sequence for future use
    self.new_sequences = []
    
    start_websocket()
    

