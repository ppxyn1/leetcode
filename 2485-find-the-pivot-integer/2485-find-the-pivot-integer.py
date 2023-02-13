class Solution:
    def pivotInteger(self, n: int) -> int:
        totSum = 0
        res = 0
        for i in range(1,n+1):
            totSum += i
        print(f'totSum:{totSum}')
        
        for i in range(1,n+1):
            if res == totSum-res-i:
                return i
            res +=i
        return -1
    

            
            
