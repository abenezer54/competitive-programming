class Node:
    def __init__(self, val = -1):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0
        

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head.next:
            self.tail.next = node
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        self.size += 1
        node = Node(val)
        if (not self.head.next) or (not self.tail.next):
            self.head.next = node
            self.tail.next = node        
            return
        temp = self.tail.next
        temp.next = node
        self.tail.next = node


    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            if index == self.size:
                self.addAtTail(val)
                return
            elif index == 0:
                self.addAtHead(val)
                return
            self.size += 1
            node = Node(val)
            curr = self.head.next
            i = 0
            while curr:
                if i == index - 1:
                    node.next = curr.next
                    curr.next = node
                    return
                i += 1
                curr = curr.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        
        if index == 0:
            if self.size > 1:
                self.head.next = self.head.next.next
            else:
                self.head.next = None
                self.tail.next = None
        elif index == self.size - 1:
            curr = self.head.next
            for _ in range(index - 1):
                curr = curr.next
            curr.next = None
            self.tail.next = curr
        else:
            curr = self.head.next
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)