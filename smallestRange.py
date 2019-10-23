import math
k = int(input())
for i in range(k):
    eleList = list(map(int,input().split()))
    arr = []
    arr.append(eleList)
ptr = [0]*k
n = len(arr[0])

def findSmallestRange(arr, n, k):  
    i, minval, maxval, minrange, minel, maxel, flag, minind = 0, -math.inf, math.inf, math.inf + math.inf, 0, 0, 0, 0 
    while(1):     
        minind = -1
        # minval = 10**9
        # maxval = -10**9
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
      
    print("The smallest range is [", minel, maxel,"]") 