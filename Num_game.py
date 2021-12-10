'''import random
no_of_stone = random.randrange(50)
count = 1
player = 'player1'
print("They have ",no_of_stone,"stone in Game!!")
while no_of_stone > 0:
    if count%2 == 0:
        player = 'Player2'
    else:
        player = 'Player1'
    user_input = int(input(player+" can remove '1' or '2' stone :: "))
    while user_input != 1 and user_input != 2:
        user_input = int(input("Your Choose '1' or '2' stone :: "))
    no_of_stone -= user_input
    print("There are",no_of_stone,"in left!")
    count += 1
if player == 'player1':
    player = 'Player1'
else:
    player = 'Player2'
print(player," is Winner!!!!!!")'''

import random
no_of_stone = random.randrange(50)
count = 1
player = pl_1 = input("Enter Ingame Name Player1 :: ")
player = pl_2 = input("Enter Ingame Name Player2 :: ")
print("***********************************")
print("There are ",no_of_stone,"in game.")
while no_of_stone > 0 :
    if count%2 == 0:
        player = pl_2
    else:
        player = pl_1
    user_input = int(input(player+", would you like to remove '1' or '2' stone :: "))
    while user_input != 1 and user_input != 2:
        user_input = int(input("Your Choose '1' or '2' stone! :: "))
    no_of_stone -= user_input
    print("There are ",no_of_stone,"is left!")
    count +=1 

if player == pl_1:
    player = pl_2

else:
    player = pl_2

print(player,"is Winner !!!!")