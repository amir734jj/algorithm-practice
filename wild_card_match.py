# https://leetcode.com/problems/wildcard-matching/


def lookahead(token, i):
    if i+1 < len(token):
        return token[i+1]
    else:
        return ''


def is_valid_match(token, pattern):
    j = 0
    for i, c in enumerate(token):
        if len(pattern) == j:
            return True
        if pattern[j] == c:
            j = j + 1
        elif pattern[j] == '*':
            j = j + 1
        elif pattern[j] == '?':
            j = j + 1
        else:
            j = 0

    return False


table = {
    ("aa", "a"): True,
    ("aa", "*"): True,
    ("cb", "?a"): False,
    ("adceb", "*a*b"): True,
    ("acdcb", "a*c?b"): False
}

print(list(filter(bool, [s for s, r in table.items() if is_valid_match(*s) != r])))
