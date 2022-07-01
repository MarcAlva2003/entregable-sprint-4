import csv

def ingresarValores():
    nombreArchivo = input("Ingresa el nombre del archivo : ")
    dni = input('Ingrese el DNI : ')
    while not( str.isdigit(dni)):
        dni = input("Ingrese un DNI Valido : ")
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

def abrirArchivoCSV (nombreArchivo) :
    archivo = open (nombreArchivo, 'r')
    reader = csv.reader (archivo)
    header = []
    listado = []
    contador = 0
    for row in reader:
        if contador == 0:
            header = row
            contador += 1
        else: 
            listado. append (row)
    return [header, listado]

def checkDni (dni, content, indexDNI, indexNroCheque) :
    # print (dni, content, indexDNI, indexNroCheque)
    nrosCheques = []
    for row in content: 
        if row[indexDNI] == dni:
            if row[indexNroCheque] in nrosCheques:
                return False
            else: 
                nrosCheques.append(row[indexNroCheque]) 
    
    return True

def StartApp():
    valores = ingresarValores()
    data = abrirArchivoCSV(valores[0])
    if not(checkDni (valores[1], data[1], data[0].index("DNI"), data[0].index("NroCheque"))) :
        print ("El numero de cheque se repite con el mismo DNI")
    # if(checkDni(valores[1], data[1]) -> return boolean)
    #   true -> sigue
    #   false -> tire error
    # dataFiltrada = obtenerDataFiltrada(valores[], content[]) -> Obtener cheques que cumplan con los filtros
                #  content = filtrarPorDni(valores[1], content)
                #  content = filtrarPorTipoCheque(valores[3], content)
                #  if(data[4] -> es un input salteado -> false -> usar filtro
                #   data[4] -> es un input salteado -> true -> NO usar filtro
                #   data[5] -> es un input salteado -> false -> usar filtro
                #   data[5] -> es un input salteado -> true -> NO usar filtro)

    # retornarValores(dataFiltrada, valores[2])

StartApp()