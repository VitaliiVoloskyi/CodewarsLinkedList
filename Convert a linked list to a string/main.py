def stringify(node):
    """
    Convert a singly linked list into its string representation.

    Each node's value is followed by " -> ", and the sequence
    ends with "None".

    Args:
        node (Node or None): The head of the linked list.

    Returns:
        str: A string representation of the linked list.

    Example:
        Node(1, Node(2, Node(3))) -> "1 -> 2 -> 3 -> None"
        None -> "None"
    """
    res = ""
    while node is not None:
        res += str(node.data) + " -> "
        node = node.next
    res += "None"
    return res
