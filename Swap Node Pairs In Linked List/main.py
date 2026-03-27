from preloaded import Node

def swap_pairs(head):
    """
    Recursively swap every pair of nodes in a singly linked list.

    Args:
        head (Node | None): Head of the linked list

    Returns:
        Node | None: Head of the updated list with nodes swapped in pairs
    """
    if not head or not head.next:
        return head
    first_node = head
    second_node = head.next
    first_node.next = swap_pairs(second_node.next)
    second_node.next = first_node
    return second_node
