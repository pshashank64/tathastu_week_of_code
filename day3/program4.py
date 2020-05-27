def duplicate(List):
 duplist = []
 for i in List:
  if i not in duplist:
   duplist.append(i)
 return duplist
 
size = int(input("ENter the no. of items in the list"))
print("Enter the elements of list: ")
List = []
for x in range(size):
 List.append(input())
print("New list is: ", duplicate(List))
