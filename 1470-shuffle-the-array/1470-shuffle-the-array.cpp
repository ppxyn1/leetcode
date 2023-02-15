class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1,arr2,res =[], [], []
        size = len(nums)
        for i in range(size):
            if i< (size//2):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        
        for i in range(size//2):
            res.append(arr1[i])
            res.append(arr2[i])
        
        return res