# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        
        iterate = head
        
        def get_value(l1: Optional[ListNode]) -> int:
            if l1 is not None:
                return l1.val
            return 0
        carry = 0
        while l1 or l2:
            
            l1_result =  get_value(l1)
            
            l2_result = get_value(l2)
            
            result = l1_result + l2_result + carry
            
            if result > 9:
                carry = 1
                iterate.next = ListNode(result - 10, None)
            else:
                carry = 0
                iterate.next = ListNode(result, None)
                
            
            
            iterate = iterate.next
            
            
            
            
            
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            while carry > 0:
                result = 0
                if carry > 9:
                    
                    result = 9
                    carry -= 9
                else:
                    result = carry
                    carry = 0
                    
                    
                iterate.next = ListNode(result, None)
                
                iterate = iterate.next
        return head.next
        
        