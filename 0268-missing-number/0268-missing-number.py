class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sorting
        nums.sort()
        # for len nums 
        for i in range(len(nums)):
            # if there is missing num between nums
            if i not in nums:
                print(i)
                return i
        # if missing num locate in the last
        return i+1