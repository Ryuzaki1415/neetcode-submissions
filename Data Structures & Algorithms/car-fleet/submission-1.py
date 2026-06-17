class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # we need to process the cars in a sorted order.
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            time_taken = (target - pos) / spd
            stack.append(time_taken)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)