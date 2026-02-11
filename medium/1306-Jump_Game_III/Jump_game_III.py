from typing import List
from collections import deque

class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:

        visited = set() # Visited indexes are going to be in this set
        queue = deque([start]) # Queue of indexes to visit

        while queue:
            idx = queue.popleft() # Take the inded of the queue

            # If we reached the 0 return True
            if arr[idx] == 0: return True

            # If we've already visited this node we can continue
            if idx in visited: continue

            visited.add(idx) # Add the node to visited if it is not visited yet

            # Add the following nodes to the stack
            for new_idx in (idx + arr[idx], idx - arr[idx]):
                if (new_idx > (len(arr) -1)) or (new_idx < 0):
                    continue
                queue.append(new_idx)
            
        return False