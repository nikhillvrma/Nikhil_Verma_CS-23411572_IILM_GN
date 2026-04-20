class MinHeap:
    def __init__(self):
        self.arr = []
        self.count = 0
        
    def heapifyUp(self, arr, ind):
        if ind == 0:
            return
        parent = (ind - 1) // 2
        if arr[parent] > arr[ind]:
            arr[parent], arr[ind] = arr[ind], arr[parent]
            self.heapifyUp(arr, parent)
        
    def initializeHeap(self):
        self.arr.clear()
        self.count = 0
        
    def insert(self, key):
        self.arr.append(key)
        self.heapifyUp(self.arr, self.count)
        self.count += 1
    
    def main(self):
        self.initializeHeap()
        self.insert(3)
        self.insert(2)
        self.insert(1)
        self.insert(5)
        self.insert(4)
        print(self.arr)
if __name__ == "__main__":    
    sol = MinHeap()
    sol.main()