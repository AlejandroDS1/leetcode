# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        number = 0
        output = ListNode()
        pointer = output

        while head.next:
            head = head.next
            if head.val == 0:
                if head.next:
                    pointer.val = number
                    pointer.next = ListNode()
                    pointer = pointer.next
                    number = 0
                else:
                    pointer.val = number
            else:
                number += head.val

        return output