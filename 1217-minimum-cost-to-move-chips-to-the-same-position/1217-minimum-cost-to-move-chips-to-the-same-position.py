class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        print(position)
        odd_sum = 0
        even_sum = 0
        # compare odd and even number because the only thing we have to do is moveing odd to even or even to odd
        for i in position: #range(len(position)):
            if i==0 or i%2 == 0:
                odd_sum += 1
            else: 
                even_sum += 1
        print(odd_sum, even_sum)
        return min(even_sum, odd_sum)