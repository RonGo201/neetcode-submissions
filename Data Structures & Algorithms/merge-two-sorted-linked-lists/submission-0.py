# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        node1, node2 = list1, list2
        
        while node1 != None and node2 != None:
            if node1.val < node2.val:
                temp.next = node1
                node1 = node1.next
            else:
                temp.next = node2
                node2 = node2.next
            temp = temp.next
        
        if node1 == None:
            temp.next = node2
        else:
            temp.next = node1
        
        return dummy.next