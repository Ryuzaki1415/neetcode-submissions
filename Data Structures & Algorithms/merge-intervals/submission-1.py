class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # the main thing we need to understand here is that we need to sort the intervals according to the starting index.

        intervals.sort(key=lambda x : x[0]) # or intervals.sort() works as well.

        output=[intervals[0]] # contains the first interval

        for interval in intervals[1:]: # starting from the second interval
            #current interval
            start_idx=interval[0]
            end_idx=interval[1]

            # lets take the ending index of the previous one
            prev_end=output[-1][1]

            # if the new interval is lesser than the prev end then we need to merge

            if start_idx<=prev_end:
                # merge
                output[-1][1]=max(prev_end,end_idx)
            else:
                # else we dont need to merge 
                output.append([start_idx,end_idx])

        return output



        