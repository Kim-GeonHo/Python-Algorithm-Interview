class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def value_change(self, head: ListNode) -> ListNode:
        root = head

        while head:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return root

    def repeat(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        
        return root.next

    def recursion(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.recursion(p.next)
            p.next = head
            return p
        
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution()


print(sol.value_change(head))