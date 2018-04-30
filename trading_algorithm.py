import requests, math, trading
import authorize as autho

def n_from_budget(budget, first_size, size_change, low_price, high_price):
  '''Using a budget in terms of the denominator of a trading pair (USD for
  BTC-USD), first_size and size_change of trade amounts, and a price range
  for trade values in terms of low_price and high_price this function will 
  give you the maximoum possible trades that can be used in a sequence of 
  alternating increasing buy and sell trades. 
  
  >>> n_from_budget(193, .01, .005, 500, 1300)
  8
  '''
  
  mid_price = ( low_price + high_price ) / 2
  
  A = 12 * size_change * mid_price
  B = 3 * ( 
    mid_price * ( 
      4 * first_size - 3 * size_change) + size_change * low_price )
  C = -3 * ( size_change * ( high_price - mid_price ) + 2 * budget ) 
  
  return 2*int(( - B + math.sqrt( B ** 2 - 4 * A * C))  / (2*A) )
  
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

def n_from_mid_budget(budget, first_size, size_change, mid_price, last_price):
  '''
  Takes a budget, first_size, size_change, mid_price, and last_price which
  could both be a high or low price. 
  >>> n_from_mid_budget(60,.01,.01,900,500)
  4.0
  >>> ta.n_from_mid_budget(120,.01,.01,900,1300)
  4.0
  '''
  
  A = size_change*(mid_price+2*last_price)
  B = 3*first_size*(
    mid_price+last_price)-3*size_change*mid_price
  C = (3*first_size-2*size_change)*(last_price-mid_price)-6*budget
  return (-B + math.sqrt(B**2-4*A*C))/(2*A)

def start_websocket():
  '''yet to be built'''
  print ('\nStill a work in progress parsing websocket...')
