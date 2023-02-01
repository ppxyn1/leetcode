class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        results = 0
        next_checked = 0
    
        for i in range(len(s)):
            #if there is a number which matched, start for loop and check from next number.
            for j in range(next_checked,len(g)):
                # print(f'j:{j}')
                if s[i] >= g[j]:
                    results+=1
                    # print(s[i],g[j])
                    next_checked = j+1
                    break
        return results