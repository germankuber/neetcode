class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            first = head
            second = head
            for _ in range(n):
                second = second.next
            if second is not None:
                while second.next:
                    first = first.next
                    second = second.next
                    
                first.next = first.next.next
            else:
                return head.next

            return head
        