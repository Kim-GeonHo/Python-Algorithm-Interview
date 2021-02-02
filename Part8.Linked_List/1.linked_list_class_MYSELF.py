class SList:
    class Node:
        def __init__(self, data, link = None):
            self.data = data
            self.next_node = link

    def __init__(self):
        self.size = 0
        self.head_node = None
        self.tail_node = None
        self.before_node = None

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        if self.isEmpty():
            self.head_node = self.Node(data)
            self.tail_node = self.head_node
            self.before_node = self.tail_node

        else:
            self.before_node = self.tail_node
            self.tail_node.next_node = self.Node(data)
            self.tail_node = self.tail_node.next_node
        
        
        self.size += 1

    def delete(self):
        self.before_node.next_node = None
        self.tail_node = self.before_node
        
        self.size -= 1
    
    def show(self):
        current = self.head_node
        while True:
            print("[" + str(current.data) + "]", end = "")

            if current.next_node == None:
                break

            print(" -> ", end = "")

            current = current.next_node            
        print()
    

sl = SList()

sl.append(1)
sl.append(2)
sl.append(3)
sl.show()
sl.delete()
sl.show()
sl.append(4)
sl.show()