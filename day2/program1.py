def iseven(x):
 if x%2==0:
  return True
 return False

def isprime(x):
 if x<=1:
  return False
 for i in range(2,x):
  if i%x==0:
   return False
  return True

def palindrome(x):
 rev = 0
 tem = x
 while tem>0:
  digit = tem%10
  rev = rev * 10 + digit
  tem //= 10
 if rev == x:
  return True
 return False


def isarmstrong(x):
 sum = 0
 temp = x
 while temp>0:
  digit = temp % 10
  sum += digit ** 3
  temp //= 10
 if x==sum:
  return True
 return False

def verify():
 num = int(input("Enter the number to check whether the number is odd/even, prime, palindrome, armstrong: "))
 if(iseven(num)):
   print("It is even")
 else:
  print("It is odd")
 
 if(isprime(num)):
  print("It is not prime")
 else:
  print("It is prime")
 
 if(palindrome(num)):
  print("It is palindrome")
 else:
  print("It is not palindrome")
  
 if(isarmstrong(num)):
  print("It is an armstrong number")
 else:
  print("It is not an armstrong number")

verify()
