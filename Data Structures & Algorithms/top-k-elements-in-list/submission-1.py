class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # lets build a freq map of all the elements

        freq={}
        for num in nums:
            freq[num]=1+freq.get(num,0)

    
        # now we need to offload this onto an array
        arr=[]

        # construct an array of value,count

        for value,count in freq.items():
            arr.append([count,value])

        arr.sort() # we need to sort according to count
        cnt=0
        result=[]
        while cnt<k:
            result.append(arr.pop()[1])
            cnt+=1
        return result







            
        