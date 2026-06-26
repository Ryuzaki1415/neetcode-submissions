from math import ceil
class Solution:


    def find_time(self,piles,rate):
        total=0
        for  pile in piles:
            total+=ceil(pile/rate)
        return total


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we need to find the optimal eating rate.
        left=1
        right=max(piles)
        best_rate=float("inf")
        while left<=right:
            rate=(left+right)//2
            # we need to check if this rate satisfies the time constraint.
            time_taken=self.find_time(piles,rate)
            if time_taken<=h:
                # its a valid  time but lets see if we can find better
                best_rate=min(best_rate,rate)
                # lets  shrink
                right=rate-1
            else:
                left=rate+1

        return best_rate

            

        