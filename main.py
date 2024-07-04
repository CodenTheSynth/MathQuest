import modules.colors as color
import os
import random

def game():
  Level = 1
  Score = 0
  Sublevel = 1
  Max = 3
  health = 3
  lost = False
  while not lost:
    a = 0
    b = 0
    while not a > b:
     a = float(random.randint(1, Max))
     b = float(random.randint(1, Max))
    sign_choice = random.randint(1, 4)  # Determine sign once
    sign = None
    if sign_choice == 1:
      sign = "+"
    elif sign_choice == 2:
      sign = "-"
    elif sign_choice == 3:
      sign = "*"
    else:
      sign = "/"

    os.system("clear")
    disa = int(a)
    disb = int(b)
    print("{} {} {}".format(disa, sign, disb))
    print(color.GREEN + (Sublevel * "#"), end=color.RESET)
    print(color.RED + ((10 - Sublevel) * "#"), end=" ")
    print(color.RESET + "L:{} ".format(Level) + color.MAGENTA + (health * "♡") + color.RESET)
    print("Score: {}".format(Score))

    try:
      ans = float(input("Answer: "))
    except ValueError:
      lost = True
      break

    if sign == "+" and a + b == ans:
      Sublevel += 1
      Score += Level * 100
    elif sign == "-" and a - b == ans:
      Sublevel += 1
      Score += Level * 100
    elif sign == "*" and a * b == ans:
      Sublevel += 1
      Score += Level * 100
    elif sign == "/" and round(a / b)   == ans:
      Sublevel += 1
      Score += Level * 100
    else:
      health -= 1
      if health <= 0:
        lost = True
      Sublevel += 1

    if Sublevel == 10:
        Level += 1
        Sublevel = 1
        Max += 1
        if random.randint(1, 3) == 2:
          health += 1

  os.system("clear")
  print(color.RED + "GAME OVER! ")
  print("---------")
  print(color.RESET + "Score: {}".format(Score))
  print("Level: {}".format(Level))
  print(color.YELLOW + "Press Anything.. ")
  print(color.RESET)
  input()
  os.system("clear")
  store_score(Score)
  show_leaderboard()
  print(color.YELLOW + "Press Anything.. ")
  print(color.RESET)
  input()
  os.system("clear")
  diffi()

print(color.BLUE + "-----+-----" + color.RESET)
print("Math Quest!")
print(color.BLUE + "-----+-----" + color.RESET)
print("Welcome to Math Quest! ")
print(color.YELLOW + "Type in anything to continue. " + color.RESET)
print()
input()
os.system("clear")

def store_score(score):
  with open("leaderboard.txt", "a") as f:
    f.write(f"{score}\n")
    
def show_leaderboard():
  print(color.BLUE + "-----+-----" + color.RESET)
  print("LEADERBOARD")
  print(color.BLUE + "-----+-----" + color.RESET)
  with open("leaderboard.txt", "r") as f:
    scores = f.readlines()
    scores = [int(score.strip()) for score in scores]
    scores.sort(reverse=True)
    for i, score in enumerate(scores[:5]):
      print(f"{i+1}. {score}")
  
def diffi():
  print(color.BLUE + "-----+-----" + color.RESET)
  print("DIFFICULTY")
  print("1. Easy")
  print("2. Medium")
  print("3. Hard")
  print(color.BLUE + "-----+-----" + color.RESET)
  global diff
  diff = 0
  while (diff > 0) == False and (diff < 4):
    try:
      diff = int(input("Choose a difficulty: "))
    except ValueError:
      print("Invalid input! Please enter a number between 1 and 3.")
      continue
    if diff == None:
      diffi()
      break
  game()

if not os.path.exists("leaderboard.txt"):
  with open("leaderboard.txt", "w"):
    pass
diffi()