class StockSpanner:

    def __init__(self):
        self.stack=[] # stores (value,span)
        

    def next(self, price: int) -> int:
        # we just have the current price.
        # we have a stack with prices lower than the current one. monotonic increasing stack

        span=1
        while self.stack and self.stack[-1][0]<=price:
            # start with span=1
            # whenever we pop elements, we add to the span
            value,cur_span=self.stack.pop()
            span+=cur_span

        self.stack.append((price,span))
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)