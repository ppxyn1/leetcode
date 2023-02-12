class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # parent = edges
        
        #re-define
        parents = {i:i for i in range(n)}
        
        def union(a,b):
            a = find(a)
            b = find(b)
            if a!=b:
                parents[b] = a
                return True
            else:
                return False
        
        def find(x):
            print(x)
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
                          
        for u,v in edges:
            union(u,v)
        
        return find(source)==find(destination)
            
            