class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    """
    Split a linked list into two lists by alternating nodes, returning them in a Context object.

    Args:
        head (Node): Head of the original linked list. Must contain at least two nodes.

    Returns:
        Context: An object with 'first' and 'second' attributes pointing to the two alternating lists.

    Raises:
        Exception: If the input list is empty or contains only one node.
    """
    if head is None or head.next is None:
        raise Exception
    first_node = head
    second_node = head.next
    context = Context(first_node, second_node)
    while second_node:
        next_first = second_node.next
        first_node.next = next_first
        second_node.next = next_first.next if next_first else None
        first_node, second_node = next_first, second_node.next
    return context
