class MyQueue:
    def __init__(self):
        self.head = -1
        self.list = []
    def push(self, x: int) -> None:
        self.list.append(x)
        self.head+=1
    def pop(self) -> int:
        self.head-= 1
        return self.list.pop(0)
    def peek(self) -> int:
        return self.list[0]
    def empty(self) -> bool:
        return self.head == -1
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()