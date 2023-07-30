class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #l = 0
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]: #unique value
                nums[l] = nums[r]
                l+=1
            r += 1
        # print(nums)
        return l 