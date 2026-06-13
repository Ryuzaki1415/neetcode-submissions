class Node:
    def __init__(self,val,next,prev):
        self.val=val
        self.next=next
        self.prev=prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space=k
        self.left=Node(0,None,None)
        self.right=Node(0,None,self.left)
        self.left.next=self.right

        

    def enQueue(self, value: int) -> bool:

        # to enqueue we need to check if the queue is full

        if self.isFull():
            return False
        # insert a node at 

        #left elm1  newnode right

        new_node=Node(value,self.right,self.right.prev)        
        # reset links

        self.right.prev.next=new_node
        self.right.prev=new_node
        self.space-=1

        return True


    def deQueue(self) -> bool:

        # to dequeue, we need a non-empty LL

        if self.isEmpty():
            return False
        
        # dequeue an element at the left position

        #left elm1 elm2 right

        self.left.next=self.left.next.next
        self.left.next.prev=self.left
        self.space+=1
        return True
        

    def Front(self) -> int:
        # return the element at the front of the array
        # check if there is any element 
        if self.isEmpty():
            return -1
        
        return self.left.next.val
        

    def Rear(self) -> int:

        # check if there is any element
        if self.isEmpty():
            return -1

        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        # the queue is empty if self.left's right neighbour is self.right
        if self.left.next==self.right:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        # the queue is full when we dont have any space
        if self.space==0:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()