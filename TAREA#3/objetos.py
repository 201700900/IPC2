class Texto:    
    def __init__(self, tamaño, mensaje):#Inicio de la clase y se definen las variables
        self.tamaño=tamaño
        self.mensaje=mensaje
        
    def Cambiar_Posiciones(arreglo, arregloNuevo):#metodo que llena el arreglo con los textos
        for i in range(0, len(arreglo), 1):
            cadena=arreglo[i]
            if len(cadena)%2!=0:
                cadena+=" " 
            
            tamaño=len(cadena)
            mitad=int(tamaño/2)
            dmitad=mitad-1
            dtamaño=tamaño-1

            for j in range(0, tamaño, 1):
                if j<mitad:
                    arregloNuevo.append(cadena[int(dmitad)])
                    dmitad-=1
                else:
                    arregloNuevo.append(cadena[int(dtamaño)])
                    dtamaño-=1
            TextoAux="".join(arregloNuevo)
            arreglo[i]=TextoAux
            arregloNuevo.clear()
    
    numero=int(input("Ingrese la cantidad de textos: "))
    arreglo=[]
    arregloNuevo=[]
    for i in range(0, numero, 1):
        mensaje=input("Ingrese el texto #"+str(i+1)+": ")
        tamaño=len(mensaje)
        arreglo.append(mensaje)    
    print(arreglo)
    Cambiar_Posiciones(arreglo, arregloNuevo)
    print(arreglo)
