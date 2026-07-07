class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


        #if we see a 1, apppend  
        # if we see a 0 reset and update max
        count=0
        maxc=0
        for num in nums:
            if num==1:
                count+=1
            else:
                maxc=max(maxc, count)
                count=0

        maxc=max(count,maxc)
        return maxc
