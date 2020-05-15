import time
from queue import Queue
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#the implementations above is O(n^2)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.dup = []
    def insert(self, value):
   
        # print('value: ', self.value)
        # if value == self.value: 
        #     self.dup.append(value)
        if value < self.value:
            if self.left is None:  
                Node = BSTNode(value)
                self.left= Node             
            else:
                return self.left.insert(value)         
        else:    
            if not self.right: 
                Node = BSTNode(value)
                self.right = Node
            else:     
                return self.right.insert(value)
    def dft_print(self, node):
            qq = Queue()
            qq.enqueue(node)

            while qq.__len__() > 0:
                
                current = qq.dequeue()
                if current.left:
                    qq.enqueue(current.left)
                if current.right:
                    qq.enqueue(current.right)
                print(current.value)
                return current.value

bst = BSTNode(names_1[50])
for i in names_1: 
    bst.insert(i)
for i in names_2:
    bst.insert(i)
duplicates.append(bst.dft_print(bst))
    
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
