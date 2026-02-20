from typing import Optional
from utils.linked_list import *

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def find_minimum_node() -> int:
            
            minimum = (float('inf'), -1)

            for idx in range(len(lists)):

                # If that list is ended, continue                
                if ended_lists[idx]:
                    continue

                if minimum[0] > lists[idx].val:
                    minimum = (lists[idx].val, idx)
            
            return minimum[1]


        if len(lists) == 0: return
        if len(lists) == 1: return lists[0]

        ROOT = ListNode()

        previous_node = None
    
        ended_lists = [node == [] for node in lists]
        lists_to_end = ended_lists.count(False)

        while lists_to_end:

            previous_node = previous_node.next if previous_node != None else ROOT

            min_node_idx = find_minimum_node()
            if min_node_idx == -1: return

            min_node = lists[min_node_idx]

            previous_node.val = min_node.val
            previous_node.next = ListNode()

            # Now we check if there are still nodes in this list.
            # If not, its time to mark it as it is.
            if not min_node.next:
                lists_to_end -= 1
                ended_lists[min_node_idx] = True
            else:
                lists[min_node_idx] = lists[min_node_idx].next


        previous_node.next = None
        return ROOT