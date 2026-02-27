class OrderList:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=[]):
        # Creamos una copia ordenada para mantener el invariante
        self._data = sorted(initial_elements)
    
    
    # return an str of the collection
    def __str__(self):
        return str(self._data)
    
    
    # return the length of the elements in the collection
    def __len__(self):
        return len(self._data)
    
    
    # return the element of the collection in the index position
    # Error: the index dont exist
    def __getitem__(self, index):
        if self.isEmpty():
            raise IndexError("The list is empty")
        
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range")
        
        return self._data[index]


    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return len(self._data) == 0
    
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        for element in self._data:
            yield element
    
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        if self.isEmpty():
            return False
        
        # búsqueda binaria simple
        left = 0
        right = len(self._data) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self._data[mid] == element:
                return True
            elif self._data[mid] < element:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    
    # add the element keeping the order
    def add(self, element):
        # Insertar manteniendo orden (búsqueda lineal simple estilo académico)
        position = 0
        
        while position < len(self._data) and self._data[position] < element:
            position += 1
        
        self._data.insert(position, element)
    
    
    # remove an element in the collection by its value
    # Error: the element dont exist in the collection
    def remove(self, element):
        if self.isEmpty():
            raise ValueError("The list is empty")
        
        if element not in self:
            raise ValueError("Element not found")
        
        index = 0
        while index < len(self._data):
            if self._data[index] == element:
                self._data.pop(index)
                return
            index += 1
    
    
    # remove and return the element in the collection by its index
    def pop(self, index):
        if self.isEmpty():
            raise IndexError("The list is empty")
        
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range")
        
        return self._data.pop(index)
    
    
    # remove all elements in the collection
    def clear(self):
        self._data.clear()

if __name__ == "__main__":
    
    print("=== Creating OrderList ===")
    order_list = OrderList([30, 10, 20, 60])
    
    print("Initial list (ordered automatically):", order_list)
    print("Length:", len(order_list))
    print("Is empty?:", order_list.isEmpty())
    
    print("\n=== Adding elements ===")
    order_list.add(40)
    print("After adding 40:", order_list)
    
    order_list.add(5)
    print("After adding 5:", order_list)
    
    order_list.add(70)
    print("After adding 70:", order_list)
    
    print("\n=== Access by index ===")
    print("Element at index 2:", order_list[2])
    
    print("\n=== Searching elements ===")
    print("Is 20 in the list?", 20 in order_list)
    print("Is 100 in the list?", 100 in order_list)
    
    print("\n=== Iterating with for ===")
    for element in order_list:
        print(element)
    
    print("\n=== Removing element by value ===")
    order_list.remove(20)
    print("After removing 20:", order_list)
    
    print("\n=== Pop by index ===")
    removed = order_list.pop(1)
    print("Removed element at index 1:", removed)
    print("Current list:", order_list)
    
    print("\n=== Clearing list ===")
    order_list.clear()
    print("After clear:", order_list)
    print("Is empty now?:", order_list.isEmpty())
    
