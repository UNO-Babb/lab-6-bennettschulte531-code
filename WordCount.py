#WordCount.py
#Name:Bennett Schulte
#Date:10/4/2025
#Assignment:Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')

  lineCount = 0
  wordCount = 0
  charCount = 0
  
  for line in textFile:
   
    lineCount += 1
    wordCount += len(line.split())
    charCount += len(line)

  textFile.close()

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", charCount)
  

if __name__ == '__main__':
  main()
