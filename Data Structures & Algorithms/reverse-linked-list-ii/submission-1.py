# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
            
        head_to_iterate =  ListNode(0, head)
        
        position_counter = 0
        
        prev_to_left = None
        
        new_right = None
        
        prev = None
        
        to_return = head_to_iterate
        
        while head_to_iterate:
            if position_counter + 1 == left:
                prev_to_left = head_to_iterate
            
            temp_next =  head_to_iterate.next
            
            if position_counter == left:
                new_right = head_to_iterate
                prev = head_to_iterate
                
            elif position_counter == right:
                new_right.next = temp_next
                
                head_to_iterate.next = prev
                
                prev_to_left.next = head_to_iterate
                break
            else:
                if new_right:
                    
                    head_to_iterate.next = prev
                    
                    prev = head_to_iterate
                    
            head_to_iterate = temp_next        
            
            position_counter += 1
            
        return to_return.next