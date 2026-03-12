class Queue:
    
    # initial_elements inicia la cola
    def __init__(self, initial_elements=[]):
        # Guarda los elementos
        # list() crea una copia 
        self._data = list(initial_elements)
    
    def __str__(self):
        return str(self._data)
    
    def __len__(self):
        return len(self._data)
    
    
    # Si esta vacia da true, si no false
    def isEmpty(self):
        return len(self._data) == 0
    
    
    # Devuelve el siguiente elemento de la cola
    def peek(self):
        # Si la cola está vacía no hay elemento que devuelva
        if self.isEmpty():
            raise IndexError("The queue is empty")
        
        return self._data[0]
    
    
    # Permite recorrer la cola con un ciclo for
    def __iter__(self):
        # iter() crea y retorna un iterador de la lista
        return iter(self._data)
    
    # Verifica la existencia del elemento
    # Permite usar queue
    def __contains__(self, element):
        # Recorre la cola
        for e in self._data:
            # Si se encuentra es true
            if e == element:
                return True
        
        # Si no se encontro
        return False
    
    
    # Agrega un elemento al final de la cola
    # Nuevos elementos al final
    def push(self, element):
        self._data.append(element)
    
    
    # Elimina y retorna el primer elemento de la cola
    def pop(self):
        # No elimina nada porque esta vacia
        if self.isEmpty():
            raise IndexError("The queue is empty")
        
        # Elimina el primer elemento
        # y lo retorna
        return self._data.pop(0)
if __name__ == "__main__":
    
    queue = Queue([10, 20, 30])
    
    print("Cola inicial: ", queue)
    
    print("Cantiadad: ", len(queue))
    
    print("Siguiente: ", queue.peek())
    
    print("\nAñadiendo")
    queue.push(40)
    queue.push(50)
    print(queue)
    
    print("\nIterando")
    for element in queue:
        print(element)
    
    print("\nBuscando")
    print(20 in queue)
    print(100 in queue)
    
    print("\nQuitando elementos")
    print("Eliminado:", queue.pop())
    print("Cola:", queue)