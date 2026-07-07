class Solution:
    def appendCharacters(self, s: str, t: str) -> int:


        sptr=0
        tptr=0


        while sptr<len(s) and tptr<len(t):

            if s[sptr]==t[tptr]:
                sptr+=1
                tptr+=1
            else:
                sptr+=1

        # now at the end of this tptr will say how much of string t is inside s

        return len(t)-tptr
        