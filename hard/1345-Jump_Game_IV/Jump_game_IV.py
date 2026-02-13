from typing import List
from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        if n == 1: return 0

        # Hashmap to map every node with equal value
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        # The queue starts with index 0 and 0 steps
        queue = deque([(0, 0)]) # (index, steps)

        visited = set([0]) # Here goes the already visited nodes

        # While there are nodes to explore...
        while queue:
            
            idx, steps = queue.popleft()

            # If we got to the end node, because it's a BFS we know that we've got the fastest path
            if idx == (n - 1): return steps # return the answer

            neighbors = []

            # Add adjacent neightbors if they are inside the array length
            if (idx - 1) >= 0:
                neighbors.append(idx - 1)
            if (idx + 1) < n:
                neighbors.append(idx + 1)

            neighbors.extend(graph[arr[idx]])

            for nxt in neighbors:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

            # Delete this to not step over again.
            graph[arr[idx]].clear()

