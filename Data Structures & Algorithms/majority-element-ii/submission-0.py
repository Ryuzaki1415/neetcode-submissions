from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # find an element which appears more than n/3 times.
        # ie the element would always take up 30% of the array
        hashmap={}


        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1

        # now that we have the freqmap

        # lets go thru the keys and find which key has values more than n//3 times
        N=floor(len(nums)//3)

        res=[]
        for number, count in hashmap.items():

            if count>N:
                res.append(number)

        return res
