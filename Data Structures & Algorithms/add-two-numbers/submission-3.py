class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        res_it = res
        leftover = 0

        # Continue if there are nodes left in either list, or a carry remains
        while l1 is not None or l2 is not None or leftover > 0:
            # Get values if nodes exist, otherwise use 0
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            total_sum = l1_val + l2_val + leftover
            
            # Calculate carry and current digit using division and modulo
            leftover = total_sum // 10
            res_it.next = ListNode(total_sum % 10)
            
            # Advance pointers
            res_it = res_it.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return res.next