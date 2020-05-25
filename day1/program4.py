cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling: "))
profit = sp - cp
newsp = 1.05 * profit + cp
print("The profit is", profit)
print("new selling price to increase profit by 5% is: ", newsp)
