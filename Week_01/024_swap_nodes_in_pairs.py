class ListNode:
    pass


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second
        