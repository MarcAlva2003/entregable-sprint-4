import csv


def abrirArchivoCSV(nombreArchivo):
    archivo = open(nombreArchivo, 'r')
    reader = csv.reader(archivo)
    header = []
    listado = []
    contador = 0
    for row in reader:
        if contador == 0:
            header = row
            contador += 1
        else: 
            listado.append(row)
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

#StartApp()

#------------------------------------------------------------------------------------------------

def ingresarValores():
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

def abrirArchivoCSV(nombreArchivo):
    """Abre el archivo y retorna el encabezado y crea una lista con los datos """
    archivo = open(nombreArchivo, 'r')
    reader = csv.reader(archivo)
    header = []
    listado = []
    contador = 0
    for row in reader:
        if contador == 0:
            header = row
            contador += 1
        else: 
            listado.append(row)
    return [header] + listado

def iniciarData():
    """Confirma el nombre del Archivo y llama a la funcion "Abrir archivo" """
    validacion_archivo = input('Si el nombre del archivo a trabajar es data.csv ingrese SI de otra manera NO:  ')
    condicion = True
    while condicion:
        if validacion_archivo == 'SI' or validacion_archivo == 'si':
            condicion = False
            return abrirArchivoCSV('data.csv')
        elif validacion_archivo == 'NO' or validacion_archivo == 'no':
            nombreArchivo = input("Ingresa el nombre del archivo : ")
            condicion = False 
            return abrirArchivoCSV(nombreArchivo)

def variableDNI():
    """ ingresa el DNI y lo guarda en una variable """
    variable_dni = input("Numero DNI : ")
    while  not(str.isdigit(variable_dni)):
        print("Dni no valido")
        variable_dni = input("Numero DNI : ")        
    return variable_dni

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

def tipo_Salida():
    """Selecciona salida por pantalla o un archivo CSV """
    salida = input('ingresa "P" para Pantalla o "CSV" para obtener el archivo : ')
    while (salida != "P" and salida != "CSV") or salida == "":
        salida = input('Ingrese un valor correcto(P o CSV)')
    return salida

def dato_filtrado_por_dni(dni,datos):
    
    formato = '{opcion:^10s} {dato_buscado:^10s}'
    print('Ingrese el numero de la opcion que desee conocer:\n')
    print(formato.format(opcion = 'Opcion\n',dato_buscado =''))

    nro_opcion = -1
    for elemento in datos[0]:
        nro_opcion += 1
        print(formato.format(opcion=str(nro_opcion),dato_buscado=str(elemento)))
    
    condicion = True
    while condicion:
        indice_elegido = int(input('Ingresa el valor REY: '))
        if indice_elegido <= nro_opcion and indice_elegido >= 0: 
            condicion = False
        else:
            print('Opcion no valida, vuelva a ingresar la opcion')

    indice = indice_elegido
    print('Este es el valor ingresado',indice)

    for fila in datos:
        if dni in fila:
            return fila[indice]

def StartApp2():
    """Inicia la App"""
    lista_datos = iniciarData()
    dni_ingresado = variableDNI()
    dato_filtrado = dato_filtrado_por_dni(dni_ingresado,lista_datos)

    #filtrado()


    #salida = tipo_Salida()
    
    
    # data = abrirArchivoCSV(valores[0])
    # if not(checkDni (valores[1], data[1], data[0].index("DNI"), data[0].index("NroCheque"))) :
    #     print ("El numero de cheque se repite con el mismo DNI")

StartApp2()