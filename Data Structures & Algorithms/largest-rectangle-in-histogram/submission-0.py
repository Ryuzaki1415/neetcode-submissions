class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        maxArea=0
        stack=[] # stores (index,height)
        for index,height in enumerate(heights):

            start_index=index

            # while the top of the stack is greater than the current element
            while stack and stack[-1][1]>height:
                # we need to pop
                pop_index,pop_height=stack.pop()

                # now calculate the area of the rectangle formed
                maxArea=max(maxArea,pop_height*(index-pop_index))

                # now we can extend it backwards
                start_index=pop_index

            # append the element
            stack.append((start_index,height))


        # now after this there are still elements
        for index,height in stack:
            maxArea=max(maxArea,height*(len(heights)-index))

        return maxArea















        