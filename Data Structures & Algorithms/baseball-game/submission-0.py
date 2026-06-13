class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack=[]

        for op in operations:

            if op =="+":
                top1=stack[-1]
                top2=stack[-2]
                result = top1+top2
                stack.append(result)
            elif op=="D":
                top=stack[-1]
                stack.append(top*2)
            
            elif op=="C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
        