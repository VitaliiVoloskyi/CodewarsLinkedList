class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Remove duplicate nodes from a sorted linked list.

    Args:
        head (Node | None): Head of a sorted linked list

    Returns:
        Node | None: Head of the list with duplicates removed
    """
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
  
