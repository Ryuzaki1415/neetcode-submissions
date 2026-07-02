class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        #this opeartion needs to be in-place.
        k=0 # this tracks the number of non val elements.

        for i in range(len(nums)):

            # if the number is val then ignore\
            # if the number is not val then we need to swap i and k

            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k
        