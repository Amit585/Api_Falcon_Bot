from resources.mydb import *
import pymysql
from resources.queries import queries

class dboperations:

    def __init__(self):
        db=connection()
        print("select one of the option:")
        print("1.VIEW")
        print("2.INSERT")
        print("3.UPDATE")
        print("4.DELETE")
        print("5.EXIT")
        case=int(input("Enter your choice:"))
        cr=db.conn.cursor()

        def errorMessage(error):
            error = format(error)
            error_message = eval(error)[1]
            print(error_message)

        if case==1:
            try:
                query = queries.fetch_query('')
                cr.execute(query)
                result=cr.fetchall()
                print("ORDER ID: ORDER STATUS")
                for data in result:
                    print(str(data[0])+": "+data[1])
            except (pymysql.err.IntegrityError,pymysql.err.ProgrammingError) as error:
                errorMessage(error)

        elif case==2:
            try:
                order_id = int(input("Enter the order id:"))
                order_status = input("Enter the order status:")
                query = queries.insert_query('', order_id, order_status)
                cr.execute(query)
                db.conn.commit()
            except (pymysql.err.IntegrityError,pymysql.err.ProgrammingError) as error:
                errorMessage(error)

        elif case==3:
            try:
                old_order_id = int(input("Enter the order id to be updated:"))
                new_order_id = int(input("Enter the new order id:"))
                order_status = input("Enter the new order status:")
                query = queries.update_query('', old_order_id, new_order_id, order_status)
                cr.execute(query)
                db.conn.commit()
            except (pymysql.err.IntegrityError,pymysql.err.ProgrammingError) as error:
               errorMessage(error)

        elif case==4:
            try:
                order_id = int(input("Enter the order id to be deleted:"))
                query = queries.delete_query('', order_id)
                result=cr.execute(query)
                if result==0:
                    print("Order id not found.")
                elif result==1:
                    print("Order with id "+order_id+" deleted.")
                db.conn.commit()
            except (pymysql.err.IntegrityError,pymysql.err.ProgrammingError) as error:
                errorMessage(error)

        elif case==5:
            exit()

        else:
            cr.close()
            print("Invalid Choice")
        print()
        dboperations()
x=dboperations()



