import mysql.connector

def get_connection():
    try:
        return mysql.connector.connect(
            host = "bzsehfulsyzmf1e718hl-mysql.services.clever-cloud.com",
            user = "uhuqob7zeqs14vje",
            password = "jw9z8U4fYIvImMscqqbG",
            database = "bzsehfulsyzmf1e718hl",
            port = 3306
        )
        # return mysql.connector.connect(
        #     host = "localhost",
        #     user = "root",
        #     password = "Kh1ng*7490@1963",
        #     database = "attention_client",
        #     port = 3306
        # )
    except mysql.connector.errors as err:
        raise err