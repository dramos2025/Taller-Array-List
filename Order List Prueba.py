class OrderList:
    
    # Constructor
    # initial_elements: permite iniciar la colección con elementos
    def __init__(self, initial_elements=[]):
        # Se ordenan los elementos desde el inicio para garantizar
        # que la lista siempre mantenga el orden (invariante).
        # sorted() devuelve una nueva lista ordenada.
        self._data = sorted(initial_elements)
    
    
    # Devuelve una representación en texto de la colección
    # Permite que al hacer print(objeto) se muestre la lista
    def __str__(self):
        return str(self._data)
    
    
    # Devuelve la cantidad de elementos de la colección
    # Permite usar len(objeto)
    def __len__(self):
        return len(self._data)
    
    
    # Permite acceder a un elemento por índice
    # Ejemplo: lista[2]
    # Lanza error si el índice no existe
    def __getitem__(self, index):
        # Si la lista está vacía no se puede acceder a ningún índice
        if self.isEmpty():
            raise IndexError("The list is empty")
        
        # Verificamos que el índice esté dentro del rango válido
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range")
        
        # Retornamos el elemento en la posición indicada
        return self._data[index]


    # Devuelve True si la lista está vacía, False en caso contrario
    def isEmpty(self):
        return len(self._data) == 0
    
    
    # Permite recorrer la colección con un ciclo for
    # Ejemplo: for element in lista:
    def __iter__(self):
        # yield devuelve los elementos uno por uno
        # sin crear una copia adicional
        for element in self._data:
            yield element
    
    
    # Verifica si un elemento existe en la colección
    # Permite usar: elemento in lista
    def __contains__(self, element):
        # Si la lista está vacía, no puede contener nada
        if self.isEmpty():
            return False
        
        # Implementación de búsqueda binaria
        # Se puede usar porque la lista siempre está ordenada
        left = 0
        right = len(self._data) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Punto medio
            
            if self._data[mid] == element:
                return True  # Elemento encontrado
            
            elif self._data[mid] < element:
                # Si el elemento buscado es mayor,
                # buscamos en la mitad derecha
                left = mid + 1
            else:
                # Si es menor, buscamos en la mitad izquierda
                right = mid - 1
        
        # Si termina el ciclo, no se encontró el elemento
        return False
    
    
    # Agrega un elemento manteniendo el orden
    def add(self, element):
        # Buscamos la posición correcta recorriendo la lista
        # hasta encontrar un elemento mayor
        position = 0
        
        while position < len(self._data) and self._data[position] < element:
            position += 1
        
        # Insertamos el elemento en la posición encontrada
        # Esto mantiene el orden
        self._data.insert(position, element)
    
    
    # Elimina un elemento por su valor
    # Lanza error si el elemento no existe
    def remove(self, element):
        # No se puede eliminar si la lista está vacía
        if self.isEmpty():
            raise ValueError("The list is empty")
        
        # Si el elemento no está en la lista, lanzamos error
        if element not in self:
            raise ValueError("Element not found")
        
        # Buscamos el índice del elemento
        index = 0
        while index < len(self._data):
            if self._data[index] == element:
                # Eliminamos el elemento encontrado
                self._data.pop(index)
                return
            index += 1
    
    
    # Elimina y retorna el elemento por índice
    def pop(self, index):
        # No se puede hacer pop si la lista está vacía
        if self.isEmpty():
            raise IndexError("The list is empty")
        
        # Validamos rango
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range")
        
        # Eliminamos y retornamos el elemento
        return self._data.pop(index)
    
    
    # Elimina todos los elementos de la colección
    def clear(self):
        self._data.clear()


# ===============================
# MAIN DE PRUEBA
# ===============================
if __name__ == "__main__":
    
    print("=== Creating OrderList ===")
    order_list = OrderList([30, 10, 20, 60])
    
    # El constructor ordena automáticamente
    print("Initial list (ordered automatically):", order_list)
    
    # Probamos longitud
    print("Length:", len(order_list))
    
    # Probamos si está vacía
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
