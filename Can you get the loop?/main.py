def loop_size(node):
    """
    Determine the length of the loop in a linked list.

    This function uses Floyd's Tortoise and Hare algorithm to find the loop.
    Once the meeting point inside the loop is found, it counts the number of
    nodes in the loop to return its size.

    Args:
        node (Node): Head of the linked list (may contain a dangling part before the loop).

    Returns:
        int: The number of nodes in the loop.
    """
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    c = 1
    cur = slow.next
    while cur != slow:
        c +=1
        cur = cur.next
    return c
