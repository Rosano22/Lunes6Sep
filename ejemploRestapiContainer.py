
from flask import Flask,request
import pymysql
import pygal

def grafico(titulo, valoresX, valoresY, archivo):
    grafico=pygal.Bar(width=500, height=300, explicit_size=True)
    grafico.x_labels=valoresX
    grafico.add(titulo, valoresY)
    grafico.render_to_file('./static/imagenes/' + archivo)

aplicacion=Flask(__name__)

conexion=pymysql.connect(host='serverbdparapython',user='root',
passwd='123',db='datossensores2')
elcursor=conexion.cursor()


@aplicacion.route('/')
def saludar():
    return 'Hallo'


@aplicacion.route('/anfrage1')
def hacerConsulta1():
    datos = ''    
    elcursor.execute("select * from sensor")
    lineas=elcursor.fetchall()

    datos = ('<table border = 1><thead><tr><td>ID</td>'
    +'<td>Sensor Name</td><td>Unit</td></tr></thead><tbody>')
    
    for linea in lineas:
        datos = (datos + '<tr><td>' + str(linea[0]) + '</td><td>' + 
        str(linea[1]) + '</td><td> ' + str(linea[2]) + '</td></tr><br>')
    
    datos = datos + '</tbody></table>'
    datos = datos.replace('tr>','tr align="center">')
        
    return datos


@aplicacion.route('/anfrage2')
def hacerConsulta2():
    datos = ''    
    elcursor.execute("select * from lecturassensor")
    lineas=elcursor.fetchall()
    fechahora=[]
    valores=[]
    
    datos = ('<table border = 1><thead><tr><td>ID</td>'
    +'<td>ID Sensor</td><td>Date & Time</td>'
    +'<td>Value</td> </tr></thead><tbody>')
    
    for linea in lineas:
        datos = (datos + '<tr><td>' + str(linea[0]) + '</td><td>' + 
        str(linea[1]) + '</td><td> ' + str(linea[2]) + '</td><td> ' 
        + str(linea[3]) + '</td></tr><br>')
        fechahora.append(str(linea[2]))
        valores.append(linea[3])
    
    datos = datos + '</tbody></table>'
    datos = datos.replace('tr>','tr align="center">')

    grafico('Sensor', fechahora, valores, 'graficosensor.svg')
    datos=datos + ('<br><embed type ="image/svg+xml"'
    + 'src="/static/imagenes/graficosensor.svg"/>')
    
    return datos

@aplicacion.route('/Martes')
def concepToMartes():
    return 'es el 2do dia de la semana'

@aplicacion.route('/python')
def conceptoPython():
    return 'es un lenguaje de programacion'

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
    aplicacion.run(host='0.0.0.0',port=4005, debug=True)

    elcursor.close()
    conexion.close()
    



