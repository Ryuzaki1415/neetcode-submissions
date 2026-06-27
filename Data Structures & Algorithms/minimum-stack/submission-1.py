class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        # we have the current value.
        # we need to push the current element to the stack and push the min value to the minstack

        self.stack.append(val)
        if self.min_stack:
            min_element=min(val,self.min_stack[-1])
            self.min_stack.append(min_element)
        else:
            self.min_stack.append(val)
    def pop(self) -> None:

        self.stack.pop()
        self.min_stack.pop()
    

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        










