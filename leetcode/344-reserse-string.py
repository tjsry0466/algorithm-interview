from typing import List


def reserse_string(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)


reserse_string(["h", "e", "l", "l", "o"])


def reserve_string1(s: List[str]) -> None:
    s.reverse()
    print(s)


reserve_string1(["h", "e", "l", "l", "o"])
