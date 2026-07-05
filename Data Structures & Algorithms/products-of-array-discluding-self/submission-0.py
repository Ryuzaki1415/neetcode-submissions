class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix_arr=[1]*len(nums)
        postfix_arr=[1]*len(nums)

        # build the prefix array

        for i in range(1,len(nums)):
            prefix_arr[i]=prefix_arr[i-1]*nums[i-1]

        # build postfix array
        # start from the second_last_element
        for i in range(len(nums)-2,-1,-1): 
            postfix_arr[i]=postfix_arr[i+1]*nums[i+1]

        
        result=[]

        for i in range(len(nums)):
            result.append(prefix_arr[i]*postfix_arr[i])

        return result

        