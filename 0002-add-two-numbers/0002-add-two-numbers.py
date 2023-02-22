# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #342 + 465 = 807
        arr1,arr2 = [],[]
        while l1 or l2:
            if l1:
                arr1.append(l1.val)
                l1 = l1.next
            if l2:
                arr2.append(l2.val)
                l2 = l2.next
        print(arr1, arr2)
        n1 = ''.join(str(x) for x in arr1[::-1])
        n2 = ''.join(str(x) for x in arr2[::-1])
        print(n1,n2)
        sum = int(n1)+int(n2)
        
        res = []
        answer = ListNode() #ListNode로 초기화 - 더미 노드가 된다. 이부분을 찾아보고 이해하는데 시간이 걸렸다...
        curr= answer 
        for i in str(sum)[::-1]:
            # if curr.val is not None:
            curr.next = ListNode(i) 
            print(curr.next.val)
            curr = curr.next
        return answer.next