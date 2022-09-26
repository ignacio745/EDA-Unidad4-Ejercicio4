from ListaEncadenada import ListaEncadenada

if __name__ == "__main__":
    unaLista = ListaEncadenada()
    archivo = open("archivo_prueba.txt")
    diccionario = dict()
    for linea in archivo:
        for caracter in linea:
            unaLista.agregar(caracter)

    arbolHuffman = unaLista.generarArbol()

    nuevoArchivo = open("comprimido.txt", "w")

    archivo.seek(0)

    for linea in archivo:
        for caracter in linea:
            codigo = arbolHuffman.getCodigo(caracter)
            nuevoArchivo.write(codigo)
    
    nuevoArchivo.close()
    archivo.close()

    archivo = open("comprimido.txt")
    descomprimido = open("descomprimido.txt", "w")
    bytes = ""
    
    for linea in archivo:
        for bit in linea:
            bytes += bit
    
    nuevaCadena = arbolHuffman.getCadena(bytes)
    
    descomprimido.write(nuevaCadena)