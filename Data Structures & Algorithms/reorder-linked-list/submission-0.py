from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        prev = None
        
        current = second
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        second = prev
        
        first = head
        
        while second:
            
            temp_first  = first.next
            
            temp_second = second.next
            
            first.next = second
            
            second.next = temp_first
            
            first = temp_first
            
            second = temp_second
            
        