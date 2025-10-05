#WordIndex.py
#Name:Bennett Schulte
#Date:10/4/2025
#Assignment:Lab 6

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  
  lineNum = 0
  for line in textFile:
    lineNum += 1
    wordList = line.split()
    for word in wordList:
      word = word.strip(",.?!").lower()
      if word in words:
        words[word].append(lineNum)
      else:
        words[word] = [lineNum]


  print ("fish" in words) #is a word already in the dictionary?
  words["fish"] = [2]     #add a list to the dictionary
  print ("fish" in words) #is the word there now?
  words["fish"].append(5) #add to an existing list
  print(words)


if __name__ == '__main__':
  main()
