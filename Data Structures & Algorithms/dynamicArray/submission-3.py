class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity #how much can the array hold initialized
        self.length = 0 #count actual elements by default
        self.arr = [0] * self.capacity #fixed-size underlying with 0s as placeholders
            

    def get(self, i: int) -> int:
        return self.arr[i] #value at index i

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n #takes value of n and stores it at pos[i] in the array
        #left is the destination
        #right is the source for assignment

    def pushback(self, n: int) -> None:
        if self.length == self.capacity: #if the length reaches the capacity, no room left
            self.resize() #therefore we call resize
        self.arr[self.length] = n #this puts n at the first unused slot
        #self length always points to the next available slot
        self.length += 1 #because u just added an element

    def popback(self) -> int:
        if self.length > 0:
            #soft del last element
            self.length -= 1 #taking one from the index to move back
        
        return self.arr[self.length] #points to last element

    def resize(self) -> None:
        self.capacity = 2 * self.capacity #doubles capacity
        newArr = [0] * self.capacity #creates a new arr with placeholder 0s
        
        for i in range(self.length):
            newArr[i] = self.arr[i] #copies elements
        self.arr = newArr #point to new arr

    def getSize(self) -> int:
        return self.length 

    
    def getCapacity(self) -> int:
        return self.capacity