# Rock, Paper, Scissors
# player_one and player_two are deciding how to divide the workload for the course "Python for Professionals."
# To do this, they decided to play Rock, Paper, Scissors to make a fair decision
# and determine who will work on the next module of the course.
#
# Input format:
# The program receives two lines of text containing the words "rock", "paper", or "scissors".
# The first line contains the choice of player_one, and the second line contains the choice of player_two.

variation = ["rock", "paper", "scissors"]
outcomes = ["tie", "player_one", "player_two"]

player_one = input()
player_two = input()

p1 = variation.index(player_one)
p2 = variation.index(player_two)

winner_comb = (p1 - p2) % len(variation)
print(outcomes[winner_comb])