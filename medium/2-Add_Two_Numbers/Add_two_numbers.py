from typing import Optional
from utils.linked_list import *
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        number1 = 0
        number2 = 0

        finished1 = False
        finished2 = False

        multiplier = 1

        # While any of the list still has elements. Keep going        
        while (not finished1) and (not finished2):

            # Add number with proper multiplier
            if not finished1:
                number1 += l1.val * multiplier   

            if not finished2:
                number2 += l2.val * multiplier

            # Get the next ListNode if it exists
            if not l1.next:
                finished1 = True
            else:
                l1 = l1.next
            if not l2.next:
                finished2 = True
            else:
                l2 = l2.next

            multiplier *= 10

        # Now we have the numbers revesed

        # Add up the two numbers
        number = number1 + number2
        number = str(number)

        firstNode = ListNode()
        node = firstNode

        # Flip the numebr over and make the ListNode
        for n in range(len(number) - 1, -1 , -1):

            node.val = int(number[n])
            
            if n != 0:
                node.next = ListNode()
                node = node.next            

        return firstNode