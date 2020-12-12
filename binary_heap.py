import random

class BinaryHeap:
    
    def __init__(self):
        self.heap = list()

    def parent(self, k):
        return (k-1)//2

    def left(self, k):
        return 2*k+1
    
    def right(self, k):
        return 2*k+2
    
    def up_heap(self, k):
        while (k != 0 and self.heap[self.parent(k)] > self.heap[k]):
            self.heap[k], self.heap[self.parent(k)] = self.heap[self.parent(k)], self.heap[k]
            k = self.parent(k)

    def down_heap(self, k):
        while (self.left(k) < len(self.heap)):
            j = self.left(k)
            if j+1<len(self.heap) and self.heap[j+1]<self.heap[j]:
                j = j+1
            if self.heap[k]<self.heap[j]:
                break
            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            k = j

    def top(self):
        return self.heap[0]

    def pop(self):
        root = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop(len(self.heap)-1)
        self.down_heap(0)
        return root


    def push(self, value):
        self.heap.append(value)
        self.up_heap(len(self.heap)-1)

    def print_heap(self):
        i = 0
        j = 0
        row = str() 
        for element in self.heap:
            row += '{:6}'.format(str(element))
            row += " "
            i+=1
            if i is pow(2, j):
                print(row)
                row = str()
                i=0
                j+=1
        print(row)

def return_test_list(j):
    test_list = [None]*j
    for i in range(j):
        test_list[i] = random.randint(1, 30000)
    return test_list



if __name__ == "__main__":
    
    tree = BinaryHeap()
    test_list = return_test_list(15)
    for num in test_list:
        tree.push(num)
    
    tree.print_heap()
    print(tree.pop())

