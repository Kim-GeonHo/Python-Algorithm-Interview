class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def append(self, item):
        if self.is_empty():
            self.tail = self.Node(item, None)
            self.tail.next = self.tail
        
        else:
            new_node = self.Node(item, self.tail.next)
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def pop(self):

        pop_item = self.tail.next.item

        self.tail.next = self.tail.next.next
        self.size -= 1
        return pop_item

    def show(self):
        t = self.tail.next
        cnt = 0

        while cnt != self.size + 1:
            print(f"[{t.item}] -> ", end="")
            
            t = t.next
            cnt += 1


sl = SList()

N, K = map(int, input().split())

result_list = []

for i in range(1, N + 1):
    sl.append(i)


while not sl.is_empty():
    for _ in range(K - 1):
        sl.tail = sl.tail.next
    
    result_list.append(str(sl.pop()))
    # sl.show()

print(f"<{', '.join(result_list)}>")