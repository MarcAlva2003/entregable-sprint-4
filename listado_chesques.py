import csv
import datetime

def abrir_guardar_datos(nombreArchivo):
    """Abre el archivo, guarda los datos en una lista y lo cierra"""

    archivo = open(nombreArchivo, 'r')
    reader = csv.reader(archivo)
    header = []
    listado = []
    contador = True

    for row in reader:
        if contador:
            header = row
            contador = False
        else: 
            listado.append(row)

    archivo.close()

    return [header, listado]

def iniciarData():
    """Confirma el nombre del Archivo y llama a la funcion "Abrir archivo" """

    validacion_archivo = input('Si el nombre del archivo a trabajar es data.csv ingrese SI de otra manera NO:  ')
    condicion = True

    while condicion:
        if validacion_archivo == 'SI' or validacion_archivo == 'si':
            condicion = False
            return abrir_guardar_datos('data.csv')
        elif validacion_archivo == 'NO' or validacion_archivo == 'no':
            nombreArchivo = input("Ingresa el nombre del archivo : ")
            condicion = False 
            return abrir_guardar_datos(nombreArchivo)

def verificarDNI(dni_Ingresado):
    valido = True
    print(len(dni_Ingresado))
    if not(str.isdigit(dni_Ingresado)) or not(len(dni_Ingresado) < 11) or not(len(dni_Ingresado) > 6):
        valido = False
    print(len(dni_Ingresado))
    return valido

def variableDNI():
    """ ingresa el DNI y lo guarda en una variable """

    variable_dni = input("Numero DNI : ")

    while not(verificarDNI(variable_dni)):
        print("Dni no valido")
        variable_dni = input("Numero DNI : ")
    
    return variable_dni


def checkDni (dni, content, indexDNI, indexNroCheque):
    """Corrobora si el cheque esta repetido para el mismo DNI"""
    nrosCheques = []
    for row in content: 
        if row[indexDNI] == dni:
            if row[indexNroCheque] in nrosCheques:
                print ("El numero de cheque se repite con el mismo DNI")
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

# # # # # # # # # # # 
# INICIO FILTRO     #
# # # # # # # # # # # 

def filtroPorDni(dni, indexDni, data):
    """Retorna las filas en las que el DNI conicida"""
    lineasARetornar  =[]
    for row in data:
        if (row[indexDni] == dni):
            lineasARetornar.append(row)
    return lineasARetornar

def filtrarPorTipo(tipo, indexTipo, data):
    """Retorna las filas en las que el Tipo de cheque conicida"""
    lineasARetornar = []
    for row in data:
        if (row[indexTipo] == tipo):
            lineasARetornar.append(row)
    return lineasARetornar

def filtrarPorEstado(estadoCheque, indexEstado, data):
    """Retorna las filas en las que el Estado de cheque conicida"""
    lineasARetornar = []
    for row in data:
        if (row[indexEstado] == estadoCheque):
            lineasARetornar.append(row)
    return lineasARetornar

def filtrarPorFecha(fechaInicio, fechaFin, indexFechaInicio, indexFechaFin, data):
    """Retorna las filas en las que el rango de fecha coincida"""
    lineasARetornar = []
    for row in data:
        if (row[indexFechaInicio] == fechaInicio and row[indexFechaFin] == fechaFin):
            lineasARetornar.append(row)
    return lineasARetornar

def filtro(dni, tipoCheque, estadoCheque, fechaInicio, fechaFin, data):
    """Retorna la data que se obtinee de data.csv utilizando los parametros ingresados por el cliente"""
    lineasARetornar = []
    indexDni = data[0].index("DNI")
    indexTipo  = data[0].index('Tipo')
    indexEstado  = data[0].index('Estado')
    indexFechaInicio = data[0].index('FechaOrigen')
    indexFechaFin = data[0].index('FechaPago')
    
    lineasARetornar = filtroPorDni(dni, indexDni, data[1])
    lineasARetornar = filtrarPorTipo(tipoCheque, indexTipo, lineasARetornar)
    # OPCIONALES
    if not(estadoCheque == ''):
        lineasARetornar = filtrarPorEstado(estadoCheque, indexEstado, lineasARetornar)
    if not((fechaInicio == '') or (fechaFin == '')):
        lineasARetornar = filtrarPorFecha(fechaInicio, fechaFin, indexFechaInicio, indexFechaFin, lineasARetornar)


    return lineasARetornar

# # # # # # # # # # # 
# FIN FILTRO        #
# # # # # # # # # # # 

def ontenerEstadoCheque(dni,tipo_cheque):
    """Obtiene a partir de un dni y el tipo de cheque su estado"""

    estadoCheque = input("PENDIENTE, APROBADO, RECHAZADO : ")

    while estadoCheque != "PENDIENTE" and estadoCheque != "APROBADO" and estadoCheque != "RECHAZADO" and estadoCheque != "" :
        estadoCheque = input('Ingrese un valor correcto(PENDIENTE, APROBADO O RECHAZADO)')

    return estadoCheque
    

def obtenerTipoCheque():
    """Ingreso de tipo de cheque"""

    tipoCheque = input("Cheque EMITIDO o DEPOSITADO? : ")

    while (tipoCheque != "EMITIDO" and tipoCheque != "DEPOSITADO") or tipoCheque == "":
        tipoCheque = input('Ingrese un valor correcto(EMITIDO O DEPOSITADO)')

    return tipoCheque




def validarFechaInicio():
    """Verifica que la fecha de inicio del cheque sea Valida"""
    fechaInicio = input("Inicio : DD-MM-AAAA ")
    try:
        fechaSeparada = fechaInicio.split('-')
        fechaAlReves = fechaSeparada[2] + '-' + fechaSeparada[1] + '-' + fechaSeparada[0]
    except:
        
        fechaAlReves = ''
    fechaIncorrecta = True

    while fechaIncorrecta:
        try:    
            datetime.datetime.strptime(fechaAlReves, '%Y-%m-%d')
            fechaIncorrecta = False
            return fechaInicio
        except:
            fechaInicio = input("Ingrese una fecha de inicio Valida : DD-MM-AAAA ")
            try:
                fechaSeparada = fechaInicio.split('-')
                fechaAlReves = fechaSeparada[2] + '-' + fechaSeparada[1] + '-' + fechaSeparada[0]
            except:
                fechaAlReves = ''

def validarFechaVto():
    """Verifica que la fecha de vencimiento del cheque sea Valida"""
    fechaInicio = input("Vencimiento : DD-MM-AAAA ")
    try:
        fechaSeparada = fechaInicio.split('-')
        fechaAlReves = fechaSeparada[2] + '-' + fechaSeparada[1] + '-' + fechaSeparada[0]
    except:
        
        fechaAlReves = ''
    fechaIncorrecta = True

    while fechaIncorrecta:
        try:    
            datetime.datetime.strptime(fechaAlReves, '%Y-%m-%d')
            fechaIncorrecta = False
            return fechaInicio
        except:
            fechaInicio = input("Ingrese una fecha de vencimiento valida : DD-MM-AAAA ")
            try:
                fechaSeparada = fechaInicio.split('-')
                fechaAlReves = fechaSeparada[2] + '-' + fechaSeparada[1] + '-' + fechaSeparada[0]
            except:
                fechaAlReves = ''


def obtenerRangoFecha():
    """Retorna ambas fechas en una lista """
    ingresarFecha = input('¿Desea ingresar fecha de inicio y fecha de vencimiento?: S/N')
    if(ingresarFecha  == 'S'):
        fechaInicio = validarFechaInicio()
        fechaVto = validarFechaVto()
    else:
        return ["",""]

    return [fechaInicio, fechaVto] 


def retornarDataCSV(header, data, dni, fechaActual):
    archivoNuevo = open(dni+fechaActual+'.csv', 'w', newline='')
    archivo = csv.writer(archivoNuevo)

    iFechaInicio = header.index('FechaOrigen')
    iFechaFin = header.index('FechaPago')
    iValorCheque = header.index('Valor')
    iCuentaOrigen = header.index('NumeroCuentaOrigen')
    iCuentaDestino = header.index('NumeroCuentaDestino')


    cadenaContenido = ''
    cadenaHeader = ''
    cadenaHeader = header[iFechaInicio],header[iFechaFin],header[iValorCheque],header[iCuentaOrigen],header[iCuentaDestino]
    archivo.writerow(cadenaHeader)
    for row in data:
                cadenaContenido = row[iFechaInicio],row[iFechaFin],row[iValorCheque],row[iCuentaOrigen],row[iCuentaDestino]
                archivo.writerow(cadenaContenido)
    archivoNuevo.close()

def retornarDataConsola(header, data):
    print(header)
    for row in data:
        print(row)

def StartApp():
    """Inicia la App"""

    lista_datos = iniciarData() # = [ header, content[] ]
    dni_ingresado = variableDNI() # = dni
    salida = tipo_Salida() # = salida

    tipoCheque = obtenerTipoCheque() # = tipoCheque
    estadoCheque = ontenerEstadoCheque(dni_ingresado,tipoCheque) # = estadoCheque o ''
    rangoFecha = obtenerRangoFecha() # = rangoFecha o ''
    if checkDni(dni_ingresado, lista_datos[1], lista_datos[0].index("DNI"), lista_datos[0].index("NroCheque")):
        dataFiltrada = filtro(dni_ingresado, tipoCheque, estadoCheque, rangoFecha[0], rangoFecha[1], lista_datos)
        fechaActual = '03-07-2022'
        if salida == 'CSV':
            
            retornarDataCSV(lista_datos[0], dataFiltrada, dni_ingresado, fechaActual)
        else:
            retornarDataConsola(lista_datos[0], dataFiltrada)

StartApp()





############     FUNCIONES EXTRAS     #############

""" Son funciones pensadas para que un trabajador del banco busque los datos del cliente a partir de su dni"""

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

    for fila in datos[1]:
        if dni in fila:
            print(datos[0][indice_elegido], " :   " ,fila[indice_elegido])


def filtro_por_dni(dni,lista_datos,dato):
    """Toma un dni y una lista de lista_datos y retorna la variable buscada en una lista"""

    indice_dni = lista_datos[0].index('DNI')
    indice_dato = lista_datos[0].index(dato)

    lista_auxiliar = []
    for fila in lista_datos[1]:
        if dni == fila[indice_dni]:
            lista_auxiliar.append(fila[indice_dato])
    return lista_auxiliar

def Estado_de_cheques(dni,lista_de_datos):
    """retorna el estado de cheques para un mismo dni"""
    Nro_cheque = filtro_por_dni(dni,lista_de_datos,'NroCheque')
    Tipo_cheque = filtro_por_dni(dni,lista_de_datos,'Tipo')
    Estado_cheque = filtro_por_dni(dni,lista_de_datos,'Estado')

    formato = '{0:<15s} {1:<15s} {2:<15s}'

    print(formato.format('Nro Cheque','Tipo','Estado'))
    for posicion in range(0,len(Nro_cheque)):
        print(formato.format(Nro_cheque[posicion],Tipo_cheque[posicion],Estado_cheque[posicion]))

def StartAppExtra():
    """Inicia la App Extra"""

    lista_datos = iniciarData()
    dni_ingresado = variableDNI()
    Estado_de_cheques(dni_ingresado,lista_datos)
    dato_filtrado_por_dni(dni_ingresado,lista_datos)