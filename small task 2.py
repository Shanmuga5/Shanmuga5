mind = 5
match_not_found = True
while match_not_found ==True:
  guess = int(input("enter a value between 1 and 10"))
  if guess== mind:
      print ("your guess is correct")
      match_not_found = False
  elif guess > mind:
      print ("your guess is higher")
  elif guess < mind:
     print ("your guess is low")
    
