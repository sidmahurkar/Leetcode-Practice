class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minn = float('inf') 
        
    def push(self, val: int) -> None:
        
        self.arr.insert(0, val)
        

    def pop(self) -> None:
        
        self.arr.pop(0)
        

    def top(self) -> int:
        
        return self.arr[0]
        

    def getMin(self) -> int:
        
        self.minn = min(self.arr)
        return self.minn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()