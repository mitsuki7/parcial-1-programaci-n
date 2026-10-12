from funciones import *

patentes = []
cantidad = int(input("Ingrese la cantidad de patentes que deseé: "))
patentes_generadas = False

while True:
    print("\n== MENÚ ==")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Salir")
    
    opcion = input("\nElegir opción: ")
    
    match opcion:
        case "1":
            print("Ejecutando opción 1...")
            cantidad = int(input("Ingrese la cantidad de patentes que quiera agregar: "))
            
            for i in range(cantidad):
                patente_nueva = generar_patente()
                while patente_repetida(patente_nueva, patentes):
                    patente_nueva = generar_patente()
                
                patentes += [patente_nueva]
                
            patentes_generadas = True
            
        case "2":
            print("Ejecutando opción 2...")
            if patentes_generadas == True:
                patente_ingresada = input("Ingrese la patente a buscar: ")
                encontrada = False
                
                for p in patentes:
                    if p == patente_ingresada:
                        encontrada = True
                        break
                    
                if encontrada == True:
                    print("Patente encontrada.")
                    
                else:
                    print("Patente no encontrada.")
                        
            else:
                print("ERROR. Debe haber patentes generadas.")
            
        case "3":
            print("Ejecutando opción 3...")
            if patentes_generadas == True:
                mas_antigua = patentes[0]
                mas_nueva = patentes[0]
                num_viejo = int(patentes[0] [2:5])
                num_nuevo = int(patentes[0][2:5])
                
                for p in patentes:
                    num_actual = int(p[2:5])
                    if num_actual > num_nuevo:
                        num_nuevo = num_actual
                        mas_nueva = p
                        
                    if num_actual < num_viejo:
                        num_viejo = num_actual
                        mas_antigua = p
                        
                print(f"Patente más antigua: {mas_antigua}")
                print(f"Patente más reciente: {mas_nueva}")
                    
                porcentaje_letras(patentes)
            else:
                print("ERROR. Debe haber patentes generadas.")
                
        case "4":
            print("Ejecutando opción 4...")
            if patentes_generadas == True:
                criterio = input("Elija metodo de ordenamiento. (ASC / DESC): ")
                
                while criterio != "ASC" and criterio != "DESC":
                    print("ERROR. Debe ingresar 'ASC' o 'DESC'.")
                    criterio = input("Elija metodo de ordenamiento. (ASC / DESC): ")
    
                patentes = ordenar_patentes(patentes, criterio)
                
            else:
                print("ERROR. Debe haber patentes generadas.")
                        
        case "5":
            print("Saliendo del programa...")
            break
        
        case _:
            print("Error. Opción inexistente.")
