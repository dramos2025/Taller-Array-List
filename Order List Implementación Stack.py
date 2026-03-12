class Stack:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=[]):
        # Guardamos los elementos iniciales en una lista
        # Se hace una copia para evitar modificar la original
        self._data = list(initial_elements)
    
    
    # return an str of the collection
    def __str__(self):
        # Permite imprimir el stack con print()
        return str(self._data)
    
    
    # return the length of the elements in the collection
    def __len__(self):
        # Permite usar len(stack)
        return len(self._data)
    
    
    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return len(self._data) == 0
    
    
    # return the next element in the collection (top of stack)
    def peek(self):
        # Si está vacío no hay elemento que ver
        if self.isEmpty():
            raise IndexError("Stack is empty")
        
        # El último elemento es el que está en la cima
        return self._data[-1]
    
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        # Permite recorrer el stack con un for
        for element in self._data:
            yield element
    
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        # Verifica si el elemento está en el stack
        return element in self._data
    
    
    # add the element to the collection
    def push(self, element):
        # Se agrega al final (top del stack)
        self._data.append(element)
    
    
    # remove and return the next element in the collection
    def pop(self, index=None):
        # En un stack siempre se elimina el último elemento
        if self.isEmpty():
            raise IndexError("Stack is empty")
        
        return self._data.pop()
    
if __name__ == "__main__":
    
    print("=== Creating Stack ===")
    stack = Stack([10, 20, 30])
    
    print("Initial stack:", stack)
    print("Length:", len(stack))
    print("Is empty?:", stack.isEmpty())
    
    print("\n=== Push elements ===")
    stack.push(40)
    print("After push 40:", stack)
    
    stack.push(50)
    print("After push 50:", stack)
    
    print("\n=== Peek ===")
    print("Top element:", stack.peek())
    
    print("\n=== Contains ===")
    print("Is 20 in stack?", 20 in stack)
    print("Is 100 in stack?", 100 in stack)
    
    print("\n=== Iteration ===")
    for element in stack:
        print(element)
    
    print("\n=== Pop ===")
    removed = stack.pop()
    print("Removed element:", removed)
    print("Stack now:", stack)
    
    removed = stack.pop()
    print("Removed element:", removed)
    print("Stack now:", stack)

