""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    """
    Insert a node with given data into a sorted linked list.

    Args:
        head (Node | None): Head of a sorted linked list
        data (int): Value for the new node

    Returns:
        Node: Head of the updated sorted linked list
    """
    new_node = Node(data)
    if not head or data <= head.data:
        new_node.next = head
        return new_node
    prev = head
    while prev.next and prev.next.data < data:
        prev = prev.next
    new_node.next = prev.next
    prev.next = new_node
    return head
