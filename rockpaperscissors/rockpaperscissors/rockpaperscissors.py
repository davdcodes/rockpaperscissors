import random

print("-------------------------------------------------------------------------------")
print("Let's play Rock Paper Scissors!")
print()

scores = [0,0]
replay = "a"

def printchoice(ch1, ch2):
        if ch1 == "r":
            userans = "Rock"
        elif ch1 == "p":
            userans = "Paper"
        else:
            userans = "Scissors"

        if ch2 == "r":
            comans = "Rock"
        elif ch2 == "p":
            comans = "Paper"
        else:
            comans = "Scissors"

        print("So I picked " + comans + ", and you picked " + userans + "...")


while replay != "q":
    user = input("You pick your option with either 'r' for Rock, 'p' for Paper, or 's' for Scissors! ")
    com = random.choice(["r", "p", "s"])
    print()

    printchoice(user, com)
    if (user == com):
        print("It's a tie!")
    elif (user == "r" and com == "s") or (user == "s" and com == "p") or (user == "p" and com == "r"):
        print("You Win!")
        scores[1] += 1
    else:
        print("I Win!")
        scores[0] += 1

    print()
    print("The score is now " + str(scores[0]) + "-" + str(scores[1]) + "!")

    print()
    replay = input("Wanna play again? Enter any key to continue, or 'q' to quit! ")
    print("-------------------------------------------------------------------------------")

print()
print("Oh, we're done? Thanks for playing then!")