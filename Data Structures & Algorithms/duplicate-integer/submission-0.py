class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # contains duplicate
        # we need to keep count of the elements and check if counts are same
        # we can keep  a visited as well


        visited=set()

        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)

        return False

         