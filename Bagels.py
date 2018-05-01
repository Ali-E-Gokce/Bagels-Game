def check_valid(guess,number_length): #checks if user_guess is a valid guess 
    a = len(str((guess)))
    b = len(set((guess)))
    if guess[0] == 0 or len(guess) != number_length or a != b: #sees if the number has repeating digits
      return False
    else:
      return True
    
def play_again(): #аsks the user if she wants to play again
  again=input("Do you want to play again? Type \"yes\" if you do. Type anything else to exit.")
  if again.lower()=="yes":
    bagels_game()
  else:
    print ("Good game! See you again!")
      
def generate(number_length): #generates a number that does not have repeating digits and does not lead with a zero
  import random
  first = random.randint(1,9) #the first digit can't be zero, but the rest can
  second_list = random.sample((set(range(1,10)))-{first},number_length-1)
  second = "".join(str(x) for x in (second_list))
  return (str(first) + second)


def bagels_game(): #This is the game.

  number_length=int(input("How long do you want the number to be?"))
  number = generate(number_length) 
  #print (number) you can remove the coment and leave the 'print number' to see the number you are trying to guess. You can test out the code or gain a better understanding of the game.
  user_guess = (input("What number do you want to guess?"))
  while check_valid(user_guess,number_length) == False: #makes sure the guess abides with the rules
    user_guess=(input("What number do you want to guess? The leading digit can't be zero, it needs to be,"+ str(number_length) + "long and there can be no repeating digits"))
    
  number_of_guesses = 1

  while int(user_guess) != int(number):
    counter = 0

    for i in range (len(number)):
     if user_guess[i] == number[i]:
      print ("Fermi!")
    position = 0
    counter = 0 
    
    for i in user_guess:
      if i in number and user_guess[position] != (number[position]):
        counter += 1
      position += 1
    while counter > 0:
      print ("Pico")
      counter = counter - 1 
    
    counter = 0
    for i in user_guess:
      if i not in (number):
        counter += 1
    if counter == number_length:
      print ("Bagel!")
    number_of_guesses += 1
    user_guess = input("What number do you want to guess?")
    
  if number_of_guesses == 1:
    print ("congrat you got in on the first try")
  else:
   print ("the guess was", number, "you got it in", number_of_guesses, "tries!!!")
  play_again() #asks the user if she wants to play again
