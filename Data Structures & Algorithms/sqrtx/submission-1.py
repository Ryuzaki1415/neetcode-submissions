class Solution:
    def mySqrt(self, x: int) -> int:

        # we are given a number x
        # we need to find the square root of x
        # the search space is between 0 and n//2\
        # also edge case of 0 and 1

        if x==0 or x==1:
            return x

        
        left=0
        right=x//2
        ans=0
        while left<=right:
            mid=(left+right)//2

            square=mid*mid

            if square>x:
                right=mid-1
            elif square<x:
                ans=mid
                left=mid+1
            else:
                return mid
        return ans

        