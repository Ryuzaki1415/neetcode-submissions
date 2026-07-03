class Solution:


    def Find_Time(self,weights,capacity)->int:
        days=1

        current_load=0

        for weight in weights:
            if current_load+weight>capacity:
                days+=1
                current_load=weight
            else:
                current_load+=weight
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:


        left=max(weights)
        right=sum(weights)

        mincap=float("inf")
        while left<=right:

            capacity=(left+right)//2

            time_taken=self.Find_Time(weights,capacity)

            if time_taken<=days:

                mincap=min(mincap,capacity)
                right=capacity-1
            else:
                left=capacity+1

        return mincap


        