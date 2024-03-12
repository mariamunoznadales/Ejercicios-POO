class Palindromo:
    def _init_(self, cadena):
        self.cadena = cadena.lower() 
    # Para convertir la cadena a minúsculas 
        
    @classmethod
    def esPalindromo(cls, cadena):
        cadena_limpia = cadena.lower()
        return cadena_limpia == cadena_limpia[::-1]  
    # Ver si la cadena es igual a si misma al revés
    
    def test(self):
        resultado = self.esPalindromo(self.cadena)  
    # Utilizar el método de clase para verificar el palíndromo
        print(self.cadena.upper())  
    # Imprimir la cadena en mayúsculas
        return resultado
    
    def _del_(self):
        print(self.cadena.upper())
        
def main():
    pass

if __name__ == "__main__":
    main()
    