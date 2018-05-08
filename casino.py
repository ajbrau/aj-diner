import random
import copy

print('--------------------------------------')
print('|34|31|28|25| |22|19|16|13| |10|7|4|1|')
print('--------------------------------------')
print('|35|32|29|26| |23|20|17|14| |11|8|5|2|')
print('--------------------------------------')
print('|36|32|30|27| |24|21|18|15| |12|9|6|3|')
print('--------------------------------------')
print(' |  3rd 12  | |   2nd 12  | | 1st 12 |')
print('--------------------------------------')
print('           | odd |  | even |          ')
print('           ----------------           ')
print('                                      ')
print('           ---------------            ')
print('            POSSIBLE BETS             ')
print('           ---------------            ')
print('                                      ')
print('odd: 1/3 winnings if odd number is landed upon')
print('even: 1/3 winnings if even number is landed upon')
print('1st 12: 1/2 winnings if landed number is in the 1st 12th')
print('2nd 12: 1/2 winnings if landed number is in the 2nd 12th')
print('3rd 12: 1/2 winnings if landed number is in the 3rd 12th')
print('number: JACKPOT! recieve all the money you have lost plus a thousand dollars more')
print('                                      ')
print('To cash out type in "QUIT" instead of your bet')
print('-Example: What would you like to bet on?: QUIT-')
print('                                      ')

bets = {'even', 'odd', '1st 12', '2nd 12', '3rd 12', 'QUIT'}
while True:
  try:
    wallet = float(input('How much would you like in your initial wallet?'))
  except ValueError:
    print('make sure you enter a number! try again')
    continue
  if wallet < 0:
    print("whoops! that's a negative number, try again!")
    continue
  else:
    break
total_inputs = copy.copy(wallet)
losses = 0.00
rounds = 1
cash = 0.00
bet = None
winnings = 0
wl = ''
difference = 0
y = True
yes_or_no = {'yes', 'no'}
#while user's input isn't 'QUIT' continue running through the game loop
while bet != 'QUIT':
  #while there is money in the wallet, continue running through the game loop
  while round(wallet) > 0:
    num = random.randint(1,37)
    print('----------------------------------------------------------------')
    print(f'round: {rounds}')
    while True:
      try:
         money = float(input('How much would you like to bet? (ex 10.50): '))
         money <= wallet
      except ValueError:
          print("Not an integer! Try again.")
          continue
      if money < 0:
         print("whoops! that's a negative number. try again")
         continue
      if round(money, 3) > round(wallet, 3):
         print("you can't bet more than you have in your wallet silly!")
         continue
      else:
         break 
    bet = input("What would you like to bet on? ex:'odd': ")
    if bet.isdigit() == True:
      bet_num = float(bet)
      if bet_num == num:
        print(f'JACKPOT! the roullete landed on {num}')
        winnings = losses + 1000
        wallet += winnings
        rounds += 1
        cash += winnings
        wl = 'won'
        print('!!!!JACKPOT!!!!')
      else:
        wallet -= money
        losses += money
        wl = 'lost'
    else:
      #check to make sure input is a valid input
      if bet in bets:  
        if bet == 'even' and num % 2 == 0:
          rounds += 1
          winnings = money * 1/3
          wallet += winnings
          cash += winnings
          wl = 'won'
        elif bet == 'odd' and num % 2 != 0:
          rounds += 1
          winnings = money * 1/3
          wallet += winnings
          cash += winnings
          wl = 'won'
        elif bet == '1st 12' and num <= 12:
          print('landed in the first 12!')
          rounds += 1
          winnings = money * 1/2
          wallet += winnings
          cash += winnings
          wl = 'won'
        elif bet == '2nd 12' and 12 < num < 25:
          print('landed in the second 12!')
          rounds += 1
          winnings = money * 1/2
          wallet += winnings
          cash += winnings
          wl = 'won'
        elif bet == '3rd 12' and 24 < num < 37:
          print('landed in the third 12!')
          rounds += 1
          winnings = money * 1/2
          wallet += winnings
          cash += winnings
          wl = 'won'
        elif bet == 'QUIT':
          print(f'ok bye! your final wallet is: {round(wallet, 3)}')
          if wallet > total_inputs:
            print(f'your total net winnings are: ${round((wallet - total_inputs),2)}')
          else:
            print(f'your total net losses are: ${round((wallet - total_inputs),2)}')
          break
        else:
          wallet -= money
          losses += money
          rounds += 1
          wl = 'lost'
      else: 
        print('not a valid entry, try again!')
    print(f'ROULLETE ROLL: {num}')
    if wl == 'won':
      difference = f'${round(winnings, 3)}'
    else:
      difference = (f'-${round(money, 2)}')
    print(f'you {wl} {difference}')
    print(f'wallet: ${round(wallet, 2)}')
    print(f'total winnings: ${round(cash, 3)}')
    print(f'total losses: ${round(losses, 3)}')
  else:
    print('You ran out of money! Add more to play or type 0 to stop playing.')
    wallet_input = int(input('Dollar amount: '))
    if wallet_input > 0:
      wallet += wallet_input
      total_inputs += wallet_input
      print(f'sweet! now you have ${round(wallet, 3)} in your wallet. Lets keep playing!')
      x = False
      break
    elif wallet_input == 0:
      confirm = input('Do you really want to quit? type yes or no:')
      if confirm == 'yes':
        print(f'ok bye! your final wallet is: {round(wallet, 3)}')
        if wallet > total_inputs:
          print(f'your total net winnings are: ${round((wallet - total_inputs),2)}')
        else:
          print(f'your total net losses are: ${round((wallet - total_inputs),2)}')
        break
      elif confirm == 'no':
        print('ok, lets keep playing!')
        break
    else:
      break
