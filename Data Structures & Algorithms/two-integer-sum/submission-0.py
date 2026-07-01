class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # we have an array of nums
        # we have a target
        # the main idea is to find A+B=target
        # now whenever we see A , we compute its complimenet and keep in hashmap


        hashmap={}# stores element -> index

        for i  in range(len(nums)):

            diff=target-nums[i]
            # if we have already seen this diff before, then we have the pair

            if diff in hashmap:
                return [hashmap[diff],i]
            
            else:
                hashmap[nums[i]]=i
        
        return []
        