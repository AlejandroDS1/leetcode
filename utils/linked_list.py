from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list_node_from_array(arr: List):

    FIRST_NODE = ListNode()
    node = FIRST_NODE

    for n in range(len(arr)):
        node.val = arr[n]

        if n != len(arr) -1:
            node.next = ListNode()
            node = node.next
    return FIRST_NODE


def print_linkedNode_as_array(node: ListNode):
    print("[", end="")

    while node:
        print(node.val, end="")
        if node.next:
            print(", ", end="")
        node = node.next
    print("]")