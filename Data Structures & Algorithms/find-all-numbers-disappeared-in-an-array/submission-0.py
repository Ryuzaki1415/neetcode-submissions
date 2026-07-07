class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # we have numbers from 1...N
        # we have an array nums which misses some elements
        # we need to find the missed elements.

        # we can mark the ones which are present as negative and then on a second pass identify the ones that are missing.


        for i in range(len(nums)):
            index=abs(nums[i])-1
            # set the index to -ve

            nums[index]=-1*abs(nums[index])


        # second pass
        result=[]
        for index,value in enumerate(nums):

            if value >0:
                result.append(index+1)

        return result



        