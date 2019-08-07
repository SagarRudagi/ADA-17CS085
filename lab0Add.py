"""This python file is associated with lab0Add.txt (if does not exist then create it)
The following terminal command is used to execute it
python3 lab0Add.py<lab0Add.txt"""

"""The lab0Add.txt file contains the following content :
2
5 6
1 2 3 4 6
5 2
1 3 4 5 6"""

tc = int(input())
for i in range(tc):
	arr = []
	n,k = map(int, input().split(" "))
	arr.extend(input().split(" "))
	if str(k) in arr:
		print("1")
	else:
		print("-1")
