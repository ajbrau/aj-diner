## print header and rules
## add money to wallet

#game
#print the game board
##pick a number between one and 36
#"spin" a random number
#return winnings

import random

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
print('odd: 1/10 winnings if odd number is landed upon')
print('even: 1/10 winnings if even number is landed upon')
print('1st 12: 1/4 winnings if landed number is in the 1st 12th')
print('2nd 12: 1/4 winnings if landed number is in the 2nd 12th')
print('3rd 12: 1/4 winnings if landed number is in the 3rd 12th')
print('number: JACKPOT! recieve all the money you have lost plus a thousand dollars more')
print('                                      ')
print('To quit type in "QUIT" instead of your bet')
print('                                      ')

bets = ['even', 'odd', '1st 12', '2nd 12', '3rd 12']
wallet = int(input('How much would you like in your initial wallet?'))
losses = 0
rounds = 0
bet = None
while bet != 'QUIT':
  while wallet > 0:
    num = random.randint(1,37)
    bet = input('Type your bet: ')
    money = int(input('How much you going to risk? (in dollars): '))
    if isinstance(bet, int) == True:
      bet_int = int(bet)
      if bet_int == num:
        print(f'JACKPOT! the roullete landed on {num}')
        winnings = losses + 1000
        wallet += winnings
        rounds += 1
      else:
        print('nope!')
        wallet -= money
    else:
      if bet == 'even' and num % 2 == 0:
        print('both numbers are even!')
        rounds += 1
        winnings = money * 1/10
        wallet += winnings
      elif bet == 'odd' and num % 2 != 0:
        print('both numbers are odd!')
        rounds += 1
        winnings = money * 1/10
        wallet += winnings
      elif bet == '1st 12' and num <= 12:
        print('landed in the first 12!')
        rounds += 1
        winnings = money * 1/4
        wallet += winnings
      elif bet == '2nd 12' and 12 < num < 25:
        print('landed in the second 12!')
        rounds += 1
        winnings = money * 1/4
        wallet += winnings
      elif bet == '3rd 12' and 24 < num < 37:
        print('landed in the third 12!')
        rounds += 1
        winnings = money * 1/4
        wallet += winnings
      else:
        print('nope!')
        wallet -= money
        rounds += 1
    print(f'wallet: {wallet}')
  else:
    print('you ran out of money! add more to play or enter 0 to stop playing')
    wallet_input = int(input('Add more dollars: '))
    if wallet_input > 0:
      wallet += wallet_input
      print(f'nice! Now there is ${wallet} in your wallet')
    elif wallet_input == 0:
      print('ok see you later!')
  