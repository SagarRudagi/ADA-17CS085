arr = list(map(int,input().split()))
key = int(input())

def findPivot(arr,low,high,key=key):
	while low<=high:
		mid=int((low+high)/2)
		if(arr[mid]<arr[mid-1]):
			pivot = mid
			if(key>=arr[low]):
				index=bin_srch(arr,low,mid)
				print(index)
			else:
				index=bin_srch(arr,mid,high)
				print(index)
			break
		elif arr[mid]>arr[mid-1]:
			findPivot(arr,mid+1,high)
		else:
			findPivot(arr,low,mid-1)


def bin_srch(arr,low,high,key=key):
	while low<=high:
		mid=int((low+high)/2)
		if arr[mid]==key:
			return mid
		elif key>arr[mid]:
			low = mid+1
		else:
			high = mid-1



findPivot(arr,0,len(arr)-1)
