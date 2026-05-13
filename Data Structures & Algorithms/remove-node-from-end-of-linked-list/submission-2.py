class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = second = dummy
        
        # avanzar second n pasos para crear el gap
        for _ in range(n):
            second = second.next
        
        # mover los dos juntos hasta que second llegue al último nodo
        while second.next:
            first = first.next
            second = second.next
        
        # first está justo antes del nodo a borrar
        first.next = first.next.next
        
        return dummy.next