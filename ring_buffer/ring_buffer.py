class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.arr = []

    def append(self, item):
        self.arr.append(item)
        self.count += 1
        
        

    def get(self):
        storage = []
        for i in range(0, self.count):
            if self.count < self.capacity: 
                self.count -= 1
                # if len(self.arr) > 2:
                #     self.arr.pop(0)
        
                storage.append(self.arr.pop(0))

            else: 
                storage.append(self.arr.pop(self.capacity - self.count))
                self.count -= 1
        print('storage: ', storage)
        return storage