class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        exp = 1
        sum = 0

        while l1:
            sum += l1.val * exp
            l1 = l1.next
            exp *= 10

        exp = 1

        while l2:
            sum += l2.val * exp
            l2 = l2.next
            exp *= 10
        
        return self.toReversedLinkedList(''.join(e for e in str(sum)))
    
    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

sol = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(sol.addTwoNumbers(l1, l2))