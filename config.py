#configuracion del proyecto (FLASK)

class DevelopmentConfig(): #Clase de configuracion
    DEBUG =True #modo debug, permite ver los errores en el navegador

#Diccionario
config = {
    'development':DevelopmentConfig #permite acceder a la clase de configuracion
}