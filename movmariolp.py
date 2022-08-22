import re

matriz = []

file = open('codigo.txt', 'r')
numero = int(file.readline()) #numero de la matriz

archivo_error = open('errores.txt', 'w')
archivo_error.close()

for i in range(numero):
    matriz.append([0]*numero)

c = 0 # Columna
f = 0 # Fila


"""
Movimiento
———————–
eje : entero
pasos : string
n : entero
————————
Agrega el movimiento de la matriz, en la columna o fila. Hace un modulo con el 
tamano de la matriz para crear el efecto de matriz ciclica. Retorna el destino
final de la columna o de la fila.
"""
def movimiento(eje, pasos, n): # Nos movemos en el eje
    eje += int(pasos)
    eje = eje % n
    return eje


"""
Cambiar valor
———————–
matriz : listas de enteros
c : entero
f : entero
valor : entero
————————
Toma coordenadas dentro de la matriz y le suma el valor entregado a la funcion. La
gracia es que cuando en el lenguaje formal tenemos un A la da un 1, mientras que 
con un B le da un -1, asi que no se necesita funciones aparte para incrementar o
disminuir una celda. Retorna la matriz actualizada.
"""
def cambiar_valor(matriz, c, f, valor):
    matriz[f][c] += valor
    return matriz


"""
Cambiar valor cero
———————–
matriz : listas de enteros
c : entero
f : entero
————————
Toma coordenadas dentro de la matriz y le impone que su valor sea 0. Retorna
como resultado la matriz actualizada.
"""
def cambiar_valor_cero(matriz, c, f):
    matriz[f][c] = 0
    return matriz


"""
Multiplicar
———————–
matriz : listas de enteros
c : entero
f : entero
c2 : entero
f2 : entero
————————
Le entregamos las coordenas de la posicion actual dentro de la matriz (f, c) y tambien
le damos las coordenas de la celda con la que queremos multiplicar (f2, c2). Obtenemos
el valor de las coordenas (f2, c2) y la multiplicamos con (f, c). Retornamos la
matriz actualizada.
"""
def multiplicar(matriz, c, f, c2, f2):
    valor = matriz[f2][c2]
    matriz[f][c] = matriz[f][c] * valor
    return matriz


"""
Dividir
———————–
matriz : listas de enteros
c : entero
f : entero
c2 : entero
f2 : entero
————————
Le entregamos las coordenas de la posicion actual dentro de la matriz (f, c) y tambien
le damos las coordenas de la celda con la que queremos multiplicar (f2, c2). Obtenemos
el valor de las coordenas (f2, c2) y la divimos con (f, c) pero si el valor del divisor
es 0 entonces la funcion no hace nada. Retornamos la matriz actualizada o la matriz
anterior, dependiendo el caso.
"""
def dividir(matriz, c, f, c2, f2):
    valor = matriz[f2][c2]
    if valor != 0:
        matriz[f][c] = matriz[f][c] // valor
        return matriz
    else:
        return matriz


"""
Imprimir ascii
———————–
matriz : listas de enteros
c : entero
f : entero
————————
Recibimos coordenadas de la matriz y obtemos su valor entero, si el numero entra
dentro de los valores ascii esperados, entonces imprime el caracter asociado al
numero. No retorna nada.
"""
def imprimir_ascii(matriz, c, f):
    valor = matriz[f][c]
    if valor >= 32 and valor < 127:
        caracter = chr(matriz[f][c])
        print(caracter.strip(), end='')
    elif valor == 127: 
        print('')


"""
Imprimir entero
———————–
matriz : listas de enteros
c : entero
f : entero
————————
Recibimos coordenadas de la matriz y obtemos su valor entero, luego imprimimos
el numero. No retorna nada.
"""
def imprimir_entero(matriz, c, f):
    entero = matriz[f][c]
    print(entero, end='')


"""
Confirmar parentesis
———————–
contador : entero
linea_parentesis : string
indice : entero
————————
Recibimos una linea de string de unicamente los parentesis de la expresion regular, 
con un contador de "abre parentesis" y un indice que indica la posicion del string, 
esta funcion es una funcion recursiva. Si estan nivelados retorna True, si no retorna 
False 
"""
def confirmar_parentesis(contador, linea_parentesis, indice):
    # Si termina el la linea de string
    if indice >= len(linea_parentesis):
        # Si contador es 0 es porque los parentesis estan en equilibrio
        if contador == 0:
            # Asi que retornamos True
            return True
        # Y retornamos False cuando los parentesis no estan nivelados
        return False
    
    # Cuando encuentra un parentesis que abre
    elif linea_parentesis[indice] == '(':
        # Incrementamos 1 el contador y aumentamos el indice para el siguiente caracter
        contador += 1
        indice += 1
        # Llamamos nuevamente la funcion para ver el siguiente caracter
        return confirmar_parentesis(contador, linea_parentesis, indice)
    
    # Cuando encuentra un cierra parentesis y ademas se ha abierto un parentesis antes
    elif (linea_parentesis[indice] == ')' and contador != 0):
        # Disminuimos el contador y aumentamos el indice
        contador -= 1
        indice += 1
        # Llamamos nuevamente la funcion para ver el siguiente caracter
        return confirmar_parentesis(contador, linea_parentesis, indice)
    
    # Cuando encuenta un parentesis que cierra, pero sin uno que abra anteriormente
    else:
        # Mandamos un falso ya que no estan nivelados los parentesis
        return False


"""
Sacar parentesis
———————–
linea : string
numero_fila : entero
————————
Recibimos una linea de string de unicamente los parentesis de la expresion regular, 
con un contador de "abre parentesis" y un indice que indica la posicion del string, 
esta funcion es una funcion recursiva. Si estan nivelados retorna True, si no retorna 
False 
"""
def sacar_parentesis(linea, numero_fila):
    # El patron seran los abre y cierra parentesis, y los matches una lista con todos los 
    # que encuentre
    patron = re.compile(r'(\()|(\))')
    matches = patron.findall(linea)
    parentesis = ''
    for match in matches:
        for a in match:
            # Para cuando encuentra un parentesis
            if a != '':
                # Agregarlo al string
                parentesis += a
    # Evaluamos si los parentesis encontrados son validos en la sintaxis
    if confirmar_parentesis(0,parentesis,0):
        # Si es asi retornamos True
        return True
    # Si los parentesis no son validos en la sintaxis
    else:
        # Agregamos la linea del error a errores.txt
        error = open('errores.txt', 'a')
        error.write(str(numero_fila) + ' ' + linea + '\n')
        error.close()
        # Retornamos False
        return False


"""
Sintaxis
———————–
linea : string
numero_fila : entero
————————
Compilaremos toda una linea de la expresion regular, y obtendremos todos los match, 
juntaremos todos estos en un string 'sinta' y luego compararemos sinta con linea, si son 
iguales es porque no hay ningun error en la sintaxis, si no es porque existe un error. 
Retorna True si no existe error y False si existe algun error.
"""
def sintaxis(linea, numero_fila):
    # Tenemos toda la sintaxis del programa en este patron
    patron = re.compile(r'(U|D|<|>)([1-9])(U|D|<|>)?([1-9])?|(\()|(\))|(A)|(B)|(X|Y)(U|D|<|>)([1-9])(U|D|<|>)?([1-9])?|(L|S)([e|c])|(R)|(Z)')
    matches = patron.findall(linea)
    sinta = ''
    for match in matches:
        for a in match:
            if a != '':
                # Agregamos cada match encontrado al string sinta
                sinta += a
    # Si sinta es igual a linea
    if sinta == linea:
        # Retornamos true
        return True
    
    # Si no es igual entonces agregamos esta linea a errores.txt
    error = open('errores.txt', 'a')
    error.write(str(numero_fila) + ' ' + linea + '\n')
    error.close()
    # Retornamos False
    return False


"""
Ejecutar codigo
———————–
codigo : string
f : entero
c : entero
numero : entero
matriz : listas de enteros
————————
Recibe una linea de codigo y la leera de izquirda a derecha completamente, y reconocera 
los comandos dados. Retornara una tupla con la fila y la columna actual de la matriz.
"""
def ejecutar_codigo(codigo, f, c, numero, matriz):
    patron = re.compile(r'(U|D|<|>)([1-9])(U|D|<|>)?([1-9])?|(\()|(\))|(A)|(B)|(X|Y)(U|D|<|>)([1-9])(U|D|<|>)?([1-9])?|(L|S)([e|c])|(R)|(Z)')
    matches = patron.findall(codigo)
    for match in matches:
        # n sera el numero del grupo del match
        n = 1
        # dir sera un char que contenga (U|D|<|>)
        dir = ''
        # multidivi sera un char que contenga (X|Y)
        multidivi = ''
        # c2 y f2 seran coordenas auxiliares para multiplicar o dividir
        c2 = 0
        f2 = 0
        # flag_multidivi indica si el match es un comando de multiplicacion o division
        flag_multidivi = False
        # ls es un char que contenga (L|S)
        ls = ''
        for a in match:
            if a != '':
                #Buscaremos a que grupo pertenece el caracter encontrado
                
                # En estos grupos se encuentra el tipo dir
                if n == 1 or n == 3 or n == 10 or n == 12:
                    # Guardamos el caracter encontrado en la variable dir
                    dir = a
                
                # En estos grupos se encuentra el tipo numero
                elif n == 2 or n == 4 or n == 11 or n == 13:
                    # Si dir es U o D se moveran las filas
                    if dir == 'U' or dir == 'D':
                        # Cuando dir es U
                        if dir == 'U':
                            # Cuando subimos en la matriz, disminuimos f
                            pasos = -int(a)
                            # Si de antemano declaramos una multiplicacion o division
                            # cambiaremos f2, la variable auxiliar, y no cambiaremos f
                            if flag_multidivi:
                                f2 = movimiento(f, pasos, numero)
                                
                            # Cambiamos la posicion de f
                            else:
                                f = movimiento(f, pasos, numero)

                        # Cuando dir es D
                        else:
                            # Cuando bajamos en la matriz, aumentamos f
                            pasos = int(a)
                            # Si de antemano declaramos una multiplicacion o division
                            # cambiaremos f2, la variable auxiliar, y no cambiaremos f
                            if flag_multidivi:
                                f2 = movimiento(f, pasos, numero)
                                
                            # Cambiamos la posicion de f
                            else:
                                f = movimiento(f, pasos, numero)

                    # Si dir es > o < se moveran las columnas
                    else:
                        # Cuando dir es <
                        if dir == '>':
                            # Cuando avanzamos en la matriz, aumentamos c
                            pasos = int(a)
                            # Si de antemano declaramos una multiplicacion o division
                            # cambiaremos c2, la variable auxiliar, y no cambiaremos c
                            if flag_multidivi:
                                c2 = movimiento(c, pasos, numero)
                                
                            # Cambiamos la posicion de c
                            else:
                                c = movimiento(c, pasos, numero)
                                
                        # Cuando dir es <
                        else:
                            # Cuando retrocedemos en la matriz, disminuimos c
                            pasos = -int(a)
                            # Si de antemano declaramos una multiplicacion o division
                            # cambiaremos c2, la variable auxiliar, y no cambiaremos c
                            if flag_multidivi:
                                c2 = movimiento(c, pasos, numero)
                                
                            # Cambiamos la posicion de c
                            else:
                                c = movimiento(c, pasos, numero)
                    
                # En estos grupos se encuentra la operacion A | B
                elif n == 7 or n == 8:
                    # Si es un A, entonces le aumenta en 1 a la posicion actual
                    if a == 'A':
                        matriz = cambiar_valor(matriz, c, f, 1)
                        
                    # Si es un B, entonces le aumenta en -1 a la posicion actual
                    else: 
                        matriz = cambiar_valor(matriz, c, f, -1)
                
                # En este grupo se encuentra la operacion X | Y
                elif n == 9:
                    # Asignamos a la variable multidivi el valor encontrado (X|Y)
                    multidivi = a
                    # Al flag la avisamos que la operacion es una multiplicacion o division
                    flag_multidivi = True
                    
                # En este grupo se encuentra la operacion L | S
                elif n == 14:
                    # Asignamos a la variable ls el valor encontrado (L|S)
                    ls = a
                    
                # En este grupo se encuentra el tipo e | c
                elif n == 15:
                    # Si se imprime unicamente la casilla actual
                    if ls == 'L':
                        # Si debemos imprimir la casilla como entero
                        if a == 'e':
                            imprimir_entero(matriz, c, f)
                        # Si debemos imprimir la casilla como caracter
                        else:
                            imprimir_ascii(matriz, c, f)
                    
                    # Si se imprime toda la matriz
                    else: 
                        # Si debemos imprimir la matriz como entero
                        if a == 'e':
                            for filas in range(numero):
                                for columnas in range(numero):
                                    imprimir_entero(matriz, columnas, filas)
                        # Si debemos imprimir la matriz como caracter
                        else:
                            for filas in range(numero):
                                for columnas in range(numero):
                                    imprimir_ascii(matriz, columnas, filas)
                
                # En este grupo se encuentra la operacion R
                elif n == 16:
                    # Le asignamos el valor 0 a la casilla actual
                    matriz = cambiar_valor_cero(matriz, c, f)
                    
                # En este grupo se encuentra la operacion Z
                elif n == 17:
                    # Le asignamos el valor 0 a toda la matriz
                    for filas in range(numero):
                        for columnas in range(numero):
                            matriz = cambiar_valor_cero(matriz, columnas, filas)
            n += 1
        # Si el match era de operacion de multiplicacion o division
        if flag_multidivi:
            # Llamamos a su respectiva funcion dependiendo del caso
            
            if multidivi == 'X':
                matriz = multiplicar(matriz, c, f, c2, f2)
            else:
                matriz = dividir(matriz, c, f, c2, f2)
    return (f,c)

"""
Leer codigo
———————–
linea : string
matches : lista
indice : entero
f : entero
c : entero
numero : entero
matriz : listas de enteros
————————
Funcion recursiva, leemos una linea valida, y colocaremos cada dato en un string codigo.
Cada vez que se habra un parentesis se llamara denuevo la funcion y cuando cierre 
terminara de anadir a la variable codigo y comenzara a ejecutarlo. de esta manera nos
aseguramos la jerarquia de los parentesis. Retorna una tupla con (fila, columna, indice)
"""
def leer_codigo(linea, matches, indice, f, c, numero, matriz):
    # Inicializamos la variable codigo, la cual sera ejecutada
    codigo = ''
    # Recorremos la lista de matches
    while indice < len(matches):
        a = ''
        # Recorreremos los grupos de cada match
        for a in matches[indice]:
            if a != '':
                # Si nos encontramos con un parentesis que abre
                if a == '(':
                    # Llamamos nuevamente la funcion incrementando el indice para que asi
                    # comience con el primer caracter despues del parentesis
                    indice += 1
                    f,c,indice = leer_codigo(linea, matches, indice, f, c, numero, matriz)
                
                # Si nos encontramos con un parentesis que cierra
                elif a == ')':
                    # ejecutaremos el codigo y nos devolvera la posicion actual de la matriz
                    f,c = ejecutar_codigo(codigo, f, c, numero, matriz)
                    # Retornamos la casilla actual con el indice de donde quedo en la linea
                    return (f, c, indice)
                
                # Si no es ningun tipo de parentesis, anade el caracter a codigo
                if a != '(' and a != ')':
                    codigo += a
        # Incrementa el indice para ver el siguiente match
        indice += 1
    # Cuando termine de leer toda la linea ejecuta la ultima parte de esta
    f,c = ejecutar_codigo(codigo, f, c, numero, matriz)
    # Retornamos la casilla actual con el indice de donde quedo en la linea
    return (f,c,indice)


# numero_fila es la fila del archivo codigo.txt, nos servira para errores.txt
numero_fila = 1
# Recorremos cada linea del archivo
for linea in file:
    # Eliminamos el salto de linea
    linea = linea.rstrip()
    # Si los parentesis estan nivelados/validados
    if sacar_parentesis(linea, numero_fila):
        # Veremos si los comandos de codigo.txt tienen una correcta sintaxis
        if sintaxis(linea, numero_fila):
            patron = re.compile(r'(U|D|<|>)([1-9])(U|D|<|>)?([1-9])?|(\()|(\))|(A)|(B)|(X|Y)(U|D|<|>)([1-9])(U|D|<|>)?([1-9])?|(L|S)([e|c])|(R)|(Z)')
            # Obtemos una lista con todos los match's
            matches = patron.findall(linea)
            # El indice es para indicar el match en donde estaremos posicionados
            indice = 0
            # Leemos el codigo para su posterior ejecucion
            f,c,_ = leer_codigo(linea, matches, indice, f, c, numero, matriz)
    numero_fila += 1


# Veremos si el archivo errores.txt esta vacio
archivo_error = open('errores.txt', 'r+')
if len(archivo_error.readlines()) == 0:
    # Si esta vacio entonces escribir lo siguiente
    archivo_error.write('No hay errores!')
archivo_error.close()

file.close()