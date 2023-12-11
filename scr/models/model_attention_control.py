from scr.database.dbconnect import get_connection

class ModelAttentionControl:
    
    @staticmethod #permite que el metodo se pueda ejecutar sin instanciar la clase
    #metodo para obtener la lista de clientes
    def get_attention_control_list():
        try:
            connection = get_connection()
            cursor = connection.cursor() #Un cursor es un objeto que permite recorrer los registros de una tabla
            query = "SELECT ID, FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK FROM attention_control"
            cursor.execute(query) 
            result = cursor.fetchall() # fetchall() retorna uma lista de tuplas
            
            # Convertir la lista de tuplas en una lista de diccionarios
            keys = ['id', 'fecha', 'nombres', 'hora_ingreso', 'hora_salida', 'polo_gift', 'keychain_gift', 'catalog_book']
            result_dict = [dict(zip(keys, values)) for values in result]
            
            #print(result_dict)
            return result_dict
        except Exception as err:
            raise err
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    #metodo para insertar un cliente
    @staticmethod
    def insert_attention_control(attention_control):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = "INSERT INTO attention_control (FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (attention_control.fecha, attention_control.nombres, attention_control.hora_ingreso, attention_control.hora_salida, attention_control.polo_gift, attention_control.keychain_gift, attention_control.catalog_book)
            cursor.execute(query, data)
        except Exception as err:
            raise err
        except:
            connection.rollback() #revertir la transaccion
            affected_rows = 0
        else:
            connection.commit() #confirmar la transaccion
            affected_rows = cursor.rowcount
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                return affected_rows
    
    #metodo para actualizar un cliente
    @staticmethod
    def update_attention_control(attention_control):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = "UPDATE attention_control SET FECHA = %s, NOMBRES = %s, HORA_INGRESO = %s, HORA_SALIDA = %s, POLO_GIFT = %s, KEYCHAIN_GIFT = %s, CATALOG_BOOK = %s WHERE ID = %s"
            data = (attention_control.fecha, attention_control.nombres, attention_control.hora_ingreso, attention_control.hora_salida, attention_control.polo_gift, attention_control.keychain_gift, attention_control.catalog_book, attention_control.id)
            cursor.execute(query, data)
        except Exception as err:
            raise err
        except:
            connection.rollback() #revertir la transaccion
            affected_rows = 0
        else:
            connection.commit() #confirmar la transaccion
            affected_rows = cursor.rowcount
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                return affected_rows
        
    #metodo para eliminar un cliente
    @staticmethod
    def delete_attention_control(id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = "DELETE FROM attention_control WHERE ID = %s"
            data = (id, )
            cursor.execute(query, data)
        except:
            connection.rollback() #revertir la transaccion
            affected_rows = 0
        else:
            connection.commit() #confirmar la transaccion
            affected_rows = cursor.rowcount
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                return affected_rows 