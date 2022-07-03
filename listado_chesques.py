import csv


# def checkDni (dni, content, indexDNI, indexNroCheque) :
#     # print (dni, content, indexDNI, indexNroCheque)
#     nrosCheques = []
#     for row in content: 
#         if row[indexDNI] == dni:
#             if row[indexNroCheque] in nrosCheques:
#                 return False
#             else: 
#                 nrosCheques.append(row[indexNroCheque]) 
    
#     return True

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

def abrirArchivoCSV(nombreArchivo):
    """Abre el archivo y retorna el encabezado y crea una lista con los datos """
    archivo = open(nombreArchivo, 'r')
    reader = csv.reader(archivo)
    header = []
    listado = []
    condision = True
    for row in reader:
        if condision == 0:
            header = row
            condision = False
        else: 
            listado.append(row)
    return [header] + listado


def abrirArchivoCSV2(nombreArchivo):
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


def iniciarData2():
    """Confirma el nombre del Archivo y llama a la funcion "Abrir archivo" """
    validacion_archivo = input('Si el nombre del archivo a trabajar es data.csv ingrese SI de otra manera NO:  ')
    condicion = True
    while condicion:
        if validacion_archivo == 'SI' or validacion_archivo == 'si':
            condicion = False
            return abrirArchivoCSV2('data.csv')
        elif validacion_archivo == 'NO' or validacion_archivo == 'no':
            nombreArchivo = input("Ingresa el nombre del archivo : ")
            condicion = False 
            return abrirArchivoCSV2(nombreArchivo)


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
                print ("El numero de cheque se repite con el mismo DNI")
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
    """Toma un dni y una lista de datos y retorna la variable buscada"""
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

    for fila in datos:
        if dni in fila:
            return fila[indice_elegido]

# # # # # # # # # # # 
# INICIO FILTRO
# # # # # # # # # # # 

def isDni(dni, indexDni, row):
    pass

def filtrarPorTipo(tipo, indexTipo, data):
    pass

def filtro(dni, tipoCheque, estadoCheque, rangoFecha, data):
    """Filtra la data que se obtinee de data.csv utilizando los parametros ingresados por el cliente"""
    lineasARetornar = []
    indexDni = data[0].index("DNI")
    indexTipo  = data[0].index('Tipo')
    
    # lista = filtrarDni(data, dni, indexDni)
    # lista = filtratTipoCheque(lista, tipo indexTIPO)
    # if not(fecha == ''):
    #     lista = filtratFecha(lista, tipo indexTIPO)
    # retutn listra
    

    for row in data[1]:
        if (row[indexDni] == dni) and (row[indexTipo] == tipoCheque):
            lineasARetornar.append(row)
    
    return lineasARetornar

# # # # # # # # # # # 
# FIN FILTRO
# # # # # # # # # # # 


def dato_filtrado_por_dni_2(dni,lista_datos,dato):
    """Toma un dni y una lista de lista_datos y retorna la variable buscada"""
    
    print(lista_datos[0])
    indice_dato = -1
    for elemento in lista_datos[0]:
        indice_dato += 1
        if elemento == dato:
            break

    indice_dni = -1
    for elemento in lista_datos[0]:
        indice_dato += 1
        print(elemento)
        if elemento == 'DNI':
            break

    lista_auxiliar = [] #lista donde se guardan los mismos datos solicitados para un DNI
    for fila in lista_datos[1]:
        if dni == fila[indice_dni]:
            lista_auxiliar.append(fila[indice_dato])
    return print(lista_auxiliar)


def obtenerTipoCheque():
    """Ingreso de tipo de cheque"""
    tipoCheque = input("Cheque EMITIDO o DEPOSITADO? : ")
    while (tipoCheque != "EMITIDO" and tipoCheque != "DEPOSITADO") or tipoCheque == "":
        tipoCheque = input('Ingrese un valor correcto(EMITIDO O DEPOSITADO)')
    return tipoCheque


def ontenerEstadoCheque(dni,tipo_cheque):
    """Obtiene a partir de un dni y el tipo de cheque su estado"""

    # estadoCheque = input("PENDIENTE, APROBADO, RECHAZADO : ")
    # while estadoCheque != "PENDIENTE" and estadoCheque != "APROBADO" and estadoCheque != "RECHAZADO" and estadoCheque != "" :
    #     estadoCheque = input('Ingrese un valor correcto(PENDIENTE, APROBADO O RECHAZADO)')
    # return estadoCheque


def obtenerRangoFecha():
    """Asigna manualmente una fecha de inicio y vencimiento a un cheque"""
    fechaInicio = input("Inicio: DD-MM-AAAA ")
    fechaVencimiento = input("Vencimiento: DD-MM-AAAA ")
    rangoFecha = fechaInicio + ":" + fechaVencimiento
    return rangoFecha

#def cerrar_archivo():
    #lista_datos2.close()
    #CREAR UNA FUNCION QUE CIERRE EL ARCHIVO O ABRIR CON WITH

def StartApp2():
    """Inicia la App"""
    # lista_lista_datos = iniciarData()
    lista_datos2 = iniciarData2() # = [ header, content[] ]
    dni_ingresado = variableDNI() # = dni
    #dato_filtrado_por_dni_2(dni_ingresado,lista_datos2,'Estado') #PAULO (A BORRAR)
    salida = tipo_Salida() # = salida
    tipoCheque = obtenerTipoCheque() # = tipoCheque
    estadoCheque = ontenerEstadoCheque(dni_ingresado,tipoCheque) # = estadoCheque o ''
    rangoFecha = obtenerRangoFecha() # = rangoFecha o ''
    checkDni(dni_ingresado, lista_datos2[1], lista_datos2[0].index("DNI"), lista_datos2[0].index("NroCheque"))
    dataFiltrada = filtro(dni_ingresado, tipoCheque, estadoCheque, rangoFecha, lista_datos2)
    for row in dataFiltrada:
        print(row)
    
    # NO BORRAR XD
    # for row in dataFiltrada:
    #     indice = 0
    #     cadena = ''
    #     for item in row:
    #         cadena += lista_datos2[0][indice] + ' : ' + item + ' - '
    #         indice += 1
    #     print(cadena)

    header =  ['NroCheque','CodigoBanco','CodigoScurusal','NumeroCuentaOrigen','NumeroCuentaDestino','Valor','FechaOrigen','FechaPago','DNI','Tipo','Estado']
    dataFiltradaMock = [
        ['0002','55','44','2432432423','343434343','5559,76','1620183371','1620183371','23665789','EMITIDO','PENDIENTE'],
        ['0002','55','44','2432432423','343434343','5559,76','1620183371','1620183371','23665789','EMITIDO','PENDIENTE'],
        ['0002','55','44','2432432423','343434343','5559,76','1620183371','1620183371','23665789','EMITIDO','PENDIENTE'],
        ['0002','55','44','2432432423','343434343','5559,76','1620183371','1620183371','23665789','EMITIDO','PENDIENTE'],
        ]

    # mostrarValres(dataFiltradaMock, salida);


    # dato_filtrado = dato_filtrado_por_dni(dni_ingresado,lista_datos)
    # print(dato_filtrado)

    # data = abrirArchivoCSV(valores[0])
    # if not(checkDni (valores[1], data[1], data[0].index("DNI"), data[0].index("NroCheque"))) :
    #     print ("El numero de cheque se repite con el mismo DNI")

StartApp2()