class A:
    def __init__(self):
        pass
    
    def obtener_instancia(self):
        # Devuelve la instancia actual
        return self
    
    def longitud_objetivo(self, objetivo):
        # Devuelve la longitud del objetivo proporcionado
        return len(objetivo)

# Creamos una instancia de la clase A
instancia_a = A()

# Obtenemos una referencia al método obtener_instancia de la instancia_a
metodo_obtener_instancia = instancia_a.obtener_instancia
print(metodo_obtener_instancia())

# Comprobamos si dos instancias de A son las mismas
otra_instancia_a = A()
print(otra_instancia_a is A())  # Devolverá False, son instancias diferentes

# Calculamos la longitud de una tupla vacía con el método longitud_objetivo
metodo_longitud_objetivo = instancia_a.longitud_objetivo
print(metodo_longitud_objetivo(()))  # Devolverá 0, la longitud de la tupla vacía es 0

# Calculamos la longitud de una tupla que contiene una referencia a la clase A
print(A().longitud_objetivo((A,)))  # Devolverá 1,  la longitud de una tupla con un elemento es 1

# Calculamos la longitud de una tupla que contiene la referencia al método obtener_instancia y otros elementos
print(instancia_a.longitud_objetivo((metodo_obtener_instancia, 1, 'z')))  # Devolverá 3, la longitud de la tupla es 3