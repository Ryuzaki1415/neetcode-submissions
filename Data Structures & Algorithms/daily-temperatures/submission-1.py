class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        # THIS IS A MONOTONIC STACK PROBLEM
        # TEMP[I] REPRESENTS THE TEMPERATURE OF THAT DAY.
        # OKAY SO THE    default temperature is0


        result=[0]*len(temperatures)
        # we neeed to find the number of days before a warmer day comes along
        stack=[] #value,index

        for i in range(len(temperatures)):

            # if the incoming temp is less than the top of the stack, then we append
            while stack and stack[-1][0]<temperatures[i]:
                # we need to pop all the lesser temps
                value,index=stack.pop()
                # day difference would be the difference of indexes right
                diff=i-index
                # save in result
                result[index]=diff

            stack.append((temperatures[i],i))

        return result

        