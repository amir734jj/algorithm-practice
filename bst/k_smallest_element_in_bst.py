# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


def k_smallest_element_in_bst(node, k):
    result = [float('inf')] * k
    k_smallest_element_in_bst_rec(node, result)
    return result


def k_smallest_element_in_bst_rec(node, result):
    if type(node) == tuple:
        (left, c, right) = node

        # already found the k smallest
        if c > max(result):
            return

        k_smallest_element_in_bst_rec(left, result)
        max_value = max(result)

        if c < max_value:
            result.remove(max_value)
            result.append(c)

        k_smallest_element_in_bst_rec(right, result)
    elif type(node) == int:
        max_value = max(result)
        if node < max_value:
            result.remove(max_value)
            result.append(node)


root = (((-3, -2, -1), 2, 3), 4, (5, 6, 7))
print(k_smallest_element_in_bst(root, 3))
