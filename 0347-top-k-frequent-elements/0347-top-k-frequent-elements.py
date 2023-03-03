class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        cnt = collections.Counter(nums)
        sorted(cnt.items(), key=lambda i: i[1])
        # print(dict(cnt)[0])
        return (list(dict(cnt.most_common(k)).keys()))