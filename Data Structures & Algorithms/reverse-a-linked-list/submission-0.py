class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(prev: Optional[ListNode], current: Optional[ListNode]) -> Optional[ListNode]:
            if current is None:
                return prev
            
            next_node = current.next
            current.next = prev
            
            return reverse(current, next_node)
        
        return reverse(None, head)