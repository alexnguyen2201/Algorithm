def calculate_height(node):
    if not node:
        return 0

    left = calculate_height(node.left)
    right = calculate_height(node.right)

    return max(left, right) + 1