class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:



        my_stack=[] #contains (val,index)

        result=[0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            # if the current temp is lesser than the top of the stack, just append 
            if not my_stack:
                my_stack.append((temperatures[i],i))
            elif my_stack[-1][0]>temperatures[i]:
                my_stack.append((temperatures[i],i))
            else:
                while my_stack and temperatures[i]>my_stack[-1][0]:
                    element,index=my_stack.pop()
                    result[index]=i-index
                my_stack.append((temperatures[i],i))

        return result



        