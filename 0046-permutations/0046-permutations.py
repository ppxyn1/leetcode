import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for x in itertools.permutations(nums, len(nums)):
            print(list(x))
            res.append(list(x))
        return res

'''
        #순열이란 모든 가능한 경우의 수를 그래프 형태로 나열한 결과라고 할 수 있다.
        results = []
        prev_e = []
        
        def dfs(e):
            #리프노드일때 결과 추가
            if len(e) == 0:
                results.append(prev_e[:]) #값복사 형태로 해야함(파이썬은 모든 객체를 참조하는 형태이므로 참조값이 변형되면 모두 바뀜)
                
            #순열 생성 재귀 호출
            for i in e:
                next_e = e[:] 
                next_e.remove(i)
                
                prev_e.append(i)
                dfs(next_e)
                prev_e.pop()
                
        dfs(nums)
        return results
        
'''