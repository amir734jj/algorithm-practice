# https://leetcode.com/problems/longest-common-subsequence/

def lcs(a, b):
    buffer = ''
    a, b = list(a), list(b)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                buffer += a[i]
                i = i + 1
            else:
                if len(buffer) > 1:
                    yield buffer
                buffer = ''


print(max(lcs('AMIR HOSSEIN', 'HOSSEIN'), key=len))
