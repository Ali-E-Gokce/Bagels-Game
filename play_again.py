def play_again():

  while True:
    again=input("Do you want to play again? Type \"yes\" if you do. Type anything else to exit.") 
    if again.lower()=="yes": #plays game again if input is yes, exits program if not. 
      bagels_game()
      continue 
    else:
      print ("Good game! See you again!") 
      break 

#uncomment following lines to play  
#bagels_game()

#play_again()
