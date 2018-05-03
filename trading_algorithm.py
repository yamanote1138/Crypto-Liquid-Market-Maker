import requests, math, trading
import authorize as autho

<<<<<<< HEAD
=======
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
    
    # trading_sequences gives the variable info for each sequence to be 
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
    """Used to send trading sequences in new_sequences to be listed
    """
    
    # Send each sequence in new_squences to GDAX and return orders to book
    for i in self.new_sequences:
      self.book += trading.send_trade_list(
        self.pair, # pair
        i['side'], # side
        i['first_size'], # first_trade_size
        self.size_change*2, # size_increase
        i['first_price'], # first_trade_price
        self.price_change, #price_increase
        self.n/2 - 1 # trade_count minus 1 as trade function starts at 0
      ) 
        
    # Empty new_sequence for future use
    self.new_sequences = []
    
    start_websocket()
    

>>>>>>> master

  
def print_review_of_trades(tt):
  '''Takes a class tt for trading_terms generated by TradingTerms() class and 
  lists the trades that would be listed under current state of trading_terms
  '''
     
  strings = {'buy' : [], 'sell' : []}
  budgets = {'buy' : 0 , 'sell' : 0}
  
  # Header
  print ( '\n' )
  print( 'buys'+'\t'*5+'sells' )   
  
  # Build strings "size BOT @ price TOP / BOT" where pair = TOP-BOT
  for i in tt.new_sequences:
    # for loop through trade counts = i['n']
    for j in range(0, int(i['n']-1)):
      
      # -1 or 1 depending on i['side']
      pos_neg = 1 - 2 * ('buy' == i['side'])
  
      size = round ( i['first_size'] + j * tt.size_change * 2 , 5)
      price = round (
        i['first_price'] + pos_neg * j * tt.price_change, 5)
      
      strings[i['side']].append(
        "{0} {1} @ {2} {3}/{1}".format(
          size, tt.pair[:3], price, tt.pair[4:] 
          )
        )
      
      if i['side'] == 'buy':
        budgets['buy'] += size * price
      else:
        budgets['sell'] += size
    
  # Print strings expect out of range error if sizes are unequal
  for i in range(0, len(strings['buy'])):
    print( strings['buy'][i] + '\t' * 2 + strings['sell'][i] )
  
  print ( '\n' )
  print ('Buy budget: {0} {1}, Sell budget {2} {3} roughly worth {4} {1} '
    .format(
      budgets['buy'],
      tt.pair[4:],
      budgets['sell'],
      tt.pair[:3], 
      budgets['sell'] * tt.mid_price) + \
      'based on {5} {1}/{3} midmarket price.'.format(
        budgets['buy'],
        tt.pair[4:],
        budgets['sell'],
        tt.pair[:3], 
        budgets['sell'] * tt.mid_price,
        tt.mid_price
      )
    ) 

