class Solution:
    def maxDifference(self, s: str) -> int:


        # lets have a hashmap tracking the frequencies


        hashmap={}

        for char in s:
            hashmap[char]=1+hashmap.get(char,0)
        
        # now that we have the frequencies, we can find the odd and the even ones

        oddmax=float("-inf")
        evenmin=float("inf")
        for value in hashmap.values():

            if value%2==0:
                # check for even min
                evenmin=min(evenmin,value)
            else:
                oddmax=max(oddmax,value)

        return oddmax-evenmin






        