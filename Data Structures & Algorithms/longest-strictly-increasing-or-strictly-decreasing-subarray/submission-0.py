class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:


        inc_state=1
        dec_state=1
        res=1


        for i in range(1,len(nums)):

            # check if strictly increasing

            if nums[i]>nums[i-1]:
                inc_state+=1
                dec_state=1
            
            elif nums[i]<nums[i-1]:
                dec_state+=1
                inc_state=1
            else:
                dec_state=1
                inc_state=1
            
            # calculate the current longest
            res=max(inc_state,dec_state,res)

        return res
        