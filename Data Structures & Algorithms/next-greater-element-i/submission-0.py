class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        # for the brute force, 
        # lets store the positions of the first array
        ans=[-1]*len(nums1)
        hashmap={}
        for i in range(len(nums1)):
            hashmap[nums1[i]]=i

        
        # now that we have the hashmap,
        for i in range(len(nums2)):

            if nums2[i] not in hashmap:
                continue

            else:
                index=hashmap[nums2[i]]

                for j in range(i+1,len(nums2)):
                    if nums2[j]>nums2[i]:
                        # we have found the next greatest element
                        ans[index]=nums2[j]
                        break

        return ans


