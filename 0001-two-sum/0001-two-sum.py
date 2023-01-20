class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums,target)
        results =[]
        for i in range(len(nums)):
            for j in range(i):
                if target== nums[i] + nums[j]:
                    results.append([i,j])
        return results[0]