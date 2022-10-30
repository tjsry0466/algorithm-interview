class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


def reverse_list1(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


node5_ = ListNode(5)
node4_ = ListNode(4, node5_)
node3_ = ListNode(3, node4_)
node2_ = ListNode(2, node3_)
node1_ = ListNode(1, node2_)
answer_node = reverse_list(node1_)

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
answer_node1 = reverse_list1(node1)

while answer_node and answer_node.val:
    print(answer_node.val)  # 5, 4, 3, 2, 1
    answer_node = answer_node.next

print()
while answer_node1 and answer_node1.val:
    print(answer_node1.val)  # 5, 4, 3, 2, 1
    answer_node1 = answer_node1.next
