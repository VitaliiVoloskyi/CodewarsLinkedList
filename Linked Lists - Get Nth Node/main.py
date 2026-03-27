from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node: Node | None, index: int) -> Node:
    """
    Return the node at the specified index in a singly linked list.

    Args:
        node (Node | None): The head of the linked list.
        index (int): Zero-based index of the node to retrieve.

    Returns:
        Node: The node at the given index.

    Raises:
        Exception: If the list is empty, the index is negative, 
                   or the index is out of range.
    
    Example:
        linked_list = Node(1, Node(2, Node(3)))
        get_nth(linked_list, 0).data  # returns 1
        get_nth(linked_list, 1).data  # returns 2
        get_nth(linked_list, 2).data  # returns 3
        get_nth(linked_list, 3)       # raises Exception
    """
    if node is None or index < 0:
        raise Exception("Index out of range")
    current_node = node
    for _ in range(index):
        if current_node.next is None:
            raise Exception("Index out of range")
        current_node = current_node.next
    return current_node
  
