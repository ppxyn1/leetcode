# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()
        
        #exceptional when no data in head
        if not head:
            return True
        
        #moving head data to deque for bidirectional output
        node=head 
        while node is not None:
            q.append(node.val)
            node=node.next
        
        # len > 1 is for considering odd number 
        while len(q)>1:
            if q.popleft() !=q.pop():
                return False
        return True
        