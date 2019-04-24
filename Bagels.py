import random

def is_int(num):
    try:
        int(num)
    except:
        return False
    return True

#checks if user_guess is a valid guess, number can start with 0
#Returns initial guess if guess is legal
def get_valid_guess(num_length):
    guess =  input("What number do you want to guess?" +
                      " The leading digit can't be zero, it needs to be" + " " +
        str(num_length) + " digits" + " long and can't have repeating digits\n")
    guess_length = len(str(guess))
    #making it a set will show how many unique digits there are
    guess_digits = len(set(guess))
    first_digit =  int(guess[0])
    if not is_int(guess) or  first_digit == 0 or\
    len(guess) != int(num_length) or guess_length != guess_digits:
        #the last condition checks if there are repeating numbers
        return get_valid_guess(num_length)
    return guess

#asks the player if they want to play agian
def play_again():
  again=input("Do you want to play again? Type \"yes\" if you do.\
                                     Type anything else to exit.")
  if again.lower()=="yes":
    bagels_game()
  else:
    print ("Good game! See you again!")

#generates random number that fits bagel rules
def generate_num(num_length):
  #the first digit can't be zero, but the rest can
  first_digit = random.randint(1,9)
  #to make sure the other two numbers are not the same as the first
  available_nums = set(range(1,10))-{first_digit}
  rest_of_digits = random.sample(available_nums, num_length-1)
  rest_of_digits_str = "".join(str(x) for x in (rest_of_digits))
  num = str(first_digit) + rest_of_digits_str
  return num

def get_valid_num_length():
    num_length=input("How long do you want the number to be?")
    if not is_int(num_length) or int(num_length)<1 or int(num_length)>9:
        return get_valid_num_length()
    return int(num_length)

def play_bagels():
  num_length = get_valid_num_length()
  num = generate_num(num_length)
  user_guess = get_valid_guess(num_length)

  num_of_guesses = 1

  while int(user_guess) != int(num):
    pico=False
    fermi=False
    #checks if any of the numbers are in the right place
    for i in range (len(num)):
     if user_guess[i] == num[i]:
      print ("Fermi!")
      fermi=True
    #checks if number is correct, but in the wrong index
    pos=0
    for i in user_guess:
      if i in num and user_guess[pos] != num[pos]:
        print("Pico!")
        pico=True
      pos += 1

    #if neither of them has been printed before
    if not (pico or fermi):
      print("Bagel!")

    num_of_guesses += 1
    user_guess = get_valid_guess(num_length)

  if num_of_guesses == 1:
    print ("congrat you got in on the first try")
  else:
   print ("the guess was", num, "you got it in", num_of_guesses, "tries!")

  play_again()

def play_again():
  while True:
    again=input("Do you want to play again? Type \"yes\" if you do. Type anything else to exit.")
    if again.lower()=="yes":
      play_bagels()
      continue
    else:
      print ("Good game! See you again!")
      break

play_bagels()
