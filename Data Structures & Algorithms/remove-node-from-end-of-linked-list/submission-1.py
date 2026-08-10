# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # finding list length
        temp = head
        len = 1
        while temp.next is not None:
            len += 1
            temp = temp.next
        if len == n:
            return head.next

        # calc steps from start
        temp = head
        counter = len - n - 1
        while counter > 0:
            temp = temp.next
            counter -= 1

        next_node = temp.next.next
        temp.next = next_node

        return head
        