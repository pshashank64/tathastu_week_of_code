def tostring(List):
 return ''.join(List)

def permutation(a, l, r):
 if l==r:
  print(tostring(a))
 else:
  for i in range(l, r+1):
   a[l], a[i] = a[i], a[l]
   permutation(a, l+1, r)
   a[l], a[i] = a[i], a[l]
   
string = input("Enter a string: ")
n = len(string)
a = list(string) 
permutation(a, 0, n-1) 
