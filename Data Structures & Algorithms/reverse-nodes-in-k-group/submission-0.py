from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        # Dummy node simplifies handling the head changes.
        dummy = ListNode(0, head)

        # Points to the node before the current group.
        group_prev = dummy

        while True:
            # Find the k-th node starting from group_prev.
            kth = self.get_kth(group_prev, k)

            # Not enough nodes remaining to form a full group.
            if not kth:
                break

            # First node after the current group.
            group_next = kth.next

            # Reverse the group.
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Reconnect the reversed group with the list.
            tmp = group_prev.next  # Original first node (becomes last).
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def get_kth(
        self,
        curr: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        """
        Returns the k-th node after curr.
        Returns None if fewer than k nodes exist.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr