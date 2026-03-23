class CircularList:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=[]):
        # Guardamos los elementos en la lista interna
        self._data = list(initial_elements)
    
    # return an str of the collection
    def __str__(self):
        return str(self._data)
    
    # return the length of the elements in the collection
    def __len__(self):
        return len(self._data)
    
    # return the element of the collection in the index position
    def __getitem__(self, index):
        if self.isEmpty():
            raise IndexError("CircularList is empty")
        
        # El truco del % hace que el índice "de la vuelta"
        return self._data[index % len(self._data)]

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
        return element in self._data
    
    # add the element to the end of the collection
    def append(self, element):
        self._data.append(element)

    # insert the element to the desired index of the collection
    def add(self, index, element):
        if not self.isEmpty():
            pos = index % len(self._data)
        else:
            pos = 0
        self._data.insert(pos, element)
    
    # remove an element in the collection by its value
    def remove(self, element):
        if self.isEmpty():
            raise ValueError("CircularList is empty")
        
        if element not in self._data:
            raise ValueError("Element not found")
        
        self._data.remove(element)
    
    # remove and return the element in the collection by its index
    def pop(self, index):
        if self.isEmpty():
            raise IndexError("CircularList is empty")
        
        return self._data.pop(index % len(self._data))
    
    # remove all elements in the collection
    def clear(self):
        self._data.clear()


if __name__ == "__main__":
    
    # 1. Creamos una lista con tres números
    lista = CircularList([1, 2, 3])
    print("Lista inicial:", lista)
    
    # 2. Probamos la circularidad
    print("\n--- Indices circulares ---")
    print("Índice 0:", lista[0])
    print("Índice 1:", lista[1])
    print("Índice 2:", lista[2])
    print("Índice 3:", lista[3])
    print("Índice 4:", lista[4])
    
    # 3. Operaciones
    print("\n--- Operaciones simples ---")
    lista.append(4)
    print("Después de append(4):", lista)
    
    lista.remove(2)
    print("Después de remove(2):", lista)
    
    elemento = lista.pop(0)
    print("Elemento sacado con pop(0):", elemento)
    print("Lista ahora:", lista)
    
    # 4. Vaciar
    lista.clear()
    print("\n¿Está vacía?:", lista.isEmpty())
