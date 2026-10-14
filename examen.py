from funciones import *

patentes = []
patentes_generadas = False

while True:
    print("\n========================")
    print("        MENÚ")
    print("========================")
    print()
    print("1. Generar patentes")
    print("2. Buscar patentes")
    print("3. Informar estadísticas")
    print("4. Ordenar y mostrar patentes")
    print("5. Salir")
    
    opcion = input("\nElegir opción: ")
    
    match opcion:
        case "1":
            print("\n------------------------")
            print("Ejecutando opción 1")
            print("------------------------")
            
            entrada = input("\nIngrese la cantidad de patentes a agregar: ")
            es_entero = False
            
            while not es_entero:
                if entrada != "":
                    es_valido = True
                    
                for caracter in entrada:
                    if caracter < '0' or caracter > '9':
                        es_valido = False
                        break
                    
                es_entero = es_valido
                    
                if not es_entero:
                    print("\n------------------------")
                    print("ERROR. Ingrese un número entero.")
                    print("------------------------\n")
                    entrada = input("Ingrese la cantidad de patentes que quiera agregar: ")
                    
            cantidad = int(entrada)
            
            for i in range(cantidad):
                patente_nueva = generar_patente()
                
                while patente_repetida(patente_nueva, patentes):
                    patente_nueva = generar_patente()
                
                patentes += [patente_nueva]
                
            patentes_generadas = True
            
            print("\n========================")
            print("Fin de la opción 1.")
            print("========================")
            
        case "2":
            print("\n------------------------")
            print("Ejecutando opción 2")
            print("------------------------")
            
            if patentes_generadas == True:
                patente_ingresada = input("\nIngrese la patente a buscar: ")
                encontrada = False
                
                for p in patentes:
                    if p == patente_ingresada:
                        encontrada = True
                        break
                    
                if encontrada == True:
                    print("\n------------------------")
                    print("Patente encontrada.")
                    print("------------------------\n")
                    
                else:
                    print("\n------------------------")
                    print("Patente no encontrada.")
                    print("------------------------\n")
                    
            else:
                print("\n------------------------")
                print("ERROR. Debe haber patentes generadas.")
                print("------------------------\n")
            
            print("\n========================")
            print("Fin de la opción 2.")
            print("========================")
            
        case "3":
            print("\n------------------------")
            print("Ejecutando opción 3")
            print("------------------------")
            
            if patentes_generadas == True:
                mas_antigua = patentes[0]
                mas_nueva = patentes[0]
                num_viejo = int(patentes[0][2:5])
                num_nuevo = int(patentes[0][2:5])
                
                for p in patentes:
                    num_actual = int(p[2:5])
                    
                    if num_actual > num_nuevo:
                        num_nuevo = num_actual
                        mas_nueva = p
                        
                    if num_actual < num_viejo:
                        num_viejo = num_actual
                        mas_antigua = p
                        
                print("\n------------------------")
                print(f"Patente más antigua: {mas_antigua}")
                print(f"Patente más reciente: {mas_nueva}")
                print("------------------------\n")
                    
                porcentaje_letras(patentes)
                
            else:
                print("\n------------------------")
                print("ERROR. Debe haber patentes generadas.")
                print("------------------------\n")
                
            print("\n========================")
            print("Fin de la opción 3.")
            print("========================")
            
        case "4":
            print("\n------------------------")
            print("Ejecutando opción 4")
            print("------------------------")
            
            if patentes_generadas == True:
                criterio = input("Elija método de ordenamiento. (ASC / DESC): ")
                
                while criterio != "ASC" and criterio != "DESC":
                    print("\n------------------------")
                    print("ERROR. Debe ingresar 'ASC' o 'DESC'.")
                    print("------------------------\n")
                    criterio = input("Elija método de ordenamiento. (ASC / DESC): ")
    
                patentes = ordenar_patentes(patentes, criterio)
                
                print("\n------------------------")
                print(patentes)
                print("========================")
                
            else:
                print("\n------------------------")
                print("ERROR. Debe haber patentes generadas.")
                print("------------------------\n")
                
            print("\n========================")
            print("Fin de la opción 4.")
            print("========================")
            
        case "5":
            print("\nSaliendo del programa...")
            break
        
        case _:
            print("\nError. Opción inexistente.")
    
    input("\nPresione Enter para volver al menú...")
