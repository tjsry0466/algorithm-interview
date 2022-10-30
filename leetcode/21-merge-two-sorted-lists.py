class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:  # ✅다시 풀어보기
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_two_lists(l1.next, l2)
    return l1


node4 = ListNode(4)
node2 = ListNode(2, node4)
node1 = ListNode(1, node2)

node4_ = ListNode(4)
node3_ = ListNode(3, node4_)
node1_ = ListNode(1, node3_)
answer_node = merge_two_lists(node1, node1_)

while answer_node and answer_node.val:
    print(answer_node.val)  # 1, 1, 2, 3, 4, 4
    answer_node = answer_node.next
