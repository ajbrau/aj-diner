from collections import namedtuple

EntreeMenuEntry = namedtuple('EntreeMenuEntry', ['index', 'name', 'price'])
_menu = []
_menu.append(EntreeMenuEntry(1, 'salad', 7.99))
_menu.append(EntreeMenuEntry(2, 'steak', 13.99))
_menu.append(EntreeMenuEntry(3, 'burger', 9.99))
_menu.append(EntreeMenuEntry(4, 'sandwich', 8.99))

steakPref = {1: 'rare', 2: 'medium-rare', 3: 'medium', 4: 'well-done'}

for thing in _menu:
  index = thing.index
  name = thing.name
  price = thing.price
  print(index, name, price)
  

  
choice1 = int(input('Please choose an Entree Item by number: '))
for item in _menu:
  if item.index == choice1:
    entree = item
    print(f'you have selected "{item.name}" which will be ${item.price}')
    if item.name == 'steak':
      pref = int(input('How would you like your steak cooked? 1: rare 2: medium-rare 3: medium 4: well done. Enter number here: '))
      for x in steakPref.keys():
        if pref == x:
          print(f'got it! we will cook your steak: {steakPref[x]}')
        
        
    

SideMenuEntry = namedtuple('SideMenuEntry', ['index', 'name', 'price'])
_sidemenu = []
_sidemenu.append(SideMenuEntry(1, 'fruit', 4.99))
_sidemenu.append(SideMenuEntry(2, 'fries', 2.99))
_sidemenu.append(SideMenuEntry(3, 'chips', 1.99))
_sidemenu.append(SideMenuEntry(4, 'broccoli', 2.99))

for item in _sidemenu:
  index = item.index
  name = item.name
  price = item.price
  print(index, name, price)
  
choice2 = int(input('Please choose a side by number: '))
for item in _sidemenu:
  if item.index == choice2:
    side = item
    print(f'you have selected "{item.name}" which will be ${item.price}')

subtotal = entree.price + side.price
print(f'Your total price before tax and tip will be: ${subtotal}')
tip_percent = int(input('what tip percentage would you like? (ex: 10) enter here: '))
total = round((subtotal*(tip_percent/100)) + (subtotal* 1.06), 2)
print(f'your total with your tip and tax will be ${total}')