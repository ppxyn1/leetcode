class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #aA가 보석인게 아니라,a,A가 보석

# Solution 2      
#         cnt = 0
#         freqs = collections.Counter(stones)
#         # print(freqs)
#         for c in jewels:
#             cnt += freqs[c]
        
#         return cnt


#Solution 1
        freqs = collections.defaultdict(int)
        cnt = 0
        
        for c in stones:
            freqs[c] +=1
            
        for c in jewels:
            cnt += freqs[c]
            
        return cnt