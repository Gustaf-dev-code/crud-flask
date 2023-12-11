import mysql.connector

def get_connection():
    try:
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Kh1ng*7490@1963",
            database = "attention_client"
        )
    except mysql.connector.errors as err:
        raise err