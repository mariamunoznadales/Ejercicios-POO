class Logger:
    def __init__(self, filename):  # Constructor de la clase Logger que recibe el nombre del archivo como parámetro
        self.filename = filename  # Guarda el nombre del archivo
        self.log_count = 0  # Inicializa el contador de registros a 0
        self.file = open(self.filename, "w")  # Abre el archivo en modo escritura ("w")
        self.file.write("--Start log--\n")  # Escribe la línea inicial en el archivo
    
    def log(self, message):  # Método para registrar un mensaje en el archivo
        self.log_count += 1  # Incrementa el contador de registros
        self.file.write(message + "\n")  # Escribe el mensaje en una nueva línea en el archivo
    
    def __del__(self):  # Método destructor de la clase
        self.file.write("--End log: {} log(s)--".format(self.log_count))  # Escribe la línea final en el archivo
        self.file.close()  # Cierra el archivo

class Test:
    def __init__(self):  # Constructor de la clase Test
        self.logger = Logger("log.txt")  # Crea una instancia de Logger con el nombre de archivo "log.txt"
    
    def llamada(self, message):  # Método para realizar una llamada y registrar un mensaje
        self.logger.log(message)  # Registra el mensaje en el archivo de registro

# Ejemplo de uso
test = Test()  # Crea una instancia de la clase Test
for i in range(1, 6):  # Itera sobre un rango del 1 al 5
    if i == 1:  # Si es la primera iteración
        test.llamada("Primera llamada")  # Registra el mensaje "Primera llamada"
    else:  # Para otras iteraciones
        test.llamada("{}ª llamada".format(i))  # Registra el mensaje con el número de iteración

# Eliminar la instancia de Test para que se escriba la última línea del registro
del test  # Elimina la instancia de Test
