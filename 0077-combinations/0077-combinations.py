class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i+1 for i in range(n)]
        component = [0] * k
        res = []
        def comb(level,start):
            if level==k:
                # print(component)
                res.append(component.copy())
                return 
            for i in range(start,n-k+level+1):
                component[level]=arr[i]
                comb(level+1, i+1)
            
        comb(0,0)
        return res
        
        
        
        
'''
        # res = []  time limit
        arr = [i+1 for i in range(n)]
        def comb(arr, k):
            res = []
            if k == 0:
                return [[]]
            
            for i in range(len(arr)):
                elem = arr[i]
                # print(arr[i+1:])
                for rest in comb(arr[i + 1:], k - 1):
                    res.append([elem] + rest)
                    print(res)
            return res

        return comb(arr, k)
'''
        
'''
        def dfs(e, start:int, k:int):
            if k==0: 
                result.append(e[:])
    
            #자신 이전 모든 값을 고정하여 재귀 호출
            for i in range(start, n+1):
                e.append(i)
                dfs(e, i+1, k-1)
                # print(f'e:{e}')
                e.pop()
            
        dfs([],1,k)
        return result
        
'''
