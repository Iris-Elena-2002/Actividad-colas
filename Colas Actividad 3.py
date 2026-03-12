class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ColaLigadaSimple:
    def __init__(self):
        self.frente = None
        self.final = None

    def vacia(self):
        return self.frente is None

    def encolar(self, valor):
        nuevo = Nodo(valor)
        if self.final is None:
            self.frente = self.final = nuevo
            return
        self.final.siguiente = nuevo
        self.final = nuevo

    def primer_elemento(self):
        if not self.vacia():
            return self.frente.valor
        return None

    def recorrer_cola(self):
        actual = self.frente
        while actual:
            print(actual.valor, end="")
            actual = actual.siguiente
        print()

    def sustituir_vocales(self):
        actual = self.frente
        while actual:
            if actual.valor == "a":
                actual.valor = "4"
            elif actual.valor == "e":
                actual.valor = "3"
            elif actual.valor == "i":
                actual.valor = "1"
            elif actual.valor == "o":
                actual.valor = "0"
            elif actual.valor == "u":
                actual.valor = "7"
            actual = actual.siguiente

    def guardar_archivo(self, nombre_archivo):
        actual = self.frente
        with open(nombre_archivo, "w") as archivo:
            while actual:
                archivo.write(actual.valor)
                actual = actual.siguiente

# Programa principal
cola = ColaLigadaSimple()
# 1.Leer archivo Texto.txt y almacenar caracteres
with open("C:\\Users\\irise\\OneDrive\\Documentos\\ITA\\Semestre 3\\Estructura y organización de datos\\EJERCICIOS\\UNIDAD 2\\Texto.txt", "r") as archivo:
    contenido = archivo.read()
    for caracter in contenido:
        cola.encolar(caracter)

# 2.Imprimir el contenido de la estructura completa
print("Contenido original de la cola: ")
cola.recorrer_cola()

# 3.Sustituir en la estructura las vocales por números
cola.sustituir_vocales()

# 4.Imprimir el elemento al frente de la estructura
print("\nElemento al frente de la cola: ")
print(cola.primer_elemento())

# 5.Imprimir el contenido de la estructura completa modificada
print("\nContenido modificado de la cola: ")
cola.recorrer_cola()

# 6.Guardar contenido en archivo
cola.guardar_archivo("C:\\Users\\irise\\OneDrive\\Documentos\\ITA\\Semestre 3\\Estructura y organización de datos\\EJERCICIOS\\UNIDAD 2\\Resultado.txt")
print("\nArchivo guardado como Resultado.txt")