class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:



        # for two asteroids to meet they must be opposite in sign
        # when they meet the smaller one is destroyed



        stack=[]

        # we need to check for collision, if the stack is non empty, the asteroid is negative  and the top of the stack is poisitve

        for asteroid in asteroids:
            while stack and asteroid<0 and stack[-1]>0:

                # see who wins
                diff=asteroid+stack[-1]
                if diff<0:
                    # the new asteroid won
                    stack.pop()
                elif diff>0:
                    asteroid=0
                else:
                    # if both are same , both get destroyed
                    stack.pop()
                    asteroid=0

            if asteroid:
                stack.append(asteroid)

        return stack
        




        