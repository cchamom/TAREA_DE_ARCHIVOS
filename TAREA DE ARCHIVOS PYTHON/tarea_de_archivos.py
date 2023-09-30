 
import json
tareas = []

print("Aquí podrás entregar y ver tus tareas realizadas, tambien podras elimminar o marcar las tareas que ya hayas hecho\n")

def guardar_tareas(archivo, tareas):
    with open(archivo, 'w') as file:
        json.dump(tareas, file)

def agregar_tarea():
    tarea = input("Ingresar una nueva tarea:\n ")
    tareas.append(tarea)
    print("Tarea agregada con éxito")

def eliminar_tarea():
    if tareas:
        tarea = int(input("Ingrese el número de la tarea que deseas marcar como realizada: ")) - 1
        if 0 <= tarea < len(tareas):
            tareas.pop(tarea)
            print("Tarea marcada con éxito")
        else:
            print("Esta tarea no existe")
    else:
        print("No hay tareas en la lista")

def mostrar_tareas():
    if tareas:
        print("Lista de las tareas\n")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas en la lista")

def main():
    opcion = 0

    while opcion != 4:
        print("---Lista de tareas---\n")
        print("1: Agregar tarea")
        print("2: Marcar una tarea completada")
        print("3: Mostrar las tareas")
        print("4: Salir\n")

        opcion = int(input("Seleccione una opción:\n "))

        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            eliminar_tarea()
        elif opcion == 3:
            mostrar_tareas()
        elif opcion == 4:
            guardar_tareas("tareas.txt", tareas)
            print("Gracias por usar este programa, bay :)")
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

            



