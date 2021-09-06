#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     26/08/2021
# Copyright:   (c) LENOVO 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask,request
#import wikipedia
#from flask_mysqldb import MySQL

aplicacion=Flask(__name__)


@aplicacion.route('/')
def saludar():
    return 'hola'

@aplicacion.route('/Martes')
def concepToMartes():
    return 'es el 2do dia de la semana'

@aplicacion.route('/python')
def conceptoPython():
    return 'es un lenguaje de programacion'

@aplicacion.route('/lunes')
def conceptoLunes():
    return 'es el primer dia de la semana'


@aplicacion.route('/definicion')
def definiciones():
    #ip:puerto/definicion?c=byte
    concepto=request.args.get('c')
    respuesta=''
    if concepto=='byte':
        respuesta='8 bits'
    elif concepto=='bit':
        respuesta='unidad minima de info puede tener valores 0 o 1'
    else:
        respuesta='concepto no encontrado'
    return respuesta




if __name__=='__main__':
    aplicacion.run(host='0.0.0.0',port=4005)
