class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        cur_sum=0
        left=0
        res=float("inf")
        for right in range(len(nums)):

            cur_sum+=nums[right]

            # if the current sum is greater than or equal to target we compute the length
            while cur_sum>=target:
                # current window length
                res=min(res,right-left+1)
                # now  update the left ptr
                # before that remember to subtract left from current sum
                cur_sum-=nums[left]
                left+=1

        if res ==float("inf"):
            return 0
        else:
            return res


        