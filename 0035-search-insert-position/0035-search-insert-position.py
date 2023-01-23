class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        results = 1e9
        idx = []
        # case1: nums has target 
        for i in range(len(nums)):
            if nums[i] > target:
                idx.append(i)
            elif nums[i] == target: 
                results= i
        # case2: nums doesn`t have a target
        print(idx)
        if results == 1e9 and target>max(nums):
            return len(nums)
        elif results == 1e9 and target<max(nums):
            return min(idx)  
        else:
            return results