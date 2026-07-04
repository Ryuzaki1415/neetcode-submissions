class Solution:
    import math
    def majorityElement(self, nums: List[int]) -> int:

        freq={}


        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1


        for key,value in freq.items():
            if value>math.floor(len(nums)/2):
                return key

        return -1
        