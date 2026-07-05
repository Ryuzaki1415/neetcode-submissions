class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # sub arrays which sum to K
        # we need to use prefix sum, since we cannot use a two pointer of sliding window approach because we 
        # could have negative numbers.


        # the idea is to maintain a hashmap of prefix sums.
        # at every point we see if we can remove any subarray with the sum = k-current sum
        # if there is , we just add that to the result


        res=0
        cur_sum=0
        freq={0:1}  # there is a default subarray which sums to 0
        for num in nums:
            cur_sum+=num
            # check if  the differnece is present in the hashmap
            diff=cur_sum-k
            # if this difference is in the frequency, then the target sum can be achieved in 'diff' ways
            # so we add it to the result
            if diff in freq:
                res+=freq[diff]

            freq[cur_sum]=1+freq.get(cur_sum,0)        

        return res