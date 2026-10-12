import random

def generar_patente() -> list:
    """
     El programa genera patentes aleatorias con el import random de fuera de la funcion.
     La patente requiere 2 letras, 3 numeros y 2 letras asi que hacemos 3 bucles for.
     en cada bucle se concatena al lado en la funcion patente los numeros o letras que se generan con el codigo ascii.
    
    Return:
        list: Retorna la patente
    """
    patente = ""
    for i in range(2):
        patente += chr(random.randint(65,90))
        continue
    
    for i in range(3):
        patente += chr(random.randint(48,57))
        continue
    
    for i in range(2):
        patente += chr(random.randint(65,90))
        
    return patente

def patente_repetida(patente: (str), lista: (list)) -> bool:
    """
     Compara las patentes guardas en la lista con las patentes de la funcion anterior. Si se repiten se vuelven a genera de forma aleatoria todas las patentes hasta que ninguna lo haga.
    
    Parametros:
        -patente(str): Las patentes generadas en la funcion anterior.
        -lista(list): Las patentes guardadas en la lista.
    
    Return:
        bool: Devuelve True si se repiten haciendo que vuelvan a generarse todas. Devuelve False si no se repiten.
    """
    for p in lista:
        if p == patente:
            return True

        return False
    
def porcentaje_letras(patentes: (list)):
    """
     Recorre con un len cuantas patentes hay en total. 
     Entra en un bucle donde recorre todas las letras y se crea un contador en 0. Dentro de otro bucle busca las letras en la patente incrementando el contador.
     Saca el porcentaje de cuantas veces sale cada letra.
     
    Parametros:
        -patentes(list): Las patentes generadas anteriormente. 
        
    Return:
        none
    """
    total = len(patentes)
    
    for i in range(65, 91):
        letra_actual = chr(i)
        contador = 0
        
        for p in patentes:
            if p[0] == letra_actual:
                contador = contador + 1
        porcentaje = (contador / total) * 100
        print(f"{letra_actual}: {porcentaje:.2f}%")
        
def ordenar_patentes(patentes: list, criterio: str) -> list:
    """
     Guarda la cantidad total de patentes que hay en la lista en una variable. 
     El primer for cuenta cuantas pasadas hay que hacer para que quede ordenado. En cada vuelta de "i" el elemento más grande flota hacia el final.
     El segundo bucle recorre elemento por elemento. Arranca en "0" y se compara con el de al lado para luego ordenarse según el criterio. El "-i" es para que no vuelva a revisar las posiciones que quedan fijas.
     El criterio evalúa si los elementos de al lado estan ordenados según criterio ascendente o descente.
     La variable "ordenar" es un variable auxiliar donde guardas de forma la patente de la izquierda.
     Se copia la patente de la derecha en la posicion de la izquierda.
     Pones lo que habia en la variable temporal a la derecha.
     
    Parametros:
        -patentes(list): Las patentes ya generadas.
        -criterio(str): El criterio "ASC" ascendente o "DESC" descendente que eligio el usuario.
        
    Return:
        list: Retorna la lista de forma ordenada.
    """
    n = len(patentes)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if criterio == "ASC" and patentes[j] > patentes[j+1]:
                ordenar = patentes[j]
                patentes[j] = patentes[j+1]
                patentes[j+1] = ordenar

            elif criterio == "DESC" and patentes[j] < patentes[j+1]:
                ordenar = patentes[j]
                patentes[j] = patentes[j+1]
                patentes[j+1] = ordenar
                
    return patentes


                
                
                
                
