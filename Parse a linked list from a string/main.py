from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Convert a string representation of a linked list into a Node chain.

    Args:
        list_repr (str): String like "1 -> 2 -> 3 -> None"

    Returns:
        Node | None: Head of the linked list or None if empty.
    """
    if list_repr == "None":
        return None
    values = list_repr.split(" -> ")
    head_node = None
    for value_str in reversed(values[:-1]):
        head_node = Node(int(value_str), head_node)
    return head_node
