# https://leetcode.com/problems/kth-largest-element-in-a-bst/


def k_largest_element_in_bst(node, k):
    result = [float('-inf')] * k
    k_largest_element_in_bst_rec(node, result)
    return result


def k_largest_element_in_bst_rec(node, result):
    if type(node) == tuple:
        (left, c, right) = node

        # already found the k largest
        if c < min(result):
            return

        k_largest_element_in_bst_rec(right, result)
        min_value = min(result)

        if c > min_value:
            result.remove(min_value)
            result.append(c)

        k_largest_element_in_bst_rec(left, result)
    elif type(node) == int:
        min_value = min(result)
        if node > min_value:
            result.remove(min_value)
            result.append(node)


root = (((-3, -2, -1), 2, 3), 4, (5, 6, 7))
print(k_largest_element_in_bst(root, 3))
