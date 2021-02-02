class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(slef, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0

        while l1 or l2 or carry:
            sum = 0

            sum += l1.val
            l1 = l1.next

            sum += l2.val
            l2 = l2.next

            carry, val = divmod(carry + sum, 10)
            head.next = ListNode(val)
            head = head.next

        
        return root.next
            