from prettytable import PrettyTable
import mysql.connector
from config import host, user, password, database

dn_name = mysql.connector.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = database
    )
mycursor = dn_name.cursor()

def read_customer(num_search, column, value):
    if num_search == 1:
        mycursor.execute("select * from customer where " + column + " = " + value)
        mytable = PrettyTable()
        mytable.field_names = ['Id_customer', 'Full_name', 'Phone_number', 'Address', 'Date_of_birth', 'Email']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)
    else:
        mycursor.execute("select * from customer where " + column + " = " + "'" + value + "'")
        mytable = PrettyTable()
        mytable.field_names = ['Id_customer', 'Full_name', 'Phone_number', 'Address', 'Date_of_birth', 'Email']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)