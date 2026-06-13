class MyQueue:

    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]

        

    def push(self, x: int) -> None:

        # for push, push to push stack

        self.push_stack.append(x)
        

    def pop(self) -> int:

        # for pop operation, if we have value in pop stack, pop it else populate values from push stack

        if len(self.pop_stack)!=0:
            return self.pop_stack.pop()
        else:
            if len(self.push_stack)>0:
                while self.push_stack:
                    self.pop_stack.append(self.push_stack.pop())
                return self.pop_stack.pop()
            else:
                return False     

    def peek(self) -> int:
        if len(self.pop_stack)!=0:
            return self.pop_stack[-1]
        
        else:
             while self.push_stack:
                    self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

            
        
        

    def empty(self) -> bool:

        if len(self.pop_stack)==0 and len(self.push_stack)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()