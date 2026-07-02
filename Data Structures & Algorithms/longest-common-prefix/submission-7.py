class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we need to find the longest commmon prefix
        # lets consider the first word as the prefix
        for i in range(len(strs[0])):
            char=strs[0][i] # current character that we are considering
            # loop thru all the words
            for string in strs[1:]:
                # check if corresponding characters are same
                if i>=len(string) or string[i]!=char:
                    return strs[0][:i] # return the prefix so far

        return strs[0]


        