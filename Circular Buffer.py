class CircularBuffer:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, capacity=5):
        # Capacidad fija del buffer
        self._capacity = capacity
        
        # Lista inicial con espacios vacíos
        self._data = [None] * capacity
        
        # Índices y tamaño
        self._size = 0
        self._front = 0
        self._rear = 0
    
    # return an str of the collection
    def __str__(self):
        elements = []
        i = self._front
        
        for _ in range(self._size):
            elements.append(self._data[i])
            i = (i + 1) % self._capacity
        
        return str(elements)
    
    # return the length of the elements in the collection
    def __len__(self):
        return self._size
    
    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return self._size == 0
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        i = self._front
        
        for _ in range(self._size):
            yield self._data[i]
            i = (i + 1) % self._capacity
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        if self.isEmpty():
            return False
        
        for item in self:
            if item == element:
                return True
        return False
    
    # add the element to the end of the collection
    # ERROR: if the collection is full before adding a new element
    def push(self, element):
        if self._size == self._capacity:
            raise OverflowError("CircularBuffer is full")
        
        self._data[self._rear] = element
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
    
    # remove and return the next element in the collection
    # ERROR: if the collection is empty 
    def pop(self, index=None):
        if self.isEmpty():
            raise IndexError("CircularBuffer is empty")
        
        element = self._data[self._front]
        self._data[self._front] = None
        
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        
        return element
    
    # remove all elements in the collection
    def clear(self):
        self._data = [None] * self._capacity
        self._size = 0
        self._front = 0
        self._rear = 0

if __name__ == "__main__":
    
    print("=== Creating CircularBuffer ===")
    buffer = CircularBuffer(3)
    
    print("Is empty?:", buffer.isEmpty())
    
    print("\n=== Push ===")
    buffer.push(10)
    buffer.push(20)
    buffer.push(30)
    print("Buffer:", buffer)
    
    print("\n=== Pop ===")
    print("Removed:", buffer.pop())
    print("Buffer:", buffer)
    
    print("\n=== Push again ===")
    buffer.push(40)
    print("Buffer:", buffer)
    
    print("\n=== Contains ===")
    print("20 in buffer?", 20 in buffer)
    print("99 in buffer?", 99 in buffer)
    
    print("\n=== Iteration ===")
    for x in buffer:
        print(x)
    
    print("\n=== Clear ===")
    buffer.clear()
    print("Buffer:", buffer)
    print("Is empty?:", buffer.isEmpty())
    