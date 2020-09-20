class ListNode:
    pass


class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = this_head = next_head = head
        
        while True:
            count = 0
            while next_head and count < k:   # use r to locate the range
                next_head = next_head.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = next_head, this_head
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, this_head = pre, this_head, next_head  # connect two k-groups
            else:
                return dummy.next