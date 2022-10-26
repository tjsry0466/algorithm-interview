from typing import List

str = "babad"


def longest_palidrome(str: str):
    def expand(left: int, right: int) -> List[int]:
        while left > -1 and right < len(str) and str[left] == str[right]:
            left -= 1
            right += 1
        return str[left + 1: right]

    if len(str) < 2 or str == str[::-1]:
        return str

    result = ''
    for i in range(len(str) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


print(longest_palidrome(str))
