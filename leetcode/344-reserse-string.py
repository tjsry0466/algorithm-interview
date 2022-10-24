from typing import List


def reserseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)
reserseString(["h","e","l","l","o"])

def reserveString1(s: List[str]) -> None:
    s.reverse()
    print(s)
reserveString1(["h","e","l","l","o"])