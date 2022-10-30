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


node2 = ListNode(2)
node1 = ListNode(1, node2)
print(isPalindrome(node1))
print(isPalindrome1(node1))

node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(isPalindrome(node1))
print(isPalindrome1(node1))
