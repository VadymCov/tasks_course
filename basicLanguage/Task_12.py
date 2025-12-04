# Rock, Paper, Scissors, Lizard, Spock 
# After losing 10 times to Player_two, Player_one decided to make the game more complex.
# Help them fairly determine who will build the next module in the new course.
# Input: two strings — Player_two's choice and Player_one's choice.
# Each string is one of: "rock", "paper", "scissors", "lizard", "Spock".


variation = ["rock", "scissors", "paper",  "lizard", "spock"]
outcomes = ["tie", "player_one", "player_two", "player_one", "player_two"]

player_one = input()
player_two = input()

p1 = variation.index(player_one)
p2 = variation.index(player_two)

winner_comb = (p1 - p2) % len(variation)
print(outcomes[winner_comb])