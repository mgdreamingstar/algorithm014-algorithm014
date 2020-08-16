class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre

            pre = cur
            cur = temp
        
        return pre