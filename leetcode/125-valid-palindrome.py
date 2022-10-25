import collections
import re
from typing import Deque


# pop()으로 구현
# 맨 왼쪽과 맨 뒤 값을 하나씩 빼면서 같은 값인지 확인
# 틀리다면 팰린더룸이 아님
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))


# 데크로 구현
# 위와 로직은 동일 데크를 사용하게되면 popLeft의 시간복잡도가 O(1)이기 때문에 더 빠르게 구현할 수 있음
def isPalindrome1(s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(isPalindrome1(s))


# 숫자와 문자만 골라낸 뒤에 뒤집은 것과 동일한지 체크
# 슬라이싱 사용
def isPalindrome2(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 슬라이싱


print(isPalindrome2(s))
