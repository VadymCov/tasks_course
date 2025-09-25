# 🧬 **Genetics Minute**
# As known from biology course, DNA and RNA are sequences of nucleotides.
# Four nucleotides in DNA:
# * adenine (A);
# * cytosine (C);
# * guanine (G);
# * thymine (T).
# 
# Four nucleotides in RNA:
# * adenine (A);
# * cytosine (C);
# * guanine (G);
# * uracil (U).
# 
# RNA chain is built based on DNA chain by sequential attachment of complementary nucleotides:
# * G → C;
# * C → G;
# * T → A;
# * A → U.
# 
# Write a program that translates a DNA chain into an RNA chain.

# Test ____________________________________________________________

my_dict = dict([('G', 'C'),('C', 'G'),('T', 'A'),('A', 'U')])
dna = input().upper()

for i in dna:
    if i in my_dict:
        print(my_dict[i], end=(""))