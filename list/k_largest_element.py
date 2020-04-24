# https://leetcode.com/problems/kth-largest-element-in-an-array/


def k_largest_element(arr, k):
    result = [float('-inf')] * k

    for item in arr:
        min_element = min(result)
        if item > min_element:
            result.remove(min_element)
            result.append(item)

    print(result)


k_largest_element([1, 2, 3, 4, -1, 5, 6, -4], 3)
