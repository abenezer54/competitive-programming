class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0
        self.k = k     

    def enQueue(self, value: int) -> bool:
        
        if not self.isFull():
            self.rear += 1
            self.queue[self.rear % self.k] = value 
            self.size += 1
            return True
        return False     

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front += 1
            self.size -= 1
            return True
        return False
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front % self.k]      

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear ) % self.k]
        
    def isEmpty(self) -> bool: return not self.size

    def isFull(self) -> bool: return self.size == len(self.queue)
