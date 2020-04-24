# https://leetcode.com/problems/number-of-islands/


def dfs(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != 1:
        return
    else:
        matrix[i][j] = -1
        dfs(matrix, i + 1, j)
        dfs(matrix, i - 1, j)
        dfs(matrix, i, j + 1)
        dfs(matrix, i, j - 1)


def count_islands(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0 and matrix[i][j] != 1:
                raise Exception(f"value is invalid at ({i}, {j}) = {matrix[i][j]}")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                # mark as visited
                count = count + 1
                dfs(matrix, i, j)

    return count


table = [
    ([
         [1, 1, 1, 1, 0],
         [1, 1, 0, 1, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0]
     ], 1),
    ([
         [1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1]
     ], 3)
]

print(list(filter(bool, [matrix for matrix, result in table if count_islands(matrix) != result])))
