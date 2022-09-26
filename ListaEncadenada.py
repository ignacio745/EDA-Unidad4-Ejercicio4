from Arbol import Arbol

class ListaEncadenada:
    __cabeza: Arbol

    def __init__(self) -> None:
        self.__cabeza = None

    
    def agregar(self, caracter: str):
        actual = self.__cabeza
        while actual != None and actual.getCaracter() != caracter:
            actual = actual.getSig()
        if actual != None:
            actual.incrementarFrecuencia()
        else:
            unNodo = Arbol(caracter)
            unNodo.setSig(self.__cabeza)
            self.__cabeza = unNodo
    
    def ordenar(self):
        cota = None
        ultimo_cambio = None

        while ultimo_cambio != self.__cabeza:
            ultimo_cambio = self.__cabeza
            actual = self.__cabeza
            while actual.getSig() != cota:
                if actual.getFrecuencia() > actual.getSig().getFrecuencia():
                    auxCaracter = actual.getCaracter()
                    auxFrecuencia = actual.getFrecuencia()
                    actual.setCaracter(actual.getSig().getCaracter())
                    actual.setFrecuencia(actual.getSig().getFrecuencia())
                    actual.getSig().setCaracter(auxCaracter)
                    actual.getSig().setFrecuencia(auxFrecuencia)
                    ultimo_cambio = actual
                actual = actual.getSig()

            cota = ultimo_cambio.getSig()
    

    def generarArbol(self) -> Arbol:
        self.ordenar()
        
        while self.__cabeza.getSig() != None:
            nuevoArbol = Arbol(self.__cabeza.getCaracter()+self.__cabeza.getSig().getCaracter())
            nuevoArbol.setFrecuencia(self.__cabeza.getFrecuencia()+self.__cabeza.getSig().getFrecuencia())
            nuevoArbol.setIzq(self.__cabeza)
            nuevoArbol.setDer(self.__cabeza.getSig())
            nuevoArbol.setSig(self.__cabeza.getSig().getSig())
            self.__cabeza = nuevoArbol
        
        return self.__cabeza