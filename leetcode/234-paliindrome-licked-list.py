import collections
from typing import List, Optional, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    q: List = []

    if not head:
        return True

    # 리스트 반환
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


def isPalindrome1(head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True


def isPalindrome2(head: ListNode) -> bool:  # ✅다시 풀어보기
    rev = None
    slow = fast = head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:  # 입력값이 홀수일때 slow 러너를 한칸 더 이동하여 체크에서 배제
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev  # return not slow도 가능


node2 = ListNode(2)
node1 = ListNode(1, node2)
print(isPalindrome(node1))
print(isPalindrome1(node1))
print(isPalindrome2(node1))

node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(isPalindrome(node1))
print(isPalindrome1(node1))
print(isPalindrome2(node1))
