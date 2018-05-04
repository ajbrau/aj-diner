import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']
player2 = None
p2_score = 0
p1_score = 0
player1 = None
print(moves)
while p1_score < 4 and p2_score < 4:
  player1 = input('PLAYER! please type your move: ')
  player2 = input('PLAYER2 please type your move: ')
  if player1 == player2:
    print("It's a tie!")
  elif player1 == 'rock':
    if player2 == 'paper' or player2 == 'spock':
      print('Player2 won!')
      print(f'player1 played {player1} and player2 played {player2}')
      p2_score += 1
    elif player2 == 'lizard' or player2 == 'scissors':
      print('Player1 won!')
      print(f'player1 played {player1} and player2 played {player2}')
      p1_score += 1
  elif player1 == 'paper':
    if player2 == 'scissors' or player2 == 'lizard':
      print('Player2 won!')
      print(f'player1 played {player1} and player2 played {player2}')
      p2_score += 1
    elif player2 == 'rock' or player2 == 'spock':
      print('Player1 won!')
      print(f'player1 played {player1} and player2 played {player2}')
      p1_score += 1
  elif player1 == 'scissors':
    if player2 == 'rock' or player2 == 'spock':
      print('you lose!')
      print(f'player1 played {player1} and player2 played {player2}')
      p2_score += 1
    elif player2 == 'paper' or player2 == 'lizard':
      print('Player1 won!')
      print(f'player1 played {player1} and player2 played {player2}')
      p1_score += 1
  elif player1 == 'lizard':
    if player2 == 'scissors' or player2 == 'rock':
      print('Player2 won!')
      print(f'player1 played {player1} and player2 played {player2}')
      p2_score += 1
    elif player2 == 'paper' or player2 == 'spock':
      print('Player1 won!')
      print(f'player1 played {player1} and player2 played {player2}')
      p1_score += 1
  elif player1 == 'spock':
    if player2 == 'paper' or player2 == 'lizard':
      print('Player2 won!')
      print(f'player1 played {player} and player2 played {player2}')
      p2_score += 1
    elif player2 == 'scissors' or player2 == 'rock':
      print('Player1 won!')
      print(f'player1 played {player} and player2 played {player2}')
      player_score += 1
  else:
    print('invalid entry try again!')
  print(f'player1: {p1_score} player2: {p2_score}')
else:
  if p1_score > p2_score:
    print('PLAYER 1 WINNNSSS!!!!!!')
  else:
    print("PLAYER 2 WINNNSSS!!!!!!")
