class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        print(f'gain:{gain}')
        res =[0]
        for i in range(len(gain)):
            val = res[i]+gain[i]
            res.append(val)
        return max(res)