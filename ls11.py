import random

print('Welcome to my first game for Github.\n'
      'Below you need to enter number from 1 to 11.\n'
      'If numbers same - you winner!\n'
      'Else i print who it smaller or bigger')

you_win = 0

try:
      my_number = random.randint(0, 11)
      user_number = int(input('Here: '))
      for i in range(0, 2):
            if user_number == my_number:
                  you_win += 1
                  break
            elif user_number < 0:
                  print('You entered number smaller then 0, game vas broke, you lose :(')
                  you_win += 2
                  break
            elif user_number > 10:
                  print('You entered number bigger then 10, game vas broke, you lose :(')
                  you_win += 2
            elif user_number < my_number:
                  print('My number bigger then your')
                  user_number = int(input('Enter here new number: '))
            elif user_number > my_number:
                  print('My number smaller then your')
                  user_number = int(input('Enter here new number: '))
      if you_win == 1:
            print('You enter the same number. You win! :)')
      elif you_win == 0:
            print("You haven't no mere chances. You lose")
      elif you_win ==  2:
            pass

except:
      print('You entered NOT number, you lose, game over :(')