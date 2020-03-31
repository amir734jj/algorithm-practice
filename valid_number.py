# https://leetcode.com/problems/valid-number/
import re


def is_valid_number(token):
    return bool(re.fullmatch(r"\s*([+-]?((\d*\.)?\d+))(e[+-]?\d+)?\s*", token))


table = {
    "0": True,
    " 0.1 ": True,
    "abc": False,
    "1 a": False,
    "2e10": True,
    " -90e3   ": True,
    " 1e": False,
    "e3": False,
    " 6e-1": True,
    " 99e2.5 ": False,
    "53.5e93": True,
    " --6 ": False,
    "-+3": False,
    "95a54e53": False
}

print(list(filter(bool, [s for s, r in table.items() if is_valid_number(s) != r])))
