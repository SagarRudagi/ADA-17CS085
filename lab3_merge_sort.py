def merge_sort(arr):
	global count
	if len(arr)>1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		merge_sort(L)
		merge_sort(R)

		i=j=k=0
		
		while i<len(L) and j<len(R):
			if L[i]<R[j]:
				count+=1
				arr[k]=L[i]
				k=k+1
				i=i+1
			else:
				count+=1
				arr[k]=R[j]
				k=k+1
				j=j+1

		while j<len(R):
			arr[k]=R[j]
			k=k+1
			j=j+1


		while i<len(L):
			arr[k]=L[i]
			k=k+1
			i=i+1




# 9 4 0 3 7 1 6 2 5 8
arr = [9,4,0,3,7,1,6,2,5,8]
count=0
merge_sort(arr)
print(arr)
print(count)