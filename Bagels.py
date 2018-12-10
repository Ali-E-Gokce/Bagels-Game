def check_valid(guess,number_length): #checks if user_guess is a valid guess, number can start with o and the guess has to be of the same length as the number. Returns initial guess if guess fits in the rules

    while True:
      a = len(str((guess)))
      b = len(set((guess)))
    
      if int(guess[0]) == 0 or len(guess) != int(number_length) or a!=b:#the last condition checks if there are repeating numbers:
        guess=input("What number do you want to guess? The leading digit can't be zero, it needs to be"+ " " + str(number_length) +" digits" + "long and there can be no repeating digits")
        continue
      else:
        break
    
    return guess

    
def play_again(): #asks the player if they want to play agian
  again=input("Do you want to play again? Type \"yes\" if you do. Type anything else to exit.")
  if again.lower()=="yes":
    bagels_game()
  else:
    print ("Good game! See you again!")
      
def generate(number_length): #generates random number that fits bagel rules
  import random
  first = random.randint(1,9) #the first digit can't be zero, but the rest can
  second_list = random.sample((set(range(1,10)))-{first},number_length-1) #to make sure the other two numbers are not the same as the first

  
  

  second = "".join(str(x) for x in (second_list))
  return (str(first) + second) #this is inefficient because it does a few unecessary type conversions, but since the number will always be very small, I will leave it like this for readability. If you want to increase performance marginally you can convert from the list straight to an integer using simple algebra and a for loop.

  


def bagels_game():

  number_length=input("How long do you want the number to be?")

  number = generate(int(number_length)) #the conversion is done outside of the input for backwards compatibality with raw_input

  user_guess = input("What number do you want to guess?")


  user_guess=check_valid(user_guess,number_length)
    
    
  number_of_guesses = 1

  while int(user_guess) != int(number):

    pico=False
    fermi=False

    #checks if any of the numbers are in the right place
    for i in range (len(number)):
     if user_guess[i] == number[i]:
      print ("Fermi!")
      fermi=True


    #checks if number is correct, but in the wrong index
    position=0
    for i in user_guess: 
      if i in number and user_guess[position] != number[position]:
        print("Pico!")
        pico=True
      position += 1

    
    if not (pico or fermi): #if neither of them has been printed before
      print("Bagel!")

    number_of_guesses += 1
    user_guess = input("What number do you want to guess?")
    user_guess=check_valid(user_guess,number_length)
    
  if number_of_guesses == 1:
    print ("congrat you got in on the first try")
  else:
   print ("the guess was", number, "you got it in", number_of_guesses, "tries!!!")
  play_again() #this could technically be an issue if the user plays more times than the recursion limit of their system. For readability I will leave it like this, but if it is an issue, you can make a while-loop in the play_again function, similiar to the check_valid function and call it manually after the bagels_game() call that starts the game.
  

#uncomment following line to play:
#bagels_game()
