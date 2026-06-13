class MinStack:

    def __init__(self):
        self.mystack=[] #contains a tuple (element,min_elementsofar)
        self.min_stack=[]
        
    def push(self, val: int) -> None:
        # when we push, we need to push the min element so far to the min stack
        self.mystack.append(val)
        if self.min_stack:
            minval=min(self.min_stack[-1],val)
            self.min_stack.append(minval)
        else:
            self.min_stack.append(val)
    def pop(self) -> None:

        # pop from both stacks
        self.mystack.pop()
        self.min_stack.pop()
    def top(self) -> int:
        return self.mystack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
        
