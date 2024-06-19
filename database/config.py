import mysql.connector
from mysql.connector import errors

def connection(user, password):
    try:
        conn = mysql.connector.connect(user=user, 
                                       password=password, 
                                       host='localhost', 
                                       database='hotel_mpc',
                                       port='3306')
        if conn.is_connected():
            return True
        else:
            return False
    except errors.ProgrammingError as e:
        print(f"Error: {e}")
        return False


        
     

     
 