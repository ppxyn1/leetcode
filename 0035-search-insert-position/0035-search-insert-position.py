class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        results = 1e9
        idx = []
        for i in range(len(nums)):
            # case1: nums doesn`t have a target and range in nums
            if nums[i] > target:
                idx.append(i)
            # case2: nums has target 
            elif nums[i] == target: 
                results= i
        # target > max OR target < min among case1       
        if results == 1e9 and target>max(nums):
            return len(nums)
        elif results == 1e9 and target<max(nums):
            return min(idx)  
        # case 2
        else:
            return results
        
 
        