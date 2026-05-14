class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_lists(left, right):
            head = ListNode(0)
            curr = head
            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            curr.next = left if left else right
            return head.next
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                right = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge_lists(lists[i], right))
            lists = merged
        
        return lists[0] if lists else None