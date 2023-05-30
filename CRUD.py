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

def read_order(num_search, column, value):
    if num_search == 1 or num_search == 4:
        mycursor.execute(
            "select Id_ordering, Payment_method, Registration_date, Total_amount, customer.full_name as Full_name_customer, employee.full_name, concat(brand,' ', model) as Car, car.id_car from ordering "
            "join customer on customer.id_customer = ordering.id_customer "
            "join employee on employee.id_employee = ordering.id_employee "
            "join car on car.id_car = ordering.id_car where " + column + " = " + value)
        mytable = PrettyTable()
        mytable.field_names = ['Id_order', 'Payment_method', 'Registration_date', 'Total_amount', 'Full_name_customer', 'Full_name_employee', 'Car', 'Id_car']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)
    else:
        mycursor.execute(
            "select Id_ordering, Payment_method, Registration_date, Total_amount, customer.full_name as Full_name_customer, employee.full_name, concat(brand,' ', model) as Car, car.id_car from ordering "
            "join customer on customer.id_customer = ordering.id_customer "
            "join employee on employee.id_employee = ordering.id_employee "
            "join car on car.id_car = ordering.id_car where " + column + " = " + "'" + value + "'")
        mytable = PrettyTable()
        mytable.field_names = ['Id_order', 'Payment_method', 'Registration_date', 'Total_amount', 'Full_name_customer', 'Full_name_employee', 'Car', 'Id_car']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)