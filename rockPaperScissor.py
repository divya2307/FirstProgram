def compare(p1,p2):
    if p1.lower() == p2.lower():
        print("Its a Tie")

    elif p1.lower() == "scissor" and p2.lower() == "paper":
        print("Player 1 Wins")

    elif p1.lower() == "rock" and p2.lower() == "scissor":
        print("Player 1 Wins")

    elif p1.lower() == "paper" and p2.lower() == "rock":
        print("Player 1 Wins")

    else:
        print("Player 2 Wins")


def main():

    i='Yes'

    while i.lower() =='yes':
        p1 = input("Player 1 Please Enter the input (either Rock , Paper or Scissor):")
        p2 = input("Player 2 Please Enter the input (either Rock , Paper or Scissor):")

        if p1.lower()not in ("rock", "paper","scissor" )or p2.lower() not in("rock" ,"paper","scissor"):
            print("Please Enter the valid input")
            i = 'yes'
            continue


        compare(p1,p2)

        i = input("Do you want to continue (Yes/No)")
        if i.lower()=="no":
            break
        else:
            continue

main()