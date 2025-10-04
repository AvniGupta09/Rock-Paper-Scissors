import random

def game_fun():
    usr_scr = 0
    comptr_scr = 0
    tie = 0

    Rnds = int(input("Enter number of rounds you want to play: "))

    choices = ["rock", "paper", "scissors"]

    # for i in range(0,Rnds):
    #     usr_input = input("Enter your choice: Rock/Paper/Scissors: ").lower()
    #     if usr_input not in choices:
    #         print("Invalid input! Please enter Rock, Paper, or Scissors.")
    #         Rnds=Rnds-1
    #         continue

    i=0 
    while i<Rnds: 
        usr_input=input("Enter your choice: Rock/Paper/Scissors: ").lower() 
        if usr_input not in ["rock", "paper", "scissors"]: 
            print("Invalid input! Please enter Rock, Paper, or Scissors.") 
            continue
        i+=1
        comptr_choice = random.choice(choices)
        print(f"You chose {usr_input}. Computer chose {comptr_choice}.")

        if usr_input == comptr_choice:
            print("It's a tie!")
            tie += 1
        elif ((usr_input == "rock" and comptr_choice == "scissors") or 
             (usr_input == "paper" and comptr_choice == "rock") or 
             (usr_input == "scissors" and comptr_choice == "paper")):
            print("You Win this round!")
            usr_scr += 1
        else:
            print("Computer Wins this round!")
            comptr_scr += 1

    print(f"\nThanks for playing the game! \n"
          f"Final Score:\n"
          f"Computer: {comptr_scr}\n"
          f"You: {usr_scr}\n"
          f"Ties: {tie}\n")


game_fun()
strt_input = input("Do you want to start another game? Yes or No: ").lower()
while strt_input=="yes": 
    game_fun()
    strt_input = input("Do you want to start another game? Yes or No: ").lower()
print("Thank You for playing!")
