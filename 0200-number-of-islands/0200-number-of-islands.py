class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i,j):
            # print(f'i:{i}, j:{j}')
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j]!='1' or (i,j) in visited:
                return 
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    res +=1
                    visited.add((i,j))
        return res