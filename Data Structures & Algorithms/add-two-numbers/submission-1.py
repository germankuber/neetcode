from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        iterate = head
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            if total > 9:
                carry = 1
                iterate.next = ListNode(total - 10)
            else:
                carry = 0
                iterate.next = ListNode(total)
            iterate = iterate.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return head.next