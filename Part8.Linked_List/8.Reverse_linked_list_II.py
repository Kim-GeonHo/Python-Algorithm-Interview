class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n == m:
            return head
        
        root = before = start = end = head


        for i in range(n - 1):
            if i < m - 2:
                before = before.next
            if i < m - 1:
                start = start.next

            end = end.next

        prev = end.next

        for i in range(n - m + 1):
            next = start.next
            start.next = prev 
            prev = start
            start = next

        if m != 1:
            before.next = prev
        else:
            root = prev


        return root


        
sol = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

m, n = map(int, input().split())

sol.reverseBetween(l1, m, n)
