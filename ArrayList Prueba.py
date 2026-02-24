class ArrayList:
    
    # size: initial capacity of the collection
    # initial_elements: allow the collection to start with some elements
    def __init__(self, size=100, initial_elements=None):
        if initial_elements is None:
            initial_elements = []
            
        self.capacity = max(size, len(initial_elements))
        self.data = [None] * self.capacity
        self.count = 0
        
        for element in initial_elements:
            self.append(element)
    
    
    # return an str of the collection
    def __str__(self):
        elements = [str(self.data[i]) for i in range(self.count)]
        return "[" + ", ".join(elements) + "]"
    
    
    # return the length of the elements in the collection
    def __len__(self):
        return self.count
    
    
    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return self.count == 0
    
    
    # return the element of the collection in the index position
    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        return self.data[index]
    
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        for i in range(self.count):
            yield self.data[i]
    
    
    # return a boolean value representing the existence of an element
    def __contains__(self, element):
        for i in range(self.count):
            if self.data[i] == element:
                return True
        return False
    
    
    # internal method to resize the array when full
    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        
        for i in range(self.count):
            new_data[i] = self.data[i]
        
        self.data = new_data
    
    
    # add the element to the end of the collection
    def append(self, element):
        if self.count == self.capacity:
            self._resize()
        
        self.data[self.count] = element
        self.count += 1
    
    
    # add the element at the requested index
    def insert(self, index, element):
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        
        if self.count == self.capacity:
            self._resize()
        
        for i in range(self.count, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = element
        self.count += 1
    
    
    # remove an element by value
    def remove(self, element):
        for i in range(self.count):
            if self.data[i] == element:
                for j in range(i, self.count - 1):
                    self.data[j] = self.data[j + 1]
                
                self.data[self.count - 1] = None
                self.count -= 1
                return
        
        raise ValueError("Element not found")
    
    
    # remove and return the element by index
    def pop(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        
        element = self.data[index]
        
        for i in range(index, self.count - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.count - 1] = None
        self.count -= 1
        
        return element
    
    
    # remove all elements in the collection
    def clear(self):
        self.data = [None] * self.capacity
        self.count = 0

if __name__ == "__main__":
    
    print("=== CREANDO ARRAYLIST ===")
    lista = ArrayList(size=5, initial_elements=[10, 20, 30])
    print("Lista inicial:", lista)
    print("Longitud:", len(lista))
    print("¿Está vacía?:", lista.isEmpty())
    
    print("\n=== APPEND ===")
    lista.append(40)
    lista.append(50)
    print("Después de append:", lista)
    
    print("\n=== INSERT ===")
    lista.insert(2, 25)
    print("Insertando 25 en posición 2:", lista)
    
    print("\n=== GET ITEM ===")
    print("Elemento en índice 3:", lista[3])
    
    print("\n=== CONTAINS ===")
    print("¿Existe 30?:", 30 in lista)
    print("¿Existe 99?:", 99 in lista)
    
    print("\n=== ITERACIÓN (FOR) ===")
    for elemento in lista:
        print(elemento)
    
    print("\n=== REMOVE ===")
    lista.remove(25)
    print("Después de eliminar 25:", lista)
    
    print("\n=== POP ===")
    eliminado = lista.pop(2)
    print("Elemento eliminado en índice 2:", eliminado)
    print("Lista actual:", lista)
    
    print("\n=== CLEAR ===")
    lista.clear()
    print("Después de clear:", lista)
    print("Longitud final:", len(lista))