import time
import random
import sys
import threading
import select

from requests import options

def slow_print(text, speed=0.04, newline=True):
    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush()      
        time.sleep(speed)       
    if newline:
        print() 

prod = [
  "Oprah Winfrey",
  "Gu-Gu-Gu",
  "Degraded Versions",
  "Denial",
  "Mickey Mouse's Pants",
  "God",
  "Jeffrey Epstein",
  "Donald Drump",
  "Satan",
  "'berries'",
  "Vietnam"
  ]
slogan = [
  "sample text",
  "Absolutely not 'bees' backwards",
  "not illegal, we prefer 'legally distinct'",
  "Hey, isn't this product supposed to be in jail?",
  "Your mother is a prostitute unless you buy this product"
]

side_effect = [
  "Causes extreme denial",
  "Scary hallucinations of Mickey Mouse",
  "God in all of his true glory shining down upon you and yours",
  "Sudden urges to visit Epstein island",
  "Makes you believe Diddy is behind you at all times",
  "becoming a muffin",
  "getting trapped in a Vietnam war flashback",
  "controllable laughter",
  "privilege of killing every single human on the planet."
]

def advertisement():
  slow_print(f"Introducing {random.choice(prod)}!")
  slow_print(f"Our Slogan: {random.choice(slogan)}")
  slow_print(f"Side Effects May Include: {random.choice(side_effect)}")

def start_of_game():
  slow_print("Welcome to The Muffin Game!")
  time.sleep(2)
  slow_print("Here, you run a cafe")
  time.sleep(2)
  print()
  advertisement()
  time.sleep(2)
  slow_print("These are your options: ", newline=False)
  options = input("1. Bake Muffins\n2. Bake Cupcakes\n3. Bake Cookies\n4. Bake a Cake\n5. Bake a Pie\n6. Bake some Bread\n7. Dan\n8.Deliver Food/n Choose an option (1-8): ")
  if options == "1":
    bake_muffins()

  elif options == "2":
    bake_cupcakes()

  elif options == "3":
    bake_cookies()

  elif options == "4":
    bake_cake()

  elif options == "5":
    bake_pie()

  elif options == "6":
    bake_bread()

  elif options == "7":
    dan()

  elif options == "8":
    deliver_food()

  else:
    slow_print("Invalid option. Please choose a number between 1 and 8.")
    start_of_game()

def bake_muffins():
  start_of_game()

def bake_cupcakes():
  start_of_game()

def bake_cookies():
  start_of_game()

def bake_cake():
  start_of_game()

def bake_pie():
  start_of_game()

def bake_bread():
  start_of_game()

def dan():
  start_of_game

def deliver_food():
  start_of_game

start_of_game()