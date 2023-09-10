#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
      l = 0
      m = 0
      h = 0
      for i in arr:
          if i == 0:
            l += 1
          elif i == 1:
            m += 1
          else:
              h += 1
      i = 0
      for _ in range(l):
          arr[i] = 0
          i += 1
      for _ in range(m):
          arr[i] = 1
          i += 1
      for _ in range(h):
          arr[i] = 2
          i += 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
