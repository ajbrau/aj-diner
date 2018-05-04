import random

entree_menu = [['steak', 12.99], ['salad', 8.99], ['sandwich', 9.99], ['burger', 11.99]]
side_menu = [['fries', 2.99], ['salad', 4.99], ['fruit', 2.99]]
comments = ['nice choice!', 'sound yummy!', "I wouldn't have chosen that but ok"]
comment = random.choice(comments)
print('Please Choose an Entree from the menu', entree_menu)
entree_choice = input('Entree: ')
print(comment)
print('Please choose a side', side_menu)
side_choice = input('Side: ')
print(comment)