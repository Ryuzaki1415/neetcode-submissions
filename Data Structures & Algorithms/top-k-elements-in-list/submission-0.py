class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        freq={}


        for num in nums:
            freq[num]=1+freq.get(num,0)

        # we have a freq map of all the elements.
        # we need to offload this into an array

        arr=[]
        for num,count in freq.items():
            arr.append([count,num])
        

        arr.sort()  #sorted according to the count

        # pop the k most common digits

        count=0
        result=[]
        while count<k:
            result.append(arr.pop()[1])
            count+=1

        return result
            


        



      