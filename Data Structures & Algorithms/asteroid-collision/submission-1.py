class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        stack=[]
        diff=0
        for  current_asteroid in asteroids:
            while stack and stack[-1]>0 and current_asteroid<0:

                diff=current_asteroid+stack[-1]

                if diff>0:
                    current_asteroid=0
                
                if  diff==0:
                    stack.pop()
                    current_asteroid=0
                
                if diff<0:
                    stack.pop()
            
            if current_asteroid:
                stack.append(current_asteroid)
        return stack
            
        