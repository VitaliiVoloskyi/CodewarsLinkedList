from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    """
    Insert a new node at the beginning of the list.

    Args:
        head (Node | None): Current head of the list
        data (int): Value to insert

    Returns:
        Node: New head of the list
    """
    new_head = Node(data)
    new_head.next = head
    return new_head

def build_one_two_three():
    """
    Build the linked list: 1 -> 2 -> 3 -> None

    Returns:
        Node: Head of the created list
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
