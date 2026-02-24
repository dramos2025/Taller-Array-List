class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=None):
        if initial_elements is None:
            initial_elements = []
            
        self.head = None
        self.count = 0
        
        for element in initial_elements:
            self.append(element)
    
    
    # return an str of the collection
    def __str__(self):
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
            
        return "[" + " -> ".join(elements) + "]"
    
    
    # return the length
    def __len__(self):
        return self.count
    
    
    # return element by index
    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    
    # check if empty
    def isEmpty(self):
        return self.head is None
    
    
    # allow for loop
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    
    # check if element exists
    def __contains__(self, element):
        current = self.head
        
        while current:
            if current.data == element:
                return True
            current = current.next
        
        return False
    
    
    # add element at end
    def append(self, element):
        new_node = Node(element)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.count += 1
    
    
    # insert at index
    def insert(self, index, element):
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        
        new_node = Node(element)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
        
        self.count += 1
    
    
    # remove by value
    def remove(self, element):
        current = self.head
        previous = None
        
        while current:
            if current.data == element:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                
                self.count -= 1
                return
            
            previous = current
            current = current.next
        
        raise ValueError("Element not found")
    
    
    # pop by index
    def pop(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        
        current = self.head
        previous = None
        
        for _ in range(index):
            previous = current
            current = current.next
        
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        
        self.count -= 1
        return current.data
    
    
    # clear list
    def clear(self):
        self.head = None
        self.count = 0

if __name__ == "__main__":
    
    print("=== CREANDO LINKEDLIST ===")
    lista = LinkedList([10, 20, 30])
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
    