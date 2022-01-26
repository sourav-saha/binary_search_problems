'''
https://www.interviewbit.com/problems/allocate-books/
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	
	def check_possible(self, A, B, m):
		student = 1
		sum_ = 0
		for i in range(len(A)):
			sum_ += A[i]
			if sum_ > m:
				student += 1
				sum_ = A[i]

			if student > B:
				return False
		return True  
		
	
	def books(self, A, B):
		start = max(A)
		end = sum(A)
		ans = -1
    #corner cases
		if (len(A) == B): #no. of students equals to array elements 
			return max(A)
		elif B == 1: #if only 1 student 
			return sum(A)
		elif len(A) < B: #array elements are less than number of students
			return -1 

    #binary search approach 
		while (start <= end):
			m = (start+end)//2
			if self.check_possible(A, B, m):
				ans = m
				end = m -1 
			else:
				start = m+1 
		
		return ans
  
  
