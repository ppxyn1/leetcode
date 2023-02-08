class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        results = ""
        strs.sort(key=len)
        # print(strs)
        
        #check character based on first word
        for i in range(len(strs[0])):
            for j in strs:
                #outerbounds & inbounds
                if i == len(j) or j[i] != strs[0][i]:
                    return results
            results += strs[0][i]
            
        return results