import re
def decode(message_file):
  #read file and create list of lines from file, separated by commas
  lines = open(message_file).read().splitlines()

  #sort list items by extracting the number from the line, converting it into an integer, and then sorting the list
  lines = sorted(lines, key=lambda s: int(re.search(r'\d+', s).group()))
    
  number = 1
  decode = []
  for i in range(1, 25):
    for j in range(1, i+1):
      if j == i:
        decode.append(lines[number-1])
      number += 1

  noDigit = []
  for x in decode:
    noDigit.append(x.split(" ")[1])

  print(noDigit)

decode('coding_qual_input.txt')
