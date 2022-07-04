import csv
import datetime
from datetime import date

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
        if validacion_archivo.upper() == 'SI':
            condicion = False
            return abrir_guardar_datos('data.csv')
        elif validacion_archivo.upper() == 'NO':
            condicion = False 
            nombreValido = False
            while not(nombreValido):
                nombreArchivo = input("Ingresa el nombre del archivo : ")
                try:
                    file = open(nombreArchivo, 'r')
                    file.close()
                    nombreValido = True
                except:
                    nombreArchivo = input("Archivo no encontrado, vuelva a ingresar el nombre: ")
            return abrir_guardar_datos(nombreArchivo)
        else:
            validacion_archivo = input("Si el nombre del archivo a trabajar es data.csv ingrese SI de otra manera NO: ")

def verificarDNI(dni_Ingresado):
    valido = True
    
    if not(str.isdigit(dni_Ingresado)) or not(len(dni_Ingresado) < 11) or not(len(dni_Ingresado) > 6):
        valido = False
    
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

    while (salida.upper() != "P" and salida.upper() != "CSV") or salida == "":
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

def obtenerEstadoCheque():
    """Obtiene a partir de un dni y el tipo de cheque su estado"""
    estadoCheque = input("Estado PENDIENTE (P), APROBADO (A), RECHAZADO (R) : ")
    while estadoCheque.upper() != "P" and estadoCheque.upper() != "A" and estadoCheque.upper() != "R" and estadoCheque != "" :
        estadoCheque = input('Ingrese un valor correcto(PENDIENTE, APROBADO O RECHAZADO)')
    if estadoCheque.upper() == 'P':
        return 'PENDIENTE'
    elif estadoCheque.upper() == 'A':
        return 'APROBADO'
    return 'RECHAZADO'

def obtenerTipoCheque():
    """Ingreso de tipo de cheque"""
    tipoCheque = input("Cheque EMITIDO (E) o DEPOSITADO (D)? : ")
    while (tipoCheque.upper() != "E" and tipoCheque.upper() != "D") or tipoCheque == "":
        tipoCheque = input('Ingrese un valor correcto (EMITIDO (E) o DEPOSITADO (D)): ')
    if tipoCheque.upper() == 'E':
        return 'EMITIDO'
    return 'DEPOSITADO'

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
    respuestaValida = False
    ingresarFecha = input('¿Desea ingresar fecha de inicio y fecha de vencimiento? S/N: ')
    while not(respuestaValida):
        if(ingresarFecha.upper()  == 'S'):
            fechaInicio = validarFechaInicio()
            fechaVto = validarFechaVto()
            respuestaValida = True
        elif ingresarFecha.upper()  == 'N':
            respuestaValida = True
            return ["",""]
        else:
            ingresarFecha = input('¿Desea ingresar fecha de inicio y fecha de vencimiento? S/N: ')
    return [fechaInicio, fechaVto] 

def retornarDataCSV(header, data, dni):
    """Crear archivo csv y agregarle los datos filtrados"""
    fechaActual = str(date.today())
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
    """Retornar datos filtrados por consola"""
    print(header)
    for row in data:
        print(row)

def StartApp():
    """Inicia la App"""
    lista_datos = iniciarData() # LISTO
    dni_ingresado = variableDNI() # LISTO
    salida = tipo_Salida() # LISTO
    tipoCheque = obtenerTipoCheque() # LISTO
    estadoCheque = obtenerEstadoCheque() #  LISTO
    rangoFecha = obtenerRangoFecha() #  LISTO
    if checkDni(dni_ingresado, lista_datos[1], lista_datos[0].index("DNI"), lista_datos[0].index("NroCheque")):
        dataFiltrada = filtro(dni_ingresado, tipoCheque, estadoCheque, rangoFecha[0], rangoFecha[1], lista_datos)
        if len(dataFiltrada) > 0:
            if salida.upper() == 'CSV':
                retornarDataCSV(lista_datos[0], dataFiltrada, dni_ingresado)
            else:
                retornarDataConsola(lista_datos[0], dataFiltrada)
        else:
            print('No se ha encontrado ningun cheque, por favor, intente con otros parametros.')
StartApp()

############     FUNCIONES EXTRAS     #############
############     FUNCIONES EXTRAS     #############
############     FUNCIONES EXTRAS     #############

""" Son funciones pensadas para que un trabajador del banco busque los datos del cliente a partir de su dni"""

def dato_filtrado_por_dni(dni,datos):
    """Toma un dni y una lista de datos y retorna la variable buscada"""

    print('Desea conocer otra dato?')
    respuesta = input('complete si o no: ')
    if respuesta == 'SI' or respuesta == 'si':
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
                print('Nro cheque: ',fila[0],6*' ',datos[0][indice_elegido], ":  " ,fila[indice_elegido])


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

def Consulta_cheque(dni_ingresado,lista_datos):
    print('Desea consultar el estado de un cheque?')
    respuesta = input('ingrese si o no: ')
    if respuesta.upper() == 'SI':
        Estado_de_cheques(dni_ingresado,lista_datos)
        


def StartAppExtra():
    """Inicia la App Extra"""

    lista_datos = iniciarData()
    dni_ingresado = variableDNI()
    Estado_cheque = Consulta_cheque(dni_ingresado,lista_datos)
    Otra_informacion = dato_filtrado_por_dni(dni_ingresado,lista_datos)

StartAppExtra()