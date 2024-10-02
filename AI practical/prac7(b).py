import itertools, random

dec = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Daimond', 'Club']))
random.shuffle(dec)
print("you got: ")
for i in range(7):
    print(dec[i][0], "of", dec[i][1])