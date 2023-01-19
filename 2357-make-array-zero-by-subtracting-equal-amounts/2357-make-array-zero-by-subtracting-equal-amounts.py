class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # counter
        count = 0
        # while loop 
        while sum(nums) !=0:
            # remove 0
            nums = [i for i in nums if i!=0]
            # choose a minimum number
            idx = min(nums)
            # subtract it from each element
            nums = list(map(lambda a:a-idx, nums))
            # increment the counter
            count +=1
        return count
        
        