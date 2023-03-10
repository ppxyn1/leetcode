class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane algo
        best_sum = -sys.maxsize
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum+num)
            best_sum = max(best_sum, curr_sum)
        return best_sum