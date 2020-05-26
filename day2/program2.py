num = int(input("Enter the number till which you want the fibnacci series to be printed: "))
n1, n2 = 0, 1
count = 0
if num<0:
 print("Enter a +ve number")
elif num == 1:
 print(n1,n2, sep=' ')
else:
 while count < num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
