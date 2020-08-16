class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not (head and head.next):
            return False
        
        fast, slow = head.next, head
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True