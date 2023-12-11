from flask import Blueprint, render_template, request, url_for
from flask_paginate import Pagination, get_page_args
from werkzeug.utils import redirect
from scr.models.entities.attention_control import AttentionControl

from scr.models.model_attention_control import ModelAttentionControl
#Blueprint: es una clase que nos permite crear un conjunto de rutas y asociarlas a un mismo controlador

#crear una instancia de Blueprint
main = Blueprint('attention_control_bp', __name__) #nombre del blueprint y el nombre del archivo

#Función auxiliar

def get_attention_control_data_from_request():
    if request.method == 'POST':
        fecha = request.form['fecha']
        nombres = request.form['nombres']
        hora_ingreso = request.form['hora_ingreso']
        hora_salida = request.form['hora_salida']
        estado_polo = request.form.get('polo_gift', False)
        print(estado_polo)
        
        if (estado_polo == 'on'):
            estado_polo = True
        else:
            estado_polo = False
            
        estado_keychain = request.form.get('keychain_gift', False)
        
        if (estado_keychain == 'on'):
            estado_keychain = True
        else:
            estado_keychain = False
        
        catalog_book = request.form['catalog_book']
        return fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book


#Select
@main.route('/') #decorador que permite crear una ruta
def Index():
    #Obtener paginación de la URL actual
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page') #paginacion, donde page es el numero de pagina, per_page es el numero de registros por pagina y offset es el numero de registros que se van a mostrar
    
    data = ModelAttentionControl.get_attention_control_list()
    #Calcular el número total de elementos y la lista de elementos para la página actual
    total = len(data)
    pagination_data = data[offset: offset + per_page] #paginacion de los datos
    #Crear objeto pagination
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap5') #objeto de paginacion
    
    #print(data)
    return render_template('index.html', attentions = pagination_data, pagination=pagination) #renderizar la plantilla index.html y enviar la lista de datos

#Insert
@main.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        #Obtenemos los datos del form por medio de la función auxiliar
        fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book = get_attention_control_data_from_request()
        attention_control = AttentionControl(fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book)
        affected_rows = ModelAttentionControl.insert_attention_control(attention_control)

        if affected_rows == 1:
            print('Registro insertado con éxito')
        else:
            print('Ocurrió un error al insertar el registro')
        #redirect redirecciona a la ruta especificada
        #url_for permite obtener la ruta de una función especifica en base a su nombre
        #attention_control_bp es el nombre del blueprint, nombre de la ruta a la que se va redirigir e Index es el nombre de la función
        return redirect(url_for('attention_control_bp.Index')) 
#Update
@main.route('/update', methods=['POST'])
def update():
    if request.method == "POST":
        fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book = get_attention_control_data_from_request()
        idKey = request.form['id']
        attention_control = AttentionControl(fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book, idKey)
        affected_rows = ModelAttentionControl.update_attention_control(attention_control)
        
        if affected_rows == 1:
            print('Registro actualizado con éxito')
        else:
            print('Ocurrió un error al actualizar el registro')
        
        return redirect(url_for('attention_control_bp.Index')) 

#Delete
@main.route('/delete/<string:id>')
def delete(id):
    affected_rows = ModelAttentionControl.delete_attention_control(id)
    
    if affected_rows == 1:
        print('Registro eliminado con éxito')
    else:
        print('Ocurrió un error al eliminar el registro')
    return redirect(url_for('attention_control_bp.Index'))