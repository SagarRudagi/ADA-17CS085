def quick_sort(arr,low,high):
	if low<high:
		pivot_pos = partition(arr,low,high)
		quick_sort(arr,low,pivot_pos-1)
		quick_sort(arr,pivot_pos+1,high)

def partition(arr,low,high):
	pivot = arr[low]
	i = low + 1
	j = high
	while True:
		while i<=high and arr[i]<=pivot:
			i = i+1	
		while j>=low and arr[j]>pivot:
			j = j-1
		if i<j:
			arr[i],arr[j] = arr[j],arr[i]
		else:
			arr[low],arr[j]=arr[j],arr[low]
			return j

arr = list(map(int,input().split()))
quick_sort(arr,0,len(arr)-1)
print(arr)
