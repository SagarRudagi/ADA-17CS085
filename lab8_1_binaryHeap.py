arr = list(map(int,input().split()))
for i in range(len(arr)//2):
	if arr[i]<arr[2*i] and arr[i] < arr[2*i + 1]:
		print("False")
		break
else:
	print("True")