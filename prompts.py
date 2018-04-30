import os
import readline
from pick import pick

def _input_default(prompt, default):
  def hook():
    readline.insert_text(default)
    readline.redisplay()
  readline.set_pre_input_hook(hook)
  result = input(prompt)
  readline.set_pre_input_hook()
  return result

def _prompt_float(title, default):
  while True:
    try:
      value = _input_default("\n"+title+"\n\n", default)
      value = float(value)
    except ValueError:
      print("\nplease enter a valid float value (e.g. .01, 1.75)\n\n")
      continue
    else:
      break
  return value

def _prompt_bool(title, default):
  while True:
    value = _input_default("\n"+title+"  (y/n)\n\n", default)
    value = value.lower()
    if value=='y':
      return True
    elif value=='n':
      return False
    else:
      print("\nplease type 'y' or 'n'\n\n")
      continue

def _prompt_list(title, list, default_index):
  value, index = pick(list, title, default_index=default_index)
  print("\n"+title+"\n\n"+value+"\n\n")
  return value

def _get_low_price(mid_price, high_price):
  if(mid_price > high_price): raise ValueError("mid price cannot be higher than high price")
  return ((2 * mid_price) - high_price)

def show_intro():
  # display header and description of program intent
  print(
    "** Crypto Liquid Market Maker - By William P. Fey **\n"+ \
    "This program will list a sequence of buy and sell trades on \n"+ \
    "GDAX.com based on pertinent user input.\n\n"
  )
  input("Press return to continue...")
  # clear screen
  os.system('clear')

def prompt_user():
  #Prompts User for input to start algorithm, returns dictionary of selected values.
  show_intro()

  options = {}

  supported_pairs = ["BTC-USD", "ETH-USD", "LTC-USD", "BCH-USD", "BTC-ETH", "LTC-BTC", "BCH-BTC"]
  selected_pair = _prompt_list(
    "What trading pair would you like to use?",
    supported_pairs,
    6
  )

  # split pair into pertinent parts
  options.pair_start = selected_pair[:3]
  options.pair_end = selected_pair[:4]
  
  options.budget = _prompt_float(
    ("What is the value of {0} would you like to allocate in terms of {1}?").format(
      options.pair_start,
      options.pair_end
    ),
    ".075"
  )

  options.min_size = _prompt_float(
    "What is the minimum trade size for this pair?",
    ".01"
  )

  options.size_change = _prompt_float(
    "How much should each trade in the sequence of buys and sells increase by?",
    ".000025"
  )
  
  options.current_price = _prompt_float(
    ("What is the estimated price of {0} in terms of {1}?").format(
      options.pair_start,
      options.pair_end
    ),
    ".15185"
  )

  use_current_price = _prompt_bool(
    ("Would you like to use {0} {1}/{2} as the the midpoint of the trading algorithm?").format(
      options.current_price,
      options.pair_end,
      options.pair_start
    ),
    "y"
  )
  
  if not use_current_price:
    options.mid_price = _prompt_float("What midpoint price would you like to use?")
  else:
    options.mid_price = options.current_price
  
  options.high_price = _prompt_float(
    "What is the highest price to be sold at?",
    ".3"
  )

  options.low_price = _get_low_price(options.mid_price, options.high_price)

  return options

def prompt_ready_to_trade():
  list_trades = _prompt_bool("Would you like trades to be listed?", "n")
  if list_trades:  
    return True
  else:
    change_input = _prompt_bool("Would you like to change your input?", "n")
    return change_input

def prompt_to_return_class():
  return _prompt_bool("Would you like to return trades as a class?", "n")
