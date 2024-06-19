import mysql.connector

def connection (user, password):
     
        conn = mysql.connector.connect(user=user, 
                                     password=password, 
                                     host= 'localhost', 
                                      database='hotel_mpc',
                                       port='3306')
        print(conn)
        return conn
     

     
 