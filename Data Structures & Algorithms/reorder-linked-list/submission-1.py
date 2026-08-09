class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        pointer1 = head
        pointer2 = head
        
        while pointer2 != None and pointer2.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        cur = pointer1.next
        pointer1.next = None
        
        # Reverse the second half
        prev = None
        while cur != None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        l1 = head
        l2 = prev
        
        while l2 != None:
            tmp1 = l1.next
            tmp2 = l2.next
            
            l1.next = l2
            l2.next = tmp1
            
            l1 = tmp1
            l2 = tmp2

        