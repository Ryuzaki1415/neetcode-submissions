class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:




        # okay so to insert a new interval there are multiple cases.

        # first case is where the new interval is before the first element

        res=[]

        for i in range(len(intervals)):

            # the new interval ends before the first one
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            
            # if our new interval appears after then we just add the current one to the res and move on
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])

            else:
                # now we could overlap
                newInterval[0]=min(newInterval[0],intervals[i][0])
                newInterval[1]=max(newInterval[1],intervals[i][1])

                # we are still not adding to the res because we could still merge with some others.

        # after the loop lets add it to the result  
        res.append(newInterval)


        return res



        