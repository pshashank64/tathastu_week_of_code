size = int(input("Enter the size of the tuple: "))
arr = []
print("Enter the elements: ")
for i in range(size):
 arr.append(input())
arr = tuple(arr)
member = input("ENter the element whose occurrence you want: ")
print("Tuple contains ", member, arr.count(member), "times")
