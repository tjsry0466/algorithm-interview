import re

words = "A man , a plan, a canal: Panama"


def valid_palindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


print(valid_palindrome(words))
