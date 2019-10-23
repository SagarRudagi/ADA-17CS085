import math
k = int(input())
arr = []
for i in range(k):
    eleList = list(map(int,input().split()))
    arr.append(eleList)
ptr = [0]*k
n = len(arr[0])

def findSmallestRange(arr, n, k):  
    i, minrange, minel, maxel, flag, minind = 0, math.inf, 0, 0, 0, 0 

    while(1):     
        minind = -1
        minval = 10**9
        maxval = -10**9
        flag = 0

        for i in range(k): 
            if(ptr[i] == n): 
                flag = 1    
                break
 
            if(ptr[i] < n and arr[i][ptr[i]] < minval): 
                minind = i 
                minval = arr[i][ptr[i]] 
 
            if(ptr[i] < n and arr[i][ptr[i]] > maxval): 
                maxval = arr[i][ptr[i]] 
              
        if(flag): 
            break
  
        ptr[minind] += 1
  
        if((maxval-minval) < minrange): 
            minel = minval 
            maxel = maxval 
            minrange = maxel - minel 
      
    print([minel, maxel]) 

findSmallestRange(arr,n,k)
