class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        # print(parent)
        path=[]
        results = 0

        def union(a,b):
            a = find(a)
            b = find(b)
            if a!=b:
                parent[b] = a
                return True
            else:
                return False

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]

        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                path.append((dist,i,j))

        path.sort()
        # print(path)
        for dist, p1, p2 in path:
            # not cycle 
            if union(p1,p2):  
                results += dist
        return results