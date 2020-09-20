class ListNode:
    pass


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head
        
        while True:
            if not (fast and fast.next):
                return None
            
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        
        new_slow = head
        while new_slow != slow:
            new_slow = new_slow.next
            slow = slow.next
        
        return new_slow