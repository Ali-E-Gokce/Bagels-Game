def generate(number_length):
  import random
  first = random.randint(1,9) #the first digit can't be zero, but the rest can
  second_list = random.sample((set(range(1,10)))-{first},int(number_length)-1)
  second = "".join(str(x) for x in (second_list))
  return (str(first) + second)

def check_fermi(comp,user):
  comp=str(comp)
  user=str(user)
  for i in range(len(comp)):
    if comp[i]==user[i]:
      print ("fermi")
  
def check_pico(comp,user):
  comp=list(str(comp))
  user=list(str(user))
  
  for i in (user):
    if i in comp and comp[user.index(i)]!=i:
      print ("pico")

def check_valid(user,number_length): #checks if user_guess is a valid guess 
    a = len(user)
    b = len(set(user))
    if user[0] == 0 or len(user) != int(number_length) or a != b:
      return False
    else:
      return True
    
def play_again():
  again=input("Do you want to play again? Type \"yes\" if you do. Type anything else to exit.")
  if again.lower()=="yes":
    bagels_game()
  else:
    print ("Good game! See you again!")
def check_bagels(comp,user):
  counter=0
  for i in (str(user)):
    if i not in str(comp):
      counter+=1
  if counter == len(str(user)):
    print ("bagels")

def bagels_game():
  number_length=input("How long do you want the number to be?")
  comp = generate(number_length) 
  print (comp)
  number_of_guesses = 0
  user = (input("What number do you want to guess?"))
  while check_valid(user,number_length) == False:
    user=(input("What number do you want to guess? The leading digit can't be zero, it needs to be "+ str(number_length) + " digits long and there can be no repeating digits"))
  while int(user) != int(comp):
    check_bagels(comp,user)
    check_pico(comp,user)
    check_fermi(comp,user)
    user = int(input("What number do you want to guess?"))
    number_of_guesses+=1
  if number_of_guesses == 1:
    print ("congrat you got in on the first try")
  else:
   print ("the guess was", comp, "you got it in", number_of_guesses, "tries!!!")
  play_again()
