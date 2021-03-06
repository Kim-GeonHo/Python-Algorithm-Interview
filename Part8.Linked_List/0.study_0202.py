class EmptyError(Exception):
    pass

class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size_(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        
        else:
            self.head = self.Node(item, self.head)

        self.size += 1

    def insert_after(self, item, p):
        p.next = self.Node(item, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')

        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError('Underflow')

        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):
        p = self.head

        for i in range(self.size):
            if p.item == target:
                return i
            
            p = p.next
        
        return None

    def print_list(self):
        p = self.head

        while True:
            print("[" + str(p.item) + "]", end = "")

            if p.next == None:
                break
                
            print(" -> ", end = "")
            p = p.next
        print()

sl = SList()

# self.size = 0
# self.head = None

# print(sl.size_())
# print(sl.is_empty())

sl.insert_front(1)
sl.insert_front(2)
sl.insert_after(7, sl.head)
sl.insert_front(5)
# 5 2 7 1

sl.print_list()