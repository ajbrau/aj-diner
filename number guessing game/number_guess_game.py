import random


def game():
  guess = int(input('please guess anumber between 1 and 20'))
  golden_number = random.randint(1,21)
  guesses = 0
  while guess != golden_number:
    guesses += 1
    if guess > golden_number:
      print(guess, "is too high!")
      if guesses > 8:
        print('you used your 8 guesses! game over...')
        break
    elif guess < golden_number:
      print(guess, "is too low!")
      if guesses > 8:
        print('you used your 8 guesses! game over...')
        break
    guess = int(input("guess again: "))
  else:
    print("nice work! It took you ", guesses + 1, " tries to guess the number!")

  
while True:
    game()
    restart = input('do you want to restart Y/N?')
    if restart == 'N':
        break
    elif restart == 'Y':
        continue
    else:
      restart = input('whoops! enter either y or n.')



