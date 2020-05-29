def replaceint(num):
 return int(str(num).replace("0","5"))
num = int(input("Enter a number: "))
print("The new number is: ", replaceint(num))
