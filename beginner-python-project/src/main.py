print ("Menú de opciones:")
print ("1. Agregar tarea")
print ("2. Ver tareas")
print ("3. Marcar tarea como completada")
print ("4. Eliminar tarea")
print ("5. Salir")

tareas = []
estado_tareas = []

while True:
    opcion = input("Opción: ")
    print ("1. Agregar tarea")
    print ("2. Ver tareas")
    print ("3. Marcar tarea como completada")
    print ("4. Eliminar tarea")
    print ("5. Salir")
    
    if opcion == "1":
        nombre = input("Nombre de la tarea: ")
        estado = input("Estado de la tarea (pendiente/completada): ")
        tareas.append(nombre)
        estado_tareas.append(estado)
    elif opcion == "2":
        print("Tareas pendientes:")
        for i in range(len(tareas)):
            print(f"{i+1}. {tareas[i]} - {estado_tareas[i]}")
    elif opcion == "3":
        indice = int(input("Indice de la tarea a marcar como completada: "))
        if indice <= len(tareas) and indice >= 1:
            estado_tareas[indice-1] = "completada"
        else:
            print("Indice no válido")
    elif opcion == "4":
        indice = int(input("Indice de la tarea a eliminar: "))
        if indice <= len(tareas) and indice >= 1:
            tareas.pop(indice-1)
            estado_tareas.pop(indice-1)
        else:
            print("Indice no válido")
    elif opcion == "5":
        break
    else:
        print("Opción no válida")