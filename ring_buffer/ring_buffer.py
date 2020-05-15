class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []

    class _Full:
        """ class that implements a full buffer """
        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.arr[self.cur] = x
            self.cur = (self.cur+1) % self.capacity
        def get(self):
            """ return list of elements in correct order """
            return self.arr[:self.cur] + self.arr[self.cur:]

    def append(self,x):
        """append an element at the end of the buffer"""
        self.arr.append(x)
        if len(self.arr) >= self.capacity:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self._Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.arr


    # def get(self):
        # storage = []
        # head = (self.count + self.capacity) % self.capacity
        # print('head', head)
        # full = []
        # end_game = []
        # for i in range(0, self.count):
        #     if self.count < self.capacity: 
        #         self.count -= 1
        #         # if len(self.arr) > 2:
        #         #     self.arr.pop(0)
        
        #         storage.append(self.arr.pop(0))
                
        #     else: 
        #         popped = self.arr.pop(self.capacity - self.count)
        #         storage.append(popped)
        #         full.append(popped)
        #         self.count -= 1
        # full = full[(head - self.count):(head - self.count)+1]
        # storage2 = storage[head+1:]
        # end_game = full + storage2
        # print('storage: ', storage, 'full', full)
        # # return storage[:self.capacity]
        # return end_game