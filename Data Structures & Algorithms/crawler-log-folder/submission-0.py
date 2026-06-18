class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack=[]


        for log in logs:

            if log =="../":
                # come back one step

                if stack:
                    stack.pop()
            
            elif log=="./":
                pass
            
            else:
                stack.append(log)

        return len(stack)

        