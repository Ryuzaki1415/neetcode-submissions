class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left



    def insert(self,node:Node):
        #insertion at the rear
        previous=self.right.prev
        next=self.right

        previous.next=node
        next.prev=node
        node.next=next
        node.prev=previous


    def remove(self,node:Node):
        # to remove store the prev and the next
        previous=node.prev
        next_node=node.next
        previous.next=next_node
        next_node.prev=previous

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        newnode=Node(key,value)
        self.cache[key]=newnode
        self.insert(newnode)

        # check for capacity

        if len(self.cache)>self.capacity:
            #remove the LRU
            LRU=self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]

        
