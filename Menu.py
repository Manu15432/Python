import os
def fn_factorial(numero): 
    if numero == 0:
        return 1 
    else:
          return numero * fn_factorial(numero-1)

def fnRecursiva(n,p,acumulado):
    while n>0 :
        acumulado=acumulado+n*p
        n=n-1
        fnRecursiva(n,p,acumulado)
        return acumulado

def digitos(n):
    digits = len((n))
    return digits

def potencia(p,n,b):
    c=1
    
    while c==1:

        if b**p==n:
            c=2
            return bool(1)
        else:
            return potencia(p+1,n,b)  

def llenar():
    lista = []
    i=0
    size=(input("Introduzca el tamaño de la lista: "))
    if size.isnumeric()==True:
        print("El número ingresado es correcto.")
    else:
        print("El número ingresado es incorrecto.")
    try:
        while i < int(size):
            listaN=float(input("Introduce un número entero para llenar la lista: "))
            lista.append(listaN)
            i+=1
        return lista
    except ValueError:
        print("ERROR, datos ingresados inválidos")
            
def burbuja():
    lista=llenar()
    for i in range(0,len(lista)-1):
        for j in range(0,len(lista)-i-1):
            if(lista[j]>lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print("Se realizó un intercambio entre los valores "+str(lista[j])+" y "+str(lista[j+1])+" en las posiciones "+str(j)+" y "+str(j+1))
    print("La lista ordenada según método burbuja es: ")
    for x in range(0,len(lista)):
        print(lista[x])
                
   
   

def burbuja_mejorada():
    lista=llenar()
    i = 0
    control = True
    while (i<=len(lista)-2) and control:
        control = False
        for j in range(0,len(lista)-i-1):
            if(lista[j]>lista[j+1]):
                lista[j],lista[j+1] = lista[j+1],lista[j]
                print("Se realizó un intercambio entre los valores "+str(lista[j])+" y "+str(lista[j+1])+" en las posiciones "+str(j)+" y "+str(j+1))
                control =True
        i+=1

    print("La lista ordenada según método burbuja mejorado es: ")
    for x in range(0,len(lista)):
        print(lista[x])

def burbuja_bidireccional():
    lista=llenar()
    izquierda=0
    derecha=len(lista)-1
    control=True
    while (izquierda<derecha) and control:
        control=False
        for i in range(izquierda,derecha):
            if(lista[i]>lista[i+1]):
                control = True
                lista[i],lista[i+1] = lista[i+1],lista[i]
                print("Se realizó un intercambio entre los valores "+str(lista[i])+" y "+str(lista[i+1])+" en las posiciones "+str(i)+" y "+str(i+1))
        derecha-=1
        for j in range(derecha,izquierda,-1):
            if(lista[j]<lista[j-1]):
                control=True
                lista[j],lista[j-1] = lista[j-1],lista[j]
                print("Se realizó un intercambio entre los valores "+str(lista[j])+" y "+str(lista[j-1])+" en las posiciones "+str(j)+" y "+str(j-1))
        izquierda+=1
    
    print("La lista ordenada según método burbuja bidireccional es: ")
    for x in range(0,len(lista)):
        print(lista[x])

def menu():
    print("Bienvenido al menu")
    print("==========================================================")
    print("Seleccion a para calcular el factorial de un numero")
    print("Seleccion b para calcular la siguiente funcion K(n, p) = 1 * p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p")
    print("Seleccion c para calcular la cantidad de digitos de un numero")
    print("Seleccion d para calcular la potencia de un numero")
    print("Seleccion e para metodo de burbuja")
    print("Seleccion f para metodo de burbuja mejorada")
    print("Seleccion g para metodo de burbuja bidireccional")
    print ("Seleccione s para salir")
    print("==========================================================")
    seleccion_menu=str(input("Ingrese una opcion: "))
    if seleccion_menu=="s" or seleccion_menu=="S":
        os.system("cls")
        quit()
    if seleccion_menu=="a" or seleccion_menu=="A":
        print("==========================================================")
        c=1
        while c==1:
            try:
                numero=int(input("Ingrese un numero: "))
                c=2
            except:
                
                print("Debe de ingresar un numero")
                input("Presiona Enter para continuar")
                os.system("cls")
        print("==========================================================")
        print(fn_factorial(numero))
        print("Presione Enter para  continuar")
        input()
        os.system("cls")
        menu()
        seleccion_menu=str(input("Digite otra opcion: "))
    if seleccion_menu=="b" or seleccion_menu=="B":
        print("==========================================================")
        c=1
        while c==1:
            try:
                p=int(input('Ingrese el numero p: '))
                n=int(input('Ingrese el numero n: '))
                c=2
            except:
                print("Debe ingresar un numero")
        print("==========================================================")
        print("El resultado es: ")
        print(fnRecursiva(n,p,0))
        print("Presione Enter para  continuar")
        input()
        os.system("cls")
        menu()
        
    if seleccion_menu=="c" or seleccion_menu=="C":
            print("==========================================================")
            n=str(input('Ingrese una cantidad: '))
            print("La cantidad de digitos es:")
            print("==========================================================")
            print(digitos(n))
            print("Presione Enter para  continuar")
            input()
            os.system("cls")
            menu()
           
    if seleccion_menu=="d" or seleccion_menu=="D":
            print("==========================================================")
            n= int(input("Digite la potencia a encontrar: "))
            b= int(input("Digite el número al que desea encontrar la potencia: "))
            p=1
            print("==========================================================")
            print(potencia(p,n,b))
            print("Presione Enter para  continuar")
            input()
            os.system("cls")
            menu()
    if seleccion_menu=="e" or seleccion_menu=="E":        
        burbuja()
        print("Presione Enter para  continuar")
        input()
        os.system("cls")
        menu()
    if seleccion_menu=="f" or seleccion_menu=="F":
        burbuja_mejorada()
        print("Presione Enter para  continuar")
        input()
        os.system("cls")
        menu()
    if seleccion_menu=="g" or seleccion_menu=="G":
        burbuja_bidireccional()
        print("Presione Enter para  continuar")
        input()
        os.system("cls")
        menu()

os.system("cls")
print("==========================================================")   
print("            Digite si para entrar al menu")
print("==========================================================")
C=1
while C==1:
        x=str(input("Desea accedar al menu?: \n"))
        if x.islower()==True:
            C=2
        if x.islower()==False:
            print("Debe de ingresarlo en minusculas ")

os.system("cls")
menu()