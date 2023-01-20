class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(len(nums)):
            if i not in nums:
                print(i)
                return i
        return i+1