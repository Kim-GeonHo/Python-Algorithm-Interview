from typing import List

class ListNode:
    def __init__(self, val : int, link = None):
        self.val = val
        self.next = link

class Solution:
    def runner(self, head : ListNode):
        fast, slow = head, head
        rev = None

        # while True:
        #     fast = fast.next.next

        #     rev = slow
        #     rev.next = rev
        #     # 이 nev의 next는 nev(1)이고 그 다음 nev(1)의 next 역시 nev(1) .....
        #     # 1 -> 1 -> 1 -> 1-> 1-> .....
        #     slow = slow.next
            # break

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while slow and slow.val == rev.val:
            slow, rev = slow.next, rev.next
        return not rev
        


Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(2)
Node4 = ListNode(2)
Node5 = ListNode(2)
Node6 = ListNode(1)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6

sol = Solution()
print(sol.runner(Node1))