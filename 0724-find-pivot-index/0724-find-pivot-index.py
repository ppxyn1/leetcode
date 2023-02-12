class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = 0
        tot = sum(nums)
        for i,j in enumerate(nums):
            print(i)
            if res == tot-res-j:
                return i
            res +=j
        return -1
            
                