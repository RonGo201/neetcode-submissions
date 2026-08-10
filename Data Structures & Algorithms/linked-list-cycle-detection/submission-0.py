# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        pointer1, pointer2 = head, head.next
        while pointer2 is not None and pointer2.next is not None:
            if pointer1 == pointer2:
                return True
            
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        
        return False
