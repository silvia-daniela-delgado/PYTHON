print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-[CENSO DE ALUMNOS 2023]-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Ingrese (si) para continuar: ")
respuesta = input("Desea comenzar el censo (si/no)?: ")

# Inicializamos las variables para contadores y promedios
cant_internet = 0
cant_computadora = 0
cant_alumnos = 0
total_edades = 0
cant_casas = 0
cant_deptos = 0
cant_otro = 0
mayor_cant_computadoras = 0
mas_alum_compu = 0
legajo_mayor_computadoras = ""
apellido_mayor_computadoras = ""
nombre_mayor_computadoras = ""
lista =[]
cuenta = 0
# Inicio del loop para ingresar datos de los alumnos
while True:
    cuenta += 1
    if respuesta.lower() != "si":
        break             
    legajo = input("Ingrese el número de legajo del alumno: ")
    lista.append(legajo)   
    apellido = input("Ingrese el apellido del alumno: ")
    lista.append(apellido)
    nombre = input("Ingrese el nombre del alumno: ")
    lista.append(nombre)
    try:
        edad = int(input("Ingrese la edad del alumno: "))
        lista.append(edad)
    except ValueError:
        print("Error: debe ingresar un número entero.")
        continue
        if edad < 0:
            print("Error: la edad debe ser un número positivo.")
            
        break
    internet = input("¿Tiene conexión a internet en su hogar? (si o no): ")
    computadora = input("¿Tiene computadora en su hogar? (si o no): ")
    if computadora.lower() == "si":
        cant_computadora += 1
        cant_computadoras = int(input("¿Cuántas computadoras tiene en su hogar?: "))
 
        if cant_computadoras > mayor_cant_computadoras:
            mayor_cant_computadoras = cant_computadoras
            legajo_mayor_computadoras = legajo
            apellido_mayor_computadoras = apellido
            nombre_mayor_computadoras = nombre
           
    # Contadores para tipos de vivienda
    vivienda = input("¿En qué tipo de vivienda reside? (Casa, Departamento, Otro): ")
    if vivienda.lower() == "casa":
        cant_casas += 1
    elif vivienda.lower() == "departamento":
        cant_deptos += 1
    else:
        cant_otro += 1
    # Contadores y sumas para promedios
    if internet.lower() == "si":
        cant_internet += 1
    cant_alumnos += 1
    total_edades += edad
    print("  ")
    print("------------------------------------------------------------------------------")
    respuesta = input("Desea continuar el censo? (si/no): ")
    print("cantidad de alumnos censados hasta el momento",cuenta)
    print("  ")
# Cálculo de resultados
porcentaje_casas = (cant_casas / cant_alumnos) * 100
porcentaje_deptos = (cant_deptos / cant_alumnos) * 100
porcentaje_otro = (cant_otro / cant_alumnos) * 100
promedio_edades = total_edades / cant_alumnos
print("----------------------------------------------------------------------------------")
# Mostramos los resultados
print("Cantidad de alumnos con conexión a internet en su hogar: ", cant_internet)
print("  ")
print("Cantidad de alumnos con computadora en su hogar: ", cant_computadora)
print("  ")
if legajo_mayor_computadoras != "":
    print("El alumno con más computadoras es: ", legajo_mayor_computadoras, apellido_mayor_computadoras, nombre_mayor_computadoras)

print("  ")
print("Porcentaje de alumnos en casa: ", porcentaje_casas)
print("  ")
print("Porcentaje de alumnos en departamento: ", porcentaje_deptos)
print("  ")
print("Porcentaje de alumnos en otro tipo de vivienda: ", porcentaje_otro)
print("  ")
print("Promedio de edad de los alumnos censados: ", promedio_edades)
print("  ")
try:
    print("El segundo alumno ingresado es: ", lista[4], lista[5], lista[6], lista[7])
    print("  ")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-[GRACIAS POR PARTICIPAR DEL CENSO 2023]-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
except IndexError:
    print("  ")
    print("No figura un segundo alumno en sistema")
    print("  ")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-[GRACIAS POR PARTICIPAR DEL CENSO 2023]-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")    
