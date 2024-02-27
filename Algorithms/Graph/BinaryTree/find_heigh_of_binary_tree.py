def cal_height(node):
    if not node:
        return 0

    left = cal_height(node.left)
    right = cal_height(node.right)

    return max(left, right) + 1