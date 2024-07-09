

def number_to_words(n):
  units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  if n==1000:
           return "onethousand"

  words  = ""

  if n>100:
          words+=units[n//100] + "hundred"
          if n%100!=0:
                  words+="and"

  if n%100<20:
          words+=units[n%100]
  else:
          words+=tens[(n%100)//10]
          words+=units[(n%100)%10]

  return words

def count_letters_in_numbers(limit):
  total_letters = 0
  for i in range(1,limit+1):
    words = number_to_words(i)
    total_letters+=len(words)
  return total_letters

result = count_letters_in_numbers(1000)
print("Total Letters used from 1 to 1000:",result)
