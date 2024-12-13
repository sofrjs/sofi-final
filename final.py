SensorBrazoRobotico = []

def cargarLecturas(SensorBrazoRobotico):
    cantidad = int(input("Ingrese la cantidad de sensores: "))
    for i in range(cantidad):
        lectura = float(input(f"Ingrese la lectura del sensor N°{i + 1}:  "))
        SensorBrazoRobotico.append(lectura)
    
def mostrarLectura(SensorBrazoRobotico):
    if SensorBrazoRobotico:
        print("Lectura de sensores: ")
        for lectura in SensorBrazoRobotico:
            print(f"Sensor N° {lectura}")
    
def agregarLectura(SensorBrazoRobotico):
    lectura = float(input("Ingrese la lectura del sensor N°: "))
    SensorBrazoRobotico.append(lectura)
    print(lectura)
    
def visualizarPromedio(SensorBrazoRobotico):
    promedio = float(sum(SensorBrazoRobotico)/len(SensorBrazoRobotico))
    print(f"El promedio de las lecturas es de: {promedio}N") #PENDIENTE 
    
def MayorLectura(SensorBrazoRobotico):
    mayorLectura = max(SensorBrazoRobotico)
    print(f"La mayor lectura registrada es de: {mayorLectura}N")
    
def SensoresInferioresA5(SensorBrazoRobotico):
    print("Sensores con lectura inferior a 5 newtowns:" )
    for lectura in SensorBrazoRobotico:
        if lectura < 5:
            print(f"Sensor N° {lectura}")

    #sensoresInferiores = (lectura for lectura in SensorBrazoRobotico if lectura < 5)
    #print(f"Los sensores con lectura inferior a 5 newtowns son: {sensoresInferiores}")
    
def eliminarLectura(SensorBrazoRobotico):
    sensor = int(input("Ingrese el número del sensor que desea eliminar: "))
    SensorBrazoRobotico.remove(sensor)
    print("Lectura eliminada correctamente")
    
while True:
    print("MENU DE OPCIONES")
    print("1. Cargar lecturas de fuerza de sensores")
    print("2. Mostrar lecturas de sensores")
    print("3. Agregar lectura de un nuevo sensor")
    print("4. Visualizar la fuerza promedio")
    print("5. Ver la mayor lectura registrada")
    print("6. Calcular sensores con lectura inferior a 5 newtowns")
    print("7. Eliminar la lectura de un sensor específico")
    print("8. Ajustar lecturas por encima de 20 newtons")
    print("0. Salir")
    
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        cargarLecturas(SensorBrazoRobotico)
    elif opcion == 2:
        mostrarLectura(SensorBrazoRobotico)
    elif opcion == 3:
        agregarLectura(SensorBrazoRobotico)
    elif opcion == 4:
        visualizarPromedio(SensorBrazoRobotico)
    elif opcion == 5:
        MayorLectura(SensorBrazoRobotico)
    elif opcion == 6:
        SensoresInferioresA5(SensorBrazoRobotico)
    elif opcion == 7:
        eliminarLectura(SensorBrazoRobotico)
    elif opcion == 0:
        print("Saliendo del programa...")
        break
    else:
        ("Ingrese un número válido")
        