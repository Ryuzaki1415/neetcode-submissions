class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        """
        We have 2 pointers, one each for each string
        What is our end condition?
        When the string s is completely present inside the string t, then p1 will have length same as len of t

        """


        p1=0
        p2=0
        if not s:
            return True

        while p1<len(s) and p2<len(t):

            if s[p1]==t[p2]:
                p1+=1
                p2+=1
            else:
                p2+=1
            
            if p1==len(s):
                return True

        return False