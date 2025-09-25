# 🎯 **Scrabble Game**
# In the Scrabble game, each letter brings a certain number of points. 
# The total cost of a word is the sum of the points of its letters. 
# The rarer a letter occurs, the more it is valued:
# 
# Points | Letter
# 1      | A, E, I, L, N, O, R, S, T, U
# 2      | D, G
# 3      | B, C, M, P
# 4      | F, H, V, W, Y
# 5      | K
# 8      | J, X
# 10     | Q, Z
# 
# Write a program to calculate the total cost of the entered word.
# 
# **Input Format**
# The program receives one word in uppercase in English.
# 
# **Output Format** 
# The program should output the total cost of the letters of the entered word.


# Test ___________________________________________

scrabble = {
    1: "AEILNORSTU",
    2: "DG",   
    3: "BCMP", 
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "OZ"
}
score = 0
word = input()

for i in word:
    for k, v in scrabble.items():
        if i in v:
            score += k
            break
print(score)