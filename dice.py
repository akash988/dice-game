import random


while True:
      print(random.randint(1,6))
      a=input("You Want to roll the dice again?(y/n)")
      if a=="y":
          continue
      else:
          break
