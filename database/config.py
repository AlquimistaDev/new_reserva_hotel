import mysql.connector

def connection ():
     
        conn = mysql.connector.connect(user='root', 
                                     password='123456789', 
                                     host= 'localhost', 
                                      database='hotel_mpc',
                                       port='3306')
        print(conn)
        return conn
     

     
 