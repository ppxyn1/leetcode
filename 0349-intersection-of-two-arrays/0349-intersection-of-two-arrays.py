class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1 = list(set(nums1))
        n2 = list(set(nums2))
        res = []
        # length = len(n1) 
        # length = len(n2) if len(n1) >= len(n2) else length
        # print(length)
        
        # length = len(n2) if len(n1) >= len(n2) else length

        for i in range(len(n2)):
            for j in range(len(n1)):
                if list(n1)[j] == list(n2)[i]:
                    res.append(list(n2)[i])
        return res