class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_num = set()
        for i in nums:
            if i not in set_num:
                set_num.add(i)
            else:
                set_num.remove(i)
        results = list(set_num)[0]
        return results

