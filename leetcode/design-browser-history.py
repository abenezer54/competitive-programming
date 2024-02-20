class Node:
    def __init__(self, url = "", next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage, None, None)
        self.ptr = self.head

    def visit(self, url: str) -> None:
        node = Node(url, None, self.ptr)
        self.ptr.next = node
        self.ptr = node

    def back(self, steps: int) -> str:
        while self.ptr.prev and steps:
            self.ptr = self.ptr.prev
            steps -= 1
        return self.ptr.url 
        
    def forward(self, steps: int) -> str:
        while self.ptr.next and steps:
            self.ptr = self.ptr.next
            steps -= 1
        return self.ptr.url
 

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)