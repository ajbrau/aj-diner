import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']
computer = moves[random.randint(0,4)]
comp_score = 0
player_score = 0
player = False
print(moves)
while player_score <= 4 and comp_score<= 4:
  player = input('Please type your move:')
  if player == computer:
    print("It's a tie!")
  elif player == 'rock':
    if computer == 'paper' or computer == 'spock':
      print('you lose!')
      print(f'you played {player} and the computer played {computer}')
      comp_score += 1
    elif computer == 'lizard' or computer == 'scissors':
      print('you win!')
      print(f'you played {player} and the computer played {computer}')
      player_score += 1
  elif player == 'paper':
    if computer == 'scissors' or computer == 'lizard':
      print('you lose!')
      print(f'you played {player} and the computer played {computer}')
      comp_score += 1
    elif computer == 'rock' or computer == 'spock':
      print('you win!')
      print(f'you played {player} and the computer played {computer}')
      player_score += 1
  elif player == 'scissors':
    if computer == 'rock' or computer == 'spock':
      print('you lose!')
      print(f'you played {player} and the computer played {computer}')
      comp_score += 1
    elif computer == 'paper' or computer == 'lizard':
      print('you win!')
      print(f'you played {player} and the computer played {computer}')
      player_score += 1
  elif player == 'lizard':
    if computer == 'scissors' or computer == 'rock':
      print('you lose!')
      print(f'you played {player} and the computer played {computer}')
      comp_score += 1
    elif computer == 'paper' or computer == 'spock':
      print('you win!')
      print(f'you played {player} and the computer played {computer}')
      player_score += 1
  elif player == 'spock':
    if computer == 'paper' or computer == 'lizard':
      print('you lose!')
      print(f'you played {player} and the computer played {computer}')
      comp_score += 1
    elif computer == 'scissors' or computer == 'rock':
      print('you win!')
      print(f'you played {player} and the computer played {computer}')
      player_score += 1
  else:
    print('invalid entry try again!')
else:
  if player_score > comp_score:
    print('GAME OVER YOU WIN YAYYYYY!')
  else:
    print("YOU LOOOOOOOOOOOSSSEE!!! GAME. OVER.")