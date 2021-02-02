from typing import List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val = 0, link = None):
        self.val = val
        self.next = link

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
            
        return True
    
    def runner(self, head: ListNode):
        fast, slow = head, head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev:
            if rev.val != slow.val:
                return False
            
            rev = rev.next
            slow = slow.next
            
        return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(3)
node5 = ListNode(2)
node6 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

s = Solution()
print(s.isPalindrome(node1))
print(s.runner(node1))
