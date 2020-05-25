rp1 = int(input("Enter the runs scored by player 1 in 60 balls: "))
rp2 = int(input("Enter the runs scored by player 2 in 60 balls: "))
rp3 = int(input("Enter the runs scored by player 3 in 60 balls: "))
sr1 = rp1 * 100 / 60
sr2 = rp2 * 100 / 60
sr3 = rp3 * 100 / 60
print("Strike rate of player 1 is", sr1)
print("Strike rate of player 2 is", sr2)
print("Strike rate of player 3 is", sr3)
print("Runs scored by player 1 if they played 60 more balls is", rp1 * 2)
print("Runs scored by player 2 if they played 60 more balls is", rp2 * 2)
print("Runs scored by player 3 if they played 60 more balls is", rp3 * 2)
print("Maximum number of sixes player 1 could hit =", rp1 // 6)
print("Maximum number of sixes player 2 could hit =", rp2 // 6)
print("Maximum number of sixes player 3 could hit =", rp3 // 6)
