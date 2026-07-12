class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        ans=[]

        freq={}

        for string in arr:
            if string in freq:
                freq[string]+=1
            else:
                freq[string]=1

        for key,value in freq.items():

            if value==1:
                ans.append(key)

        if k>len(ans):
            return ""
        else:
            return ans[k-1]

            
        