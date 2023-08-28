#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,A, N): 
        ##Your code here
        ans = 0
        # for i in range(0, N):
        #     for j in range(i+1,N):
        #         if A[i] <= A[j]:
        #             ans = max(ans, j - i)
        min_arr = []
        min_ele = A[0]
        min_arr.append(min_ele)
        for i in range(1,N):
            min_ele = min(min_ele, A[i])
            min_arr.append(min_ele)
        
        max_arr = []
        max_ele = A[N-1]
        max_arr.append(max_ele)
        for i in range(N-2,-1,-1):
            max_ele = max(max_ele, A[i])
            max_arr.append(max_ele)
        max_arr.reverse()
        # print(min_arr)
        # print(max_arr)
        # print(len(max_arr), len(min_arr))
        i,j = 0,0
        while i < N and j < N:
            if (max_arr[i] >= min_arr[j]):
                ans = max(ans,i - j)
                i += 1
            else:
                j += 1
        
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends