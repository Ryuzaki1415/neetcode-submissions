class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # we have two string words 1  and word 2,
        # we need to create a new string by alternatively merging the word1 and word2.


        ans=""

        i=0
        j=0

        while i<len(word1) and j<len(word2):
            
            ans+=word1[i]+word2[j]
            i+=1
            j+=1
            
        # cleanup
        while i<len(word1):
            ans+=word1[i]
            i+=1

        while j<len(word2):
            ans+=word2[j]
            j+=1


        return ans

        