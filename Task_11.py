# Rock, Paper, Scissors
# player_one and player_two are deciding how to divide the workload for the course "Python for Professionals."
# To do this, they decided to play Rock, Paper, Scissors to make a fair decision
# and determine who will work on the next module of the course.
#
# Input format:
# The program receives two lines of text containing the words "rock", "paper", or "scissors".
# The first line contains the choice of player_one, and the second line contains the choice of player_two.


player_one = input()
player_two = input()


if player_one[0] == player_two[0]:
    print("draw")

elif player_one[0] == "p" and player_two[0] == "r":
    print("player_one")

elif player_one[0] == "r" and player_two[0] == "s":
    print("player_one")

elif player_one[0] == "s" and player_two[0] == "p":
    print(player_one)

else:
    print("player_two")