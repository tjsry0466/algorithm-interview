from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 연결 리스트 뒤집기
def reverse_list(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev


# 연결 리스트를 파이썬 리스트로 변환
def to_list(node: ListNode) -> list:
    list: List = []
    while node:
        list.append(node.val)
        node = node.next
    return list


# 파이썬 리스트를 연결 리스트로 변환
def to_reversed_linked_list(result: str) -> ListNode:
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node


# 두 연결 리스트의 덧셈
def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    a = to_list(reverse_list(l1))
    b = to_list(reverse_list(l2))

    result_str = int(''.join(str(e) for e in a)) + \
                 int(''.join(str(e) for e in b))

    # 최종 개선 결과 연결 리스트 변환
    return to_reversed_linked_list(str(result_str))


node3 = ListNode(3)
node4 = ListNode(4, node3)
node2 = ListNode(2, node4)

node4 = ListNode(4)
node6 = ListNode(6, node4)
node5 = ListNode(5, node6)
answer_node = add_two_numbers(node2, node5)

while answer_node and answer_node.val:
    print(answer_node.val)  # 5, 4, 3, 2, 1
    answer_node = answer_node.next
