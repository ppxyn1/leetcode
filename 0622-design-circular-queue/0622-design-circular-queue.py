class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k #k : queue size
        self.maxlen = k
        self.p1 = 0 #front pointer
        self.p2 = 0 #rear pointer

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None: # rear pointer위치가 None이 아니라 다른 요소가 있는 공간이 꽉찬 상태이므로 False return
            self.q[self.p2] = value #rear pointer p2위치에 값을 넣고
            self.p2 = (self.p2+1)%self.maxlen  #pointer를 앞으로 한칸 이동
            return True

    def deQueue(self) -> bool:
        if self.q[self.p1] is None: 
            return False
        else:
            self.q[self.p1] = None #프론트포인터 p1위치에 None을 넣어 삭제하고
            self.p1 = (self.p1+1)%self.maxlen #포인터를 한칸 앞으로 이동 , 최대 길일를 넘지 않도록..
            return True

    def Front(self) -> int:
        if self.q[self.p1] is None: 
            return -1
        else: 
            return self.q[self.p1]

    def Rear(self) -> int:
        if self.q[self.p2-1] is None: 
            return -1 
        else:
            return self.q[self.p2-1]

    def isEmpty(self) -> bool:
        if self.p1 == self.p2 and self.q[self.p1] is None:
            return True

    def isFull(self) -> bool:
        if self.p1 == self.p2 and self.q[self.p1] is not None:
            return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()