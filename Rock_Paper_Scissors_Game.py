import random

#Writing for Beauty:
print("=== Rock Paper Scissors Game === ")
name = input(("The User Playing Please Enter Your Name: "))

#variable to store number of rounds to be Played;
no_of_rounds = int(input("Enter The Number of Rounds You Wanna play: "))
print()

#Creating a variable i to compare with no of rounds for the loop condition:
i=0

#A list for Computers Choice:
compchoicelist = ["Rock", "Paper", "Scissors"]

#Ditionary For Scores:
scores = {"player_pts" : 0,
          "computer_pts" : 0,
          "ties" : 0
          }



#Function For Players Choice:
def get_player_choice(name):
    print(f"{name} Select Your Choice From These Options\n-Rock \n-Paper\n-Scissors")
    playerchoice = input("Choice:")

    print(f"You Have Chosen: {playerchoice}")
    if(playerchoice == "Rock"):
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif(playerchoice == "Paper"):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print("------------------------------")

    return playerchoice



#Function For Computers Choice:
def get_computer_choice(compchoicelist):
    num = random.randint(0,2)
    print(f"The Computer Has Chosen: {compchoicelist[num]}")
     
    if(num== 0):
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif(num == 1):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print("------------------------------")

    return num


#Function to Determine The Winner and Update The Score:
def determine_winner(playerchoice, num, compchoicelist, name,scores):
    if(playerchoice == "Rock" and compchoicelist[num] == "Rock"):
        print("Tie!")
        scores["ties"] += 1
    
    elif(playerchoice == "Rock" and compchoicelist[num] == "Paper"):
        print("Computer Wins!")
        scores["computer_pts"] +=1
        

    
    elif(playerchoice == "Rock" and compchoicelist[num] == "Scissors"):
        print(f"{name} Wins!")
        scores["player_pts"] +=1
        


    if(playerchoice == "Paper" and compchoicelist[num] == "Rock"):
        print(f"{name} Wins!")
        scores["player_pts"] +=1
        

    elif(playerchoice == "Paper" and compchoicelist[num] == "Paper"):
        print("Tie!")
        scores["ties"] += 1
       

    elif(playerchoice == "Paper" and compchoicelist[num] == "Scissors"):
       print("Computer Wins!")
       scores["computer_pts"] +=1
       



    if(playerchoice == "Scissors" and compchoicelist[num] == "Rock"):
        print("Computer Wins!")
        scores["computer_pts"] +=1
       

    elif(playerchoice == "Scissors" and compchoicelist[num] == "Paper"):
        print(f"{name} Wins!")
        scores["player_pts"] +=1
        

    elif(playerchoice == "Scissors" and compchoicelist[num] == "Scissors"):
       print("Tie!")
       scores["ties"] += 1

    print("------------------------------")
       
  
#Function To Display The Score:
def display_score(scores, name):
    print(f"{name} Points: {scores["player_pts"]}")
    print(f"Computer Points: {scores["computer_pts"]}")
    print(f"Ties: {scores["ties"]}")
    print()

    if(scores["player_pts"] > scores["computer_pts"]):
        print(f"=== {name.upper()} WINS!!!!! ===")

    elif(scores["player_pts"] < scores["computer_pts"]):
        print(f"=== COMPUTER WINS!!!!! ===")
    
    else:
        print("ITS A TIE !!!!!")
    
    
        
while(i < no_of_rounds):
    print(f"Round: {i+1}")
    playerchoice = get_player_choice(name)
    print()
    num = get_computer_choice(compchoicelist)
    print()
    determine_winner(playerchoice, num,  compchoicelist, name,scores)
    print()
    i += 1




score_count = display_score(scores, name)
print()
