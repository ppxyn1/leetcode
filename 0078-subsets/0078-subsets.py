class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx,path):
            #부분집합은 모든 탐색경로가 정답이므로, 탐색할때마다 결과에 추가
            res.append(path)
            #tree route만들면서 DFS
            for i in range(idx, len(nums)):
                dfs(i+1,path+[nums[i]])
            
        dfs(0,[])
        return res
        