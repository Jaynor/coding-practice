def binary_tree_helper(root):
    if root.val == None:
        return 0
    right_node_total = binary_tree_helper(root.right)
    left_node_total = binary_tree_helper(root.left)

    temp_root_val = root.val
    root.val = right_node_total + left_node_total

    return temp_root_val + left_node_total + right_node_total


def binary_tree(root):
    return binary_tree_helper(root)