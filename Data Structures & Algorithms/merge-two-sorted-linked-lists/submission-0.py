
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(head_1: Optional[ListNode], head_2: Optional[ListNode]) -> Optional[ListNode]:
            if head_1 is None:
                return head_2
            if head_2 is None:
                return head_1
            
            if head_1.val <= head_2.val:
                head_1.next = merge(head_1.next, head_2)
                return head_1
            else:
                head_2.next = merge(head_1, head_2.next)
                return head_2
        return merge(list1, list2)
            