import pymysql

class connection:
    try:
        conn=pymysql.connect("127.0.0.1","root","Root@123","new_schema")
    except(pymysql.err.OperationalError) as error:
        print("Error Connecting to MYSQL server!!!")
        exit()