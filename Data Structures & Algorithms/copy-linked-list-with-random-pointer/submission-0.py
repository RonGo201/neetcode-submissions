"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None: None}
        temp = head
        while temp is not None:
            copies[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp is not None:
            copies[temp].random = copies[temp.random]
            temp = temp.next
        
        temp = head
        copy = Node(-1)
        copy_iterator = copy
        while temp is not None:
            copy_iterator.next = copies[temp]
            copy_iterator = copy_iterator.next
            temp = temp.next
        
        return copy.next