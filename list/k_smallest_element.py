# https://leetcode.com/problems/kth-smallest-element-in-an-array/


def k_smallest_element(arr, k):
    result = [float('inf')] * k

    for item in arr:
        max_element = max(result)
        if item < max_element:
            result.remove(max_element)
            result.append(item)

    print(result)


k_smallest_element([1, 2, 3, 4, -1, 5, 6, -4], 3)
