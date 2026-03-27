class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    """
    Move the first node from the source list to the front of the dest list.

    Args:
        source (Node | None): Head of the source linked list
        dest (Node | None): Head of the destination linked list

    Returns:
        Context: Object containing the updated source and dest lists

    Raises:
        Exception: If the source list is empty
    """
    if source is None:
        raise Exception("Source list is empty")
    moved_node = source
    source = source.next
    moved_node.next = dest
    dest = moved_node
    return Context(source, dest)
