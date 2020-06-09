import random 
  
# Print rules of this game
# performing concatenation of string 
print(
    "\nRules of the Rock paper scissorss game are:- \n"
                                +  "Rock vs paper -> paper wins \n"
                                +  "Rock vs scissorss -> Rock wins \n"
                                +  "paper vs scissorss -> scissorss wins \n"
) 
  
while True: 
    print("Choose a number : \n 1 for Rock \n 2 for paper \n 3 for scissorss \n") 
      
    # taking input from player
    number = int(input("Your turn: \n")) 
      
    # looping until user enter invalid input 
    while number > 3 or number < 1: 
        number = int(input("Please,enter valid input: ")) 


    if number == 1: 
        number_name = 'Rock'
    elif number == 2: 
        number_name = 'paper'
    else: 
        number_name = 'scissors'
          
    #printing user number  
    print("\nHere's your choice " + number_name) 
    print("\n Now its my turn :) ") 
  
    #chooses randomly any number  
    random_num = random.randint(1, 3) 
       
    while random_num == number: 
        random_num = random.randint(1, 3) 
  
    if random_num == 1: 
        random_num_name = 'Rock'
    elif random_num == 2: 
        random_num_name = 'paper'
    else: 
        random_num_name = 'scissors'
          
    print("\nAnd I choose " + random_num_name) 
  
    print(number_name + " V/s " + random_num_name) 
  
    # condition for win
    if((number == 1 and random_num == 2) or
      (number == 2 and random_num ==1 )): 
        print("paper covers rock\n", end = "") 
        outcome = "paper"
          
    elif((number == 1 and random_num == 3) or
        (number == 3 and random_num == 1)): 
        print("Rock smashes scissors\n ", end = "") 
        outcome = "Rock"
    else: 
        print("scissors cut paper \n", end = "") 
        outcome = "scissors"
  
    #announcing winner
    if outcome == number_name: 
        print("\n You win! \n") 
    else: 
        print("\n You lose! Try again") 
          
    print("Would you like to play again? (Y/N)") 
    answer = input() 
  
    # if condition is True loop breaks
    if answer == 'n' or answer == 'N': 
        break
      
print("  \n*****Thanks for playing***** \n  "
            + "  Hope you enjoyed!\n  ")  
