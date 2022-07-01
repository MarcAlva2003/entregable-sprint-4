import csv




def ingresarValores():
    nombreArchivo = input("Ingresa el nombre del archivo : ")
    dni = input('Ingrese el DNI : ')
    while not( str.isdigit(dni)):
        input("Ingrese un DNI Valido : ")
    salida = input('ingresa "P" para Pantalla o "CSV" para obtener el archivo : ')
    while (salida != "P" and salida != "CSV") or salida == "":
        salida = input('Ingrese un valor correcto(P o CSV)')
    tipoCheque = input("Cheque EMITIDO o DEPOSITADO? : ")
    while (tipoCheque != "EMITIDO" and tipoCheque != "DEPOSITADO") or tipoCheque == "":
        tipoCheque = input('Ingrese un valor correcto(EMITIDO O DEPOSITADO)')
    estadoCheque = input("PENDIENTE, APROBADO, RECHAZADO : ")
    while estadoCheque!= "PENDIENTE" and estadoCheque != "APROBADO" and estadoCheque != "RECHAZADO" and estadoCheque != "" :
        estadoCheque = input('Ingrese un valor correcto(PENDIENTE, APROBADO O RECHAZADO)')
    fechaInicio = input("Inicio: DD-MM-AAAA ")
    fechaVencimiento = input("Vencimiento: DD-MM-AAAA ")
    rangoFecha = fechaInicio + ":" + fechaVencimiento

    return [nombreArchivo, dni, salida, tipoCheque, estadoCheque, rangoFecha]


    # a. Nombre del archivo csv.
    # b. DNI del cliente donde se filtraran.
    # c. Salida: PANTALLA o CSV
    # d. Tipo de cheque: EMITIDO o DEPOSITADO
    # e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
    # f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)
    
    # return nombre (Lista con las respuestas de los inputs)
    # valores = ['Nombre archivo', dni]
    pass

def abrirArchivoCsv(nombre):
    archivo = open(nombre,'r')
    reader = csv.reader(archivo)


def ingresarDni():
    dniIngresado = int(input("Ingrese DNI"))

# def Prueba():
#     variable = input('Ingresa la variable REY: ')
#     contador=0
#     for row in reader:
#         if contador == 0:
#             posicion = row.index(variable)
#             contador += 1

#         if dni in row:
#             print(row[posicion])

def StartApp():
    valores = ingresarValores()
    print(valores)
    # data : [header, content] = abrirArchivoCsv(valores[0])
    # if(checkDni(dni, content) -> return boolean)
    #   true -> sigue
    #   false -> tire error
    # dataFiltrada = obtenerDataFiltrada(valores[], content[]) -> Obtener cheques que cumplan con los filtros
                #  content = filtrarPorDni(valores[1], content)
                #  content = filtrarPorTipoCheque(valores[3], content)
                #  if(data[4] -> es un input salteado -> false -> usar filtro
                #   data[4] -> es un input salteado -> true -> NO usar filtro
                    
                #   data[5] -> es un input salteado -> false -> usar filtro
                #   data[5] -> es un input salteado -> true -> NO usar filtro)

StartApp()