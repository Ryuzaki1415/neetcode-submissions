class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr,LEFT,MID,RIGHT):
            # we basically need to merge the left and right halves of the array
            left_subarray=arr[LEFT:MID+1]
            right_subarray=arr[MID+1:RIGHT+1]

            i,j,k=LEFT,0,0  # i to track the og array j to track the left subarray and K for the right subarray

            while j<len(left_subarray) and k<len(right_subarray):
                # check which is smaller

                if left_subarray[j]<=right_subarray[k]:
                    # set it as the ith element and incremet j and i
                    arr[i]=left_subarray[j]
                    j+=1
                else:
                    arr[i]=right_subarray[k]
                    k+=1
                i+=1

            # after this while loop there may still be elements in either subarrays
            while j<len(left_subarray):
                arr[i]=left_subarray[j]
                j+=1
                i+=1

            while k<len(right_subarray):
                arr[i]=right_subarray[k]
                k+=1
                i+=1




        # for n log n time we need a quick sort or merge sort.
        def mergeSort(arr,l,r):
            # base case is when the array has len 1  ie when left==right pointer
            if l==r:
                return arr
            
            # else we need to divide the left half and the right half
            # compute the middel

            mid=(l+r)//2

            mergeSort(arr,l,mid) # no overlap between left and right halves.
            mergeSort(arr,mid+1,r)

            # now we need to merge it
            merge(arr,l,mid,r)

            return arr

        return mergeSort(nums,0,len(nums)-1)


        