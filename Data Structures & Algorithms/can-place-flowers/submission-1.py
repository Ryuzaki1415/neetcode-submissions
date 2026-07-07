class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        flowerbed = [0] + flowerbed + [0]
        # we need to count the number of adjacent zeroes
        # once we find the adjacnet zeroes , we need to skip one spot as well
        count=0
        for i in range(1,len(flowerbed)-1):

            if flowerbed[i+1]==0 and flowerbed[i-1]==0 and flowerbed[i]==0:
                # we can plant a flower
                count+=1
                flowerbed[i]=1 # to indicate planted

        if n>count:
            return False
        else:
            return True


        