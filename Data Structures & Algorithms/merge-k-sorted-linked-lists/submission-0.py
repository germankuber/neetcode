# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        to_merge = lists
        
        if len(lists) == 0:
            return None
        def merge_lists(left: ListNode, right: Optional[ListNode]) -> Optional[ListNode]:
            
            head = ListNode(0, None)
            
            head_to_iterate = head
            
            
            while left or right:
                
                if left is None:
                    head_to_iterate.next  = right
                    break
                if right is None:
                    head_to_iterate.next = left
                    break
                if left.val <= right.val:
                    head_to_iterate.next = left
                    left = left.next
                else:
                    head_to_iterate.next = right
                    right = right.next
                
                head_to_iterate  = head_to_iterate.next
                
            return head.next
            
            
        while len(to_merge) > 1:

            merge = []
        
            for i in range(0, len(to_merge), 2):
                
                left = to_merge[i]
                
                right = to_merge[i + 1] if i + 1 < len(to_merge) else None
                
                merge.append(merge_lists(left, right))
            
            to_merge = merge            
        
        return to_merge[0]