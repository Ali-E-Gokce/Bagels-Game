def generate(number_length): #generates random number that fits bagel rules
  import random
  first = random.randint(1,9) #the first digit can't be zero, but the rest can
  second_list = random.sample((set(range(1,10)))-{first},number_length-1) #to make sure the other two numbers are not the same as the first

  
  number=first*(10**(number_length-1)) #uses algebra to generate integer instead of string

  for i in range(len(second_list)):
    number+=second_list[i]*(10**(number_length-i-2))

  return number
