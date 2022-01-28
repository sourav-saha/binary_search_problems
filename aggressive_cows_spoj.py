'''
https://www.spoj.com/problems/AGGRCOW/
'''

def check_possibility(arr, cows, maxDistance):
  count = 1 
  coord = arr[0]
  for i in range(1, len(arr)):
    if arr[i]-coord >= maxDistance:
      count += 1
      coord = arr[i]
    if count == cows:
      return True 
  
  return False 
	
def binary_search(arr, n, c):
  arr = sorted(arr) #need to sort it as we are calculating difference whihc is different from allocate books
  if n == c:
    return (arr[1]-arr[0])
  #elif c > n:
  #	return -1 
  
  start = 1 
  end = arr[n-1] - arr[0]
  while start <= end:
    mid = (start+end)//2 
    if check_possibility(arr, c, mid):
      ans = mid 
      start = mid+1 #this is also different from allocate books, as we want to get the max no. here 
    else:
      end = mid-1 
  return ans 

if __name__ == "__main__":
	t = int(input().strip())
	for ti in range(t):
		n, c = map(int, input().strip().split(' '))
		arr = []
		for i in range(n):
			num = int(input().strip())
			arr.append(num)
		print(binary_search(arr, n, c))
    
    
