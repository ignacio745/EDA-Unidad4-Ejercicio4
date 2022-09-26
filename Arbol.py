from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Arbol import Arbol


class Arbol:
    __caracter: str
    __frecuencia: int
    __izq: Arbol
    __der: Arbol
    __sig: Arbol


    def __init__(self, caracter) -> None:
        self.__caracter = caracter
        self.__frecuencia = 1
        self.__izq = None
        self.__der = None
        self.__sig = None

    
    def vacio(self):
        return self.__caracter == None

    
    def getCaracter(self):
        return self.__caracter
    
    def getSig(self) -> Arbol:
        return self.__sig
    
    def incrementarFrecuencia(self):
        self.__frecuencia += 1
    
    def getFrecuencia(self):
        return self.__frecuencia
    
    def setSig(self, sig:Arbol):
        self.__sig = sig
    
    def setFrecuencia(self, frecuencia:int):
        self.__frecuencia = frecuencia
    
    def setCaracter(self, caracter:str):
        self.__caracter = caracter


    def getIzq(self):
        return self.__izq
    
    def getDer(self):
        return self.__der
    
    def setDer(self, nuevoDer:Arbol):
        self.__der = nuevoDer
    
    def setIzq(self, nuevoIzq:Arbol):
        self.__izq = nuevoIzq


    
    def getCodigo(self, caracter:str) -> str:
        if not caracter in self.__caracter:
            raise Exception("No se encuentra el caracter {0} en el arbol".format(caracter))

        if len(self.__caracter) == 1:
            return ""
        elif caracter in self.__izq.getCaracter():
            return "0" + self.__izq.getCodigo(caracter)
        elif caracter in self.__der.getCaracter():
            return "1" + self.__der.getCodigo(caracter)
    


    def getCadena(self, bytes: str):
        pos = 0
        cadena = ""
        actual = self
        while pos < len(bytes):
            if bytes[pos] == "0":
                actual = actual.getIzq()
            elif bytes[pos] == "1":
                actual = actual.getDer()
            pos += 1

            if len(actual.getCaracter()) == 1:
                cadena += actual.getCaracter()
                actual = self

        return cadena