import random
player1 = input("whats your name?")
player2 = input("whats your name?")
print(""" I will now explain the rules of this fun dice game!
    The points rolled on each player’s dice are added to their score.
If the total is an even number, and additional 10 points are added to their score.
If the total is an odd number, 5 points are subtracted from their score.
The score of a player cannot go below 0 at any point.
The person with the highest score at the end of the 5 rounds wins.
If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).
""")

def dice():
    num = random.randint(1,6)
    #print(num)
    return num
    
player1_total_score = 0
player2_total_score = 0

for i in range(5):
    print(player1, " is now rolling the dice...")
    dice_one = dice()
    dice_two = dice()
    print(player1, "has rolled ", dice_one , " and a" , dice_two)
    player1_score = dice_one + dice_two
    if player1_score % 2 == 0:
        player1_score = player1_score +10
    else:
        player1_score = player1_score - 5

    print(player1_score)
    player1_total_score = player1_total_score + player1_score

    print(player2, " is now rolling the dice...")
    dice_one = dice()
    dice_two = dice()
    print(player2, "has rolled ", dice_one, " and a", dice_two)
    player2_score = dice_one + dice_two
    print(player2_score)
    if player2_score % 2 == 0:
        player2_score = player2_score +10
    else:
       player2_score = player2_score - 5
    print(player2_score)
    player2_total_score = player2_total_score + player2_score
    
print(" player1 has scored ", player1_total_score)
print(" player2 has scored ", player2_total_score)
    
if player1_total_score > player2_total_score:
        print("player1 wins!")
elif player2_total_score > player1_total_score:
        print("player2 wins!")
else:
        print("It's a tie! Rolling 1 die each to determine the winner...")
        while player1_total_score == player2_total_score:
            player1_roll = dice()
            player2_roll = dice()
            print("player1 rolls: {player1_roll}, player2 rolls: {player2_roll}")

            if player1_roll > player2_roll:
                print("player1 wins the tiebreaker!")
                break
            elif player2_roll > player1_roll:
                print("player2 wins the tiebreaker!")
                break

