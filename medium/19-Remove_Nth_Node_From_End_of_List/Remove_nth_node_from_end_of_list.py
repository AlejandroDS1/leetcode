from typing import Optional
from collections import deque
from utils.linked_list import *

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pointer = head # We are going to iterate over the array

        queue = deque([head])
        length_of_array = 1 # This is going to be usefull to keep track of the lenght of the array

        # While there are nodes left to check
        while pointer.next:

            length_of_array += 1
            pointer = pointer.next

            if len(queue) == n + 1:
                queue.popleft()
            
            queue.append(pointer)

        # There are some extreme cases
        
        # 1. The lenght of the queue is 1. That means that the lenght of the array was 1.
        # Because n can not be 0. Therefore we return None
        if len(queue) == 1:
            return None

        # If n == length of the array. Just return the second node
        if n == length_of_array: return head.next

        # If there are elements in the queue
        if len(queue) > 0:
            prev_node = queue.popleft()

            queue.popleft()

            # If there's still nodes in the queue
            # If there aren't any more nodes this node is going to be null
            prev_node.next = queue.popleft() if queue else None
    
        return head