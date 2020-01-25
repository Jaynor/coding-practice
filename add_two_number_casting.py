# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def convert_int(List1: ListNode):
    temp = ""
    while List1:
        temp += str(List1.val)
        List1 = List1.next
    return int(temp[::-1])


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1 = convert_int(l1) + convert_int(l2)
        t1 = str(t1)[::-1]
        result = ListNode(t1[0])
        pointer = result
        for i in range(len(t1) - 1):
            temp = ListNode(t1[i + 1])
            pointer.next = temp
            pointer = pointer.next
        return (result)

