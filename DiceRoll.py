#DiceRoll.py
#Name:Bennett Schulte
#Date:10/4/2025
#Assignment:Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for i in range(10000):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
  

  #find the sum total of the two dice
    total = die1 +die2
    rolls[total - 1] += 1
  #print statictics for dice rolls
  print("Total\tCount\tPercent")
  for total in range(2,13):
    count = rolls[total - 1]
    percent = (count / 10000) * 100
    print(f"{total}\t{count}\t{percent:.2f}%")



if __name__ == '__main__':
  main()
