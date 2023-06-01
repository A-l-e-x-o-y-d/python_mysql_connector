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

def read_employee(num_search, column, value):
    if num_search == 1 or num_search == 7:
        mycursor.execute("select * from employee where " + column + " = " + value)
        mytable = PrettyTable()
        mytable.field_names = ['Id_customer', 'Full_name', 'Phone_number', 'Address', 'Date_of_birth', 'Email', 'Salary']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)
    else:
        mycursor.execute("select * from employee where " + column + " = " + "'" + value + "'")
        mytable = PrettyTable()
        mytable.field_names = ['Id_customer', 'Full_name', 'Phone_number', 'Address', 'Date_of_birth', 'Email', 'Salary']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)

def read_car(num_search, column, value):

    if num_search == 1 or num_search == 5:
        mycursor.execute(
            "select Id_car, concat(brand,' ',model), year_of_release, price, color, equipment.gearbox_type, equipment.car_interior, equipment.electrical_equipment, insurance.insurance_number from car "
            "join equipment on car.id_equipment = equipment.id_equipment "
            "join insurance on car.id_insurance = insurance.id_insurance "
            "where " + column + " = " + value)
        mytable = PrettyTable()
        mytable.field_names = ['Id_car', 'Car', 'Year_of_release', 'Price', 'Color', 'Gearbox_type', 'Car_interior',
                               'Electrical_equipment', 'Insurance_number']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)

    else:
        mycursor.execute(
            "select Id_car, concat(brand,' ',model), year_of_release, price, color, equipment.gearbox_type, equipment.car_interior, equipment.electrical_equipment, insurance.insurance_number from car "
            "join equipment on car.id_equipment = equipment.id_equipment "
            "join insurance on car.id_insurance = insurance.id_insurance "
            "where " + column + " = " + "'" + value + "'")
        mytable = PrettyTable()
        mytable.field_names = ['Id_car', 'Car', 'Year_of_release', 'Price', 'Color', 'Gearbox_type', 'Car_interior',
                               'Electrical_equipment', 'Insurance_number']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)

def delete_customer(num_delete, column, value):

    if num_delete == 1:
        mycursor.execute("delete from customer where " + column + " = " + value)

    else:
        mycursor.execute("select * from customer where " + column + " = " + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from customer where " + column + " = " + '"' + value + '"')
            mytable = PrettyTable()
            mytable.field_names = ['Id_customer', 'Full_name', 'Phone_number', 'Address', 'Date_of_birth', 'Email']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_customer = input('\nВведите Id клиента: ')
            mycursor.execute("delete from customer where id_customer = " + id_customer)
            print('\nЗапись клиента успешно удалена')

        elif count == 0:
            print('\nКлиента с такими данными отсутствует')

        else:
            mycursor.execute("delete from customer where " + column + " = " + '"' + value + '"')
            print('\nЗапись клиента успешно удалена')

def delete_order(num_delete, column, value):
    if num_delete == 4:
        mycursor.execute("select * from ordering where " + column + " = " + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from ordering where " + column + " = " + value)
            mytable = PrettyTable()
            mytable.field_names = ['Id order', 'Payment method', 'Registration date', 'Total amount',
                                   'Full name customer', 'Full name employee', 'Car', 'Id car']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_order = input('\nВведите Id заказа: ')
            mycursor.execute("delete from ordering where id_ordering = " + id_order)
            print('\nЗапись заказа успешно удалена')

        elif count == 0:
            print('\nЗаказ с такими данными отсутствует')

        else:
            mycursor.execute("delete from ordering where " + column + " = " + value)
            print('\nЗапись заказа успешно удалена')

    elif num_delete == 5 or num_delete == 6 or num_delete == 7:
        mycursor.execute('select * from ordering '
                         'join customer on ordering.id_customer = customer.id_customer '
                         'join employee on ordering.id_employee = employee.id_employee '
                         'join car on ordering.id_car = car.id_car '
                         'where ' + column + ' = ' + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute('select * from ordering '
                             'join customer on ordering.id_customer = customer.id_customer '
                             'join employee on ordering.id_employee = employee.id_employee '
                             'join car on ordering.id_car = car.id_car '
                             'where ' + column + ' = ' + '"' + value + '"')
            mytable = PrettyTable()
            mytable.field_names = ['Id order', 'Payment method', 'Registration date', 'Total amount',
                                   'Full name customer', 'Full name employee', 'Car', 'Id car']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_order = input('\nВведите Id заказа: ')
            mycursor.execute('delete ordering from ordering '
                             'join customer on ordering.id_customer = customer.id_customer '
                             'join employee on ordering.id_employee = employee.id_employee '
                             'join car on ordering.id_car = car.id_car '
                             'where ' + column + ' = ' + '"' + value + '"')
            print('\nЗапись заказа успешно удалена')

        if count == 0:
            print('\nЗаказа с таким клиентом нет')

        else:
            mycursor.execute('delete ordering from ordering '
                             'join customer on ordering.id_customer = customer.id_customer '
                             'join employee on ordering.id_employee = employee.id_employee '
                             'join car on ordering.id_car = car.id_car '
                             'where ' + column + ' = ' + '"' + value + '"')
            print('\nЗапись заказа успешно удалена')

    else:
        mycursor.execute("select * from ordering where " + column + " = " + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from ordering where " + column + " = " + '"' + value + '"')
            mytable = PrettyTable()
            mytable.field_names = ['Id order', 'Payment method', 'Registration date', 'Total amount',
                                   'Full name customer', 'Full name employee', 'Car', 'Id car']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_order = input('\nВведите Id заказа: ')
            mycursor.execute("delete from ordering where id_ordering = " + id_order)
            print('\nЗапись заказа успешно удалена')

        elif count == 0:
            print('\nСотрудника с таким ФИО нет')

        else:
            mycursor.execute("delete from ordering where " + column + " = " + "'" + value + "'")
            print('\nЗапись заказа успешно удалена')

def delete_employee(num_delete, column, value):
    if num_delete == 1:
        mycursor.execute("delete from employee where " + column + " = " + value)

    elif num_delete == 7:
        mycursor.execute("delete from employee where " + column + " = " + value)
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from employee where " + column + " = " + value)
            mytable = PrettyTable()
            mytable.field_names = ['Id_customer', 'Full_name', 'Phone_number', 'Address',
                                   'Date_of_birth', 'Email', 'Salary']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_employee = input('\nВведите Id сотрудника: ')
            mycursor.execute("delete from employee where id_employee = " + id_employee)
            print('\nЗапись сотрудника успешно удалена')

        elif count == 0:
            print('\nСотрудник с такими данными отсутствует')

        else:
            mycursor.execute("delete from employee where " + column + " = " + value)

    else:
        mycursor.execute("delete from employee where " + column + " = " + "'" + value + "'")
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from employee where " + column + " = " + "'" + value + "'")
            mytable = PrettyTable()
            mytable.field_names = ['Id_customer', 'Full_name', 'Phone_number', 'Address',
                                   'Date_of_birth', 'Email', 'Salary']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_employee = input('\nВведите Id сотрудника: ')
            mycursor.execute("delete from employee where id_employee = " + id_employee)
            print('\nЗапись сотрудника успешно удалена')

        elif count == 0:
            print('\nСотрудник с такими данными отсутствует')

        else:
            mycursor.execute("delete from employee where " + column + " = " + "'" + value + "'")
            print('\nЗапись сотрудника успешно удалена')

def delete_car(num_delete, column, value):
    if num_delete == 1:
        mycursor.execute("delete from сar where " + column + " = " + value)

    else:
        mycursor.execute("select * from сar where " + column + " = " + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from сar where " + column + " = " + '"' + value + '"')
            mytable = PrettyTable()
            mytable.field_names = ['Id_car', 'Car', 'Year_of_release', 'Price', 'Color', 'Gearbox_type', 'Car_interior',
                                   'Electrical_equipment', 'Insurance_number']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_car = input('\nВведите Id клиента: ')
            mycursor.execute("delete from сar where id_car = " + id_car)
            print('\nЗапись клиента успешно удалена')

        elif count == 0:
            print('\nАвтомобиль с такими данными отсутствует')

        else:
            mycursor.execute("delete from сar where " + column + " = " + '"' + value + '"')
            print('\nЗапись автомобиля успешно удалена')