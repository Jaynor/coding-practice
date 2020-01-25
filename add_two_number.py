# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        carry = 0
        l3 = ListNode(None)
        result = l3
        while l1 != None or l2 != None:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum = sum + carry
            if sum > 9:
                carry = 1
            else:
                carry = 0
            l3.val = (sum) % 10
            sum = 0
            l3.next = ListNode(None)
            l3 = l3.next
        print(result)
        temp = result
        while 1:
            if temp.next.val == None:
                if carry == 1:
                    temp.next.val = carry
                else:
                    temp.next = None
                break
            temp = temp.next

        return (result)