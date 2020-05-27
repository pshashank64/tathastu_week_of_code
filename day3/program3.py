def dupstring(str1):
 dstr = ""
 for i in str1:
  if i not in dstr:
   dstr = dstr+i
 return dstr
 
str1 = input("Enter a string: ")
print(dupstring(str1))
