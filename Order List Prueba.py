class OrderList:
    
    def __init__(self, elementos_iniciales=None):
        if elementos_iniciales is None:
            elementos_iniciales = []
        self._datos = sorted(elementos_iniciales)
    
    
    # Representación en texto
    def __str__(self):
        return str(self._datos)
    
    
    # Longitud
    def __len__(self):
        return len(self._datos)
    
    
    # Acceso por índice (permitido porque no rompe el orden)
    def __getitem__(self, indice):
        if indice < 0 or indice >= len(self._datos):
            raise IndexError("Índice fuera de rango")
        return self._datos[indice]
    
    
    # Verificar si está vacía
    def esta_vacia(self):
        return len(self._datos) == 0
    
    
    # Iterador
    def __iter__(self):
        for elemento in self._datos:
            yield elemento
    
    
    # 🔎 Búsqueda binaria
    def __contains__(self, elemento):
        izquierda = 0
        derecha = len(self._datos) - 1
        
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            
            if self._datos[medio] == elemento:
                return True
            elif self._datos[medio] < elemento:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        
        return False
    
    
    # 🔥 Encontrar posición correcta (binaria)
    def _buscar_posicion(self, elemento):
        izquierda = 0
        derecha = len(self._datos)
        
        while izquierda < derecha:
            medio = (izquierda + derecha) // 2
            
            if self._datos[medio] < elemento:
                izquierda = medio + 1
            else:
                derecha = medio
        
        return izquierda
    
    
    # Insertar manteniendo orden
    def agregar(self, elemento):
        posicion = self._buscar_posicion(elemento)
        self._datos.insert(posicion, elemento)
    
    
    # Eliminar por valor
    def eliminar(self, elemento):
        if elemento not in self:
            raise ValueError("Elemento no encontrado")
        
        posicion = self._buscar_posicion(elemento)
        self._datos.pop(posicion)
    
    
    # Sacar por índice (no rompe orden porque solo elimina)
    def sacar(self, indice):
        if indice < 0 or indice >= len(self._datos):
            raise IndexError("Índice fuera de rango")
        return self._datos.pop(indice)
    
    
    # Vaciar lista
    def limpiar(self):
        self._datos.clear()

if __name__ == "__main__":
    
    print("=== CREANDO ORDER LIST ===")
    lista = OrderList([30, 10, 20, 60])
    print("Lista inicial (ordenada automáticamente):", lista)
    print("Longitud:", len(lista))
    print("¿Está vacía?:", lista.esta_vacia())
    
    print("\n=== AGREGAR ELEMENTOS ===")
    lista.agregar(40)
    print("Después de agregar 40:", lista)
    
    lista.agregar(5)
    print("Después de agregar 5:", lista)
    
    lista.agregar(70)
    print("Después de agregar 70:", lista)
    
    print("\n=== ACCESO POR ÍNDICE ===")
    print("Elemento en índice 2:", lista[2])
    
    print("\n=== BÚSQUEDA (BINARIA) ===")
    print("¿Está 20 en la lista?", 20 in lista)
    print("¿Está 100 en la lista?", 100 in lista)
    
    print("\n=== ITERACIÓN ===")
    for elemento in lista:
        print(elemento)
    
    print("\n=== ELIMINAR ===")
    lista.eliminar(20)
    print("Después de eliminar 20:", lista)
    
    print("\n=== SACAR POR ÍNDICE ===")
    eliminado = lista.sacar(1)
    print("Elemento eliminado en índice 1:", eliminado)
    print("Lista actual:", lista)
    
    print("\n=== LIMPIAR ===")
    lista.limpiar()
    print("Después de limpiar:", lista)
    print("Longitud final:", len(lista))