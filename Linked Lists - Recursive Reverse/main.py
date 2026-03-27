class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Recursively reverse a singly linked list.

    Args:
        head (Node | None): Head of the linked list

    Returns:
        Node | None: Head of the reversed linked list
    """
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head
