arr = []
n = int(input("Enter the number of elements : "))
print("Enter the digits :")

for i in range(n):
	arr.append(int(input()))

print("Maximum of the array : ",max(arr))
