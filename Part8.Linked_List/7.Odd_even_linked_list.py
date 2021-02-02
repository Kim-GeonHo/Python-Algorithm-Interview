class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def myself(self, head: ListNode) -> ListNode:
        if not head:
            return None

        root = head
        even_root = root.next

        odd = head
        even = head.next

        while odd and odd.next:
            odd.next, odd = odd.next.next, odd.next.next
        
            if even and even.next:
                even.next, even = even.next.next, even.next.next

        if odd:
            odd.next = even_root
        else:
            while head.next:
                head = head.next
            head.next = even_root

        return root
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            
            odd, even = odd.next, even.next
        
        odd.next = even_head

        return head
        
        
        # while root:
        #     print(f'{root.val} -> ', end='')
        #     root = root.next
        return root


sol = Solution()

head = ListNode(2)
l2 = ListNode(1)
l3 = ListNode(3)
l4 = ListNode(5)
l5= ListNode(6)
l6 = ListNode(4)
l7 = ListNode(7)
# l8 = ListNode(8)

head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
# l7.next = l8

print(sol.oddEvenList(head))