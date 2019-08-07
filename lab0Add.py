"""This python file is associated with lab0Add.txt
The following terminal command is used to execute it
python3 lab0Add.py<lab0Add.txt"""
tc = int(input())
for i in range(tc):
	arr = []
	n,k = map(int, input().split(" "))
	arr.extend(input().split(" "))
	if str(k) in arr:
		print("1")
	else:
		print("-1")
