class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        strNum = ''
        strRes = 0
        # string = "".join(num)
        for i in range(len(num)):
            strNum += str(num[i])
        print(strNum)
        strRes = int(strNum)+k
        
        print(str(strRes))
        for i in str(strRes):
            res.append(int(i))
        return res