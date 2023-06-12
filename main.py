from prettytable import PrettyTable
import mysql.connector
from config import host, user, password, database

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
            "select Id_ordering, Payment_method, Registration_date, Total_amount, customer.full_name as Full_name_customer, employee.full_name, concat(brand,' ', model) as car, car.id_car from ordering "
            "join customer on customer.id_customer = ordering.id_customer "
            "join employee on employee.id_employee = ordering.id_employee "
            "join car on car.id_car = ordering.id_car where " + column + " = " + value)
        mytable = PrettyTable()
        mytable.field_names = ['Id_order', 'Payment_method', 'Registration_date', 'Total_amount', 'Full_name_customer', 'Full_name_employee', 'Car', 'Id_car']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)
    else:
        mycursor.execute(
            "select Id_ordering, Payment_method, Registration_date, Total_amount, customer.full_name as Full_name_customer, employee.full_name, concat(brand,' ', model) as car, car.id_car from ordering "
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
        mytable.field_names = ['Id_car', 'car', 'Year_of_release', 'Price', 'Color', 'Gearbox_type', 'car_interior',
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
        mytable.field_names = ['Id_car', 'car', 'Year_of_release', 'Price', 'Color', 'Gearbox_type', 'Car_interior',
                               'Electrical_equipment', 'Insurance_number']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)

def read_insurance(column, value):
    mycursor.execute(
        'select * from insurance where ' + column + ' = ' + value)
    mytable = PrettyTable()
    mytable.field_names = ['Id_insurance', 'Insurance_number', 'Start_date', 'End_date']
    mytable.add_rows(mycursor.fetchall())
    print(mytable)

def read_supplier(num_search, column, value):

    if num_search == 1:
        mycursor.execute(
            'select * from supplier where ' + column + ' = ' + value)
        mytable = PrettyTable()
        mytable.field_names = ['Id supplier', 'Company name', 'Phone number', 'Address', 'Full name contact person']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)

    else:
        mycursor.execute(
            'select * from supplier where ' + column + ' = ' + '"' + value + '"')
        mytable = PrettyTable()
        mytable.field_names = ['Id supplier', 'Company name', 'Phone number', 'Address', 'Full name contact person']
        mytable.add_rows(mycursor.fetchall())
        print(mytable)

def read_supplier_to_delivery(column, value):
    mycursor.execute(
        'select id_supplier_to_delivery, supplier.company_name, supplier.phone_number, supplier.adress, supplier.full_name_contact_person, delivery.order_date, delivery.delivery_date '
        'from supplier_to_delivery '
        'join supplier on supplier_to_delivery.id_supplier = supplier.id_supplier '
        'join delivery on supplier_to_delivery.id_delivery = delivery.id_delivery '
        'where ' + column + ' = ' + value)
    mytable = PrettyTable()
    mytable.field_names = ['Id supplier to delivery', 'Id supplier', 'Id delivery']
    mytable.add_rows(mycursor.fetchall())
    print(mytable)

def read_delivery(column, value):
    mycursor.execute(
        'select * from delivery where ' + column + ' = ' + '"' + value + '"')
    mytable = PrettyTable()
    mytable.field_names = ['Id delivery', 'Order date', 'Delivery date', 'Delivery place']
    mytable.add_rows(mycursor.fetchall())
    print(mytable)

def delete_customer(num_delete, column, value):

    if num_delete == 1:
        mycursor.execute("delete from customer where id_customer = " + value)
        print('\nЗапись клиента успешно удалена')

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

    if num_delete == 1:
        mycursor.execute("delete from ordering where id_ordering = " + value)
        print('\nЗапись заказа успешно удалена')

    elif num_delete == 4:
        mycursor.execute('select * from ordering '
                         'join customer on ordering.id_customer = customer.id_customer '
                         'join employee on ordering.id_employee = employee.id_employee '
                         'join car on ordering.id_car = car.id_car where ' + column + ' = ' + value)
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute('select * from ordering '
                             'join customer on ordering.id_customer = customer.id_customer '
                             'join employee on ordering.id_employee = employee.id_employee '
                             'join car on ordering.id_car = car.id_car where ' + column + ' = ' + value)
            mytable = PrettyTable()
            mytable.field_names = ['Id order', 'Payment method', 'Registration date', 'Total amount',
                                   'Full name customer', 'Full name employee', 'C1ar', 'Id car']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_order = input('\nВведите Id заказа: ')
            mycursor.execute('delete from ordering where id_ordering = ' + id_order)
            print('\nЗапись заказа успешно удалена')

        elif count == 0:
            print('\nЗаказ с такими данными отсутствует')

        else:
            mycursor.execute('delete ordering from ordering '
                             'join customer on ordering.id_customer = customer.id_customer '
                             'join employee on ordering.id_employee = employee.id_employee '
                             'join car on ordering.id_car = car.id_car '
                             'where ' + column + ' = ' + value)
            print('\nЗапись заказа успешно удалена')

    else:
        mycursor.execute('select * from ordering '
                         'join customer on ordering.id_customer = customer.id_customer '
                         'join employee on ordering.id_employee = employee.id_employee '
                         'join car on ordering.id_car = car.id_car where ' + column + ' = ' + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute('select * from ordering '
                             'join customer on ordering.id_customer = customer.id_customer '
                             'join employee on ordering.id_employee = employee.id_employee '
                             'join car on ordering.id_car = car.id_car '
                             'where ' + column + ' = ' + "'" + value + "'")
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
            mycursor.execute('delete ordering from ordering '
                             'join customer on ordering.id_customer = customer.id_customer '
                             'join employee on ordering.id_employee = employee.id_employee '
                             'join car on ordering.id_car = car.id_car where ' + column + ' = ' + '"' + value + '"')
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
        mycursor.execute("delete from car where id_car = " + value)
        print('\nЗапись автомобиля успешно удалена')

    elif num_delete == 4:
        mycursor.execute("select * from car where " + column + " = " + value)
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from car where " + column + " = " + value)
            mytable = PrettyTable()
            mytable.field_names = ['Id_car', 'car', 'Year_of_release', 'Price', 'Color', 'Gearbox_type', 'car_interior',
                                   'Electrical_equipment', 'Insurance_number']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_car = input('\nВведите Id автомобиля: ')
            mycursor.execute("delete from car where id_car = " + id_car)
            print('\nЗапись автомобиля успешно удалена')

        elif count == 0:
            print('\nАвтомобиль с такими данными отсутствует')

        else:
            mycursor.execute("delete from car where " + column + " = " + value)

            print('\nЗапись автомобиля успешно удалена')

    else:
        mycursor.execute("select * from car where " + column + " = " + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from car where " + column + " = " + '"' + value + '"')
            mytable = PrettyTable()
            mytable.field_names = ['Id_car', 'car', 'Year_of_release', 'Price', 'Color', 'Gearbox_type', 'car_interior',
                                   'Electrical_equipment', 'Insurance_number']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_car = input('\nВведите Id клиента: ')
            mycursor.execute("delete from car where id_car = " + id_car)
            print('\nЗапись клиента успешно удалена')

        elif count == 0:
            print('\nАвтомобиль с такими данными отсутствует')

        else:
            mycursor.execute("delete from car where " + column + " = " + '"' + value + '"')
            print('\nЗапись автомобиля успешно удалена')

def delete_insurance(column, value):
    mycursor.execute('delete from insurance where ' + column + ' = ' + value)
    print('\nЗапись страховки успешно удалена')

def delete_supplier(num_delete, column, value):

    if num_delete == 1:
        mycursor.execute("delete from supplier where id_supplier = " + value)
        print('\nЗапись клиента успешно удалена')

    else:
        mycursor.execute("select * from supplier where " + column + " = " + '"' + value + '"')
        mycursor.fetchall()
        count = mycursor.rowcount

        if count > 1:
            mycursor.execute("select * from supplier where " + column + " = " + '"' + value + '"')
            mytable = PrettyTable()
            mytable.field_names = ['Id', 'Company name', 'Phone number', 'Address', 'Full name contact person']
            mytable.add_rows(mycursor.fetchall())
            print(mytable)
            id_supplier = input('\nВведите Id поставщика: ')
            mycursor.execute("delete from supplier where id_supplier = " + id_supplier)
            print('\nЗапись поставщика успешно удалена')

        elif count == 0:
            print('\nПоставщика с такими данными отсутствует')

        else:
            mycursor.execute("delete from supplier where " + column + " = " + '"' + value + '"')
            print('\nЗапись поставщика успешно удалена')


#--------------------------------------------------------------------------------------------------------------------

# Соединение с БД
try:
    action = True
    while action == True:

        db_name = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=database
        )
        print("\nSuccessfully connected...")

        print('\n1. Таблицы\n2. Аналитические запросы\n3. Закончить работу\n')
        num = int(input('\nВведите номер для продолжения: '))
        mycursor = db_name.cursor()  # Объявление курсора

        if num == 1:

            # Выбор таблицы для взаимодействия
            print('\nТаблицы:\n1. Customer\n2. Ordering\n3. Employee\n4. Car\n5. Equipment\n6. Insurance\n7. Supplier\n8. Supplier to Delivery\n9. Delivery\n')
            num_table = int(input('\nВведите номер таблицы для взаимодействия: '))

            # Клиент
            if num_table == 1:
                print('\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_customer = input('\nВведите Id клиента: ')
                    full_name = input('Введите ФИО клиента: ')
                    phone_number = input('Введите номер клиента: ')
                    address = input('Введите адрес клиента: ')
                    date_of_birth = input('Введите дату рождения клиента(ГГГГ-ММ-ДД): ')
                    email = input('Введите Email клиента: ')

                    mycursor.execute('insert into Customer(id_customer, full_name, phone_number, adress, date_of_birth, email) values (' + id_customer + ',"' + full_name + '","' + phone_number + '","' + address + '","' + date_of_birth + '","' + email + '")')

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись клиента успешно добавлена')

                # Читать запись
                elif num_act == 2:
                    print('\nКолонки:\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n')
                    num_search = int(input('\nВведите номер колонки, по которой будет производиться поиск клиента: '))

                    if num_search == 1:
                        id_customer = input('\nВведите Id клиента: ')
                        read_customer(num_search, 'id_customer', id_customer)

                    elif num_search == 2:
                        full_name = input('\nВведите ФИО клиента: ')
                        read_customer(num_search, 'full_name', full_name)

                    elif num_search == 3:
                        phone_number = input('\nВведите номер телефона клиента: ')
                        read_customer(num_search, 'phone_number', phone_number)

                    elif num_search == 4:
                        address = input('\nВведите адрес клиента: ')
                        read_customer(4, 'adress', address)

                    elif num_search == 5:
                        date_of_birth = input('\nВведите дату рождения клиента(ГГГГ-ММ-ДД): ')
                        read_customer(5, 'date_of_birth', date_of_birth)

                    elif num_search == 6:
                        email = input('\nВведите Email клиента: ')
                        read_customer(6, 'email', email)

                # Редактировать запись
                elif num_act == 3:
                    id_customer = input('\nВведите Id клиента: ')
                    print('\nКолонки:\n1. Id customer\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n')
                    num_update = int(input('\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_customer = input('\nВведите новое Id клиента: ')
                        mycursor.execute("update customer set id_customer = " + new_id_customer + " where id_customer = " + id_customer)

                    elif num_update == 2:
                        new_full_name = input('\nВведите новое ФИО клиента: ')
                        mycursor.execute("update customer set full_name = " + "'" + new_full_name + "'" + " where id_customer = " + id_customer)

                    elif num_update == 3:
                        new_phone_number = input('\nВведите новый телефон клиента: ')
                        mycursor.execute("update customer set phone_number = " + "'" + new_phone_number + "'" + " where id_customer = " + id_customer)

                    elif num_update == 4:
                        new_address = input('\nВведите новый адрес клиента: ')
                        mycursor.execute("update customer set adress = " + "'" + new_address + "'" + " where id_customer = " + id_customer)

                    elif num_update == 5:
                        new_date_of_birth = input('\nВведите новую дату рождения клиента(ГГГГ-ММ-ДД): ')
                        mycursor.execute("update customer set date_of_birth = " + "'" + new_date_of_birth + "'" + " where id_customer = " + id_customer)

                    elif num_update == 6:
                        new_email = input('\nВведите новый Email клиента: ')
                        mycursor.execute("update customer set email = " + "'" + new_email + "'" + " where id_customer = " + id_customer)

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись клиента успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\nКолонки:\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n')
                    num_delete = int(input('\nВведите номер колонки, по которой будет производиться удаление клиента: '))

                    if num_delete == 1:
                        id_customer = input('\nВведите Id клиента: ')
                        delete_customer(1, 'id_customer', id_customer)
                        # mycursor.execute('delete from customer where id_customer = ' + id_customer)

                    elif num_delete == 2:
                        full_name = input('\nВведите ФИО клиента: ')
                        delete_customer(2, 'full_name', full_name)

                    elif num_delete == 3:
                        phone_number = input('\nВведите номер телефона клиента: ')
                        delete_customer(3, 'phone_number', phone_number)

                    elif num_delete == 4:
                        address = input('\nВведите адрес клиента: ')
                        delete_customer(3, 'adress', address)

                    elif num_delete == 5:
                        date_of_birth = input('\nВведите дату рождения клиента(ГГГГ-ММ-ДД): ')
                        delete_customer(4, 'date_of_birth', date_of_birth)

                    elif num_delete == 6:
                        email = input('\nВведите Email клиента: ')
                        delete_customer(5, 'email', email)

                    else:
                        print('\nНомера выбранной колонки не существует')

                    # Принять изменения
                    db_name.commit()

                else:
                    print('\nНомер выбранного действия не существует!')

            # Заказ
            elif num_table == 2:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_order = input('\nВведите Id заказа: ')
                    payment_method = input('Введите метод оплаты заказа(Б/Н): ')
                    registration_date = input('Введите дату регистрации заказа(ГГГГ-ММ-ДД): ')
                    total_amount = input('Введите итоговую цену заказа: ')
                    id_customer = input('Введите Id клиента: ')
                    id_employee = input('Введите Id сотрудника: ')
                    id_car = input('Введите Id автомобиля: ')

                    mycursor.execute(
                        'insert into Ordering(id_ordering, payment_method, registration_date, total_amount, id_customer, id_car, id_employee) values (' + id_order + ',"' + payment_method + '","' + registration_date + '","' + total_amount + '",' + id_customer + ',' + id_car + ',' + id_employee + ')')

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись заказа успешно добавлена')

                # Читать запись
                elif num_act == 2:

                    print('\nКолонки:\n1. Id\n2. Payment method\n3. Registration date\n4. Total amount\n5. Full name customer\n6. Full name employee\n7. car brand\n')
                    num_search = int(input('\nВведите номер колонки, по которой будет производиться поиск заказа: '))

                    if num_search == 1:
                        id_order = input('\nВведите Id заказа: ')
                        read_order(1, 'Id_ordering', id_order)

                    if num_search == 2:
                        payment_method = input('\nВведите способ оплаты заказа(Б/Н): ')
                        read_order(2, 'payment_method', payment_method)

                    if num_search == 3:
                        registration_date = input('\nВведите дату регистрации заказа(ГГГГ-ММ-ДД): ')
                        read_order(3, 'registration_date', registration_date)

                    if num_search == 4:
                        total_amount = input('\nВведите итоговую цену заказа: ')
                        read_order(3, 'total_amount', total_amount)

                    if num_search == 5:
                        full_name_customer = input('\nВведите ФИО клиента: ')
                        read_order(3, 'customer.full_name', full_name_customer)

                    if num_search == 6:
                        full_name_employee = input('\nВведите ФИО сотруника: ')
                        read_order(3, 'employee.full_name', full_name_employee)

                    if num_search == 7:
                        brand = input('\nВведите марку автомобиля: ')
                        read_order(3, 'car.brand', brand)

                # Редактировать запись
                elif num_act == 3:
                    id_order = input('\nВведите Id заказа: ')
                    print('\nКолонки:\n1. Id order\n2. Payment method\n3. Registration date\n4. Total amount\n5. Id customer\n6. Id employee\n7. Id car\n')
                    num_update = int(input('\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_order = input('\nВведите новое Id заказа: ')
                        mycursor.execute(
                            "update ordering set id_ordering = " + new_id_order + " where id_ordering = " + id_order)

                    if num_update == 2:
                        new_payment_method = input('\nВведите новый метод оплаты заказа(Б/Н): ')
                        mycursor.execute(
                            "update ordering set payment_method = " + "'" + new_payment_method + "'" + " where id_ordering = " + id_order)

                    if num_update == 3:
                        new_registration_date = input('\nВведите новую дату регистрации заказа(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update ordering set registration_date = " + "'" + new_registration_date + "'" + " where id_ordering = " + id_order)

                    if num_update == 4:
                        new_total_amount = input('\nВведите новую итоговую цену заказа: ')
                        mycursor.execute(
                            "update ordering set total_amount = " + "'" + new_total_amount + "'" + " where id_ordering = " + id_order)

                    if num_update == 5:
                        new_id_customer = input('\nВведите новое Id клиента: ')
                        mycursor.execute(
                            "update ordering set id_customer = " + "'" + new_id_customer + "'" + " where id_ordering = " + id_order)

                    if num_update == 6:
                        new_id_employee = input('\nВведите новое Id сотрудника: ')
                        mycursor.execute(
                            "update ordering set id_employee = " + "'" + new_id_employee + "'" + " where id_ordering = " + id_order)

                    if num_update == 7:
                        new_id_car = input('\nВведите новое Id автомобиля: ')
                        mycursor.execute(
                            "update ordering set id_car = " + "'" + new_id_car + "'" + " where id_ordering = " + id_order)

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись заказа успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\nКолонки:\n1. Id order\n2. Payment method\n3. Registartion date\n4. Total amount\n5. Full name customer\n6. Brand and model\n7. Full name employee\n')

                    num_delete = int(
                        input('\nВведите номер колонки, по которой будет производиться удаление заказа: '))

                    if num_delete == 1:
                        id_order = input('\nВведите Id заказа: ')
                        delete_order(1, 'id_ordering', id_order)

                    elif num_delete == 2:
                        payment_method = input('\nВведите способ оплаты заказа(Б/Н): ')
                        delete_order(2, 'payment_method', payment_method)

                    elif num_delete == 3:
                        registration_date = input('\nВведите дату регистрации заказа(ГГГГ-ММ-ДД): ')
                        delete_order(3, 'registration_date', registration_date)

                    elif num_delete == 4:
                        total_amount = input('\nВведите итоговую цену заказа: ')
                        delete_order(4, 'total_amount', total_amount)

                    elif num_delete == 5:
                        full_name_customer = input('\nВведите ФИО клиента: ')
                        delete_order(5, 'customer.full_name', full_name_customer)

                    elif num_delete == 6:
                        brand_and_model = input('\nВведите марку и модель автомобиля: ')
                        delete_order(6, 'concat(car.brand, " ", car.model)', brand_and_model)

                    elif num_delete == 7:
                        full_name_employee = input('\nВведите ФИО сотрудника: ')
                        delete_order(7, 'employee.Full_name', full_name_employee)

                    else:
                        print('\nНомера выбранной колонки не существует')

                    # Принять изменения
                    db_name.commit()

                else:
                    print('\nНомер выбранного действия не существует!')

            # Сотрудник
            elif num_table == 3:
                print('\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_employee = input('\nВведите Id сотрудника: ')
                    full_name = input('Введите ФИО сотрудника: ')
                    phone_number = input('Введите номер сотрудника: ')
                    address = input('Введите адрес сотрудника: ')
                    date_of_birth = input('Введите дату рождения сотрудника(ГГГГ-ММ-ДД): ')
                    email = input('Введите Email сотрудника: ')
                    salary = input('Введите заработную плату сотрудника: ')

                    mycursor.execute('insert into Employee(id_employee, full_name, phone_number, adress, date_of_birth, email, salary) values (' + id_employee + ',"' + full_name + '","' + phone_number + '","' + address + '","' + date_of_birth + '","' + email + '",' + salary + ')')

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись сотрудника успешно добавлена')

                # Читать запись
                elif num_act == 2:

                    print('\nКолонки:\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n7. Salary\n')
                    num_search = int(input('\nВведите номер колонки, по которой будет производиться поиск сотрудника: '))

                    if num_search == 1:
                        id_employee = input('\nВведите Id сотрудника: ')
                        read_employee(1, 'id_employee', id_employee)

                    elif num_search == 2:
                        full_name = input('\nВведите ФИО сотрудника: ')
                        read_employee(2, 'full_name', full_name)

                    elif num_search == 3:
                        phone_number = input('\nВведите номер телефона сотрудника: ')
                        read_employee(3, 'phone_number', phone_number)

                    elif num_search == 4:
                        address = input('\nВведите адрес сотрудника: ')
                        read_employee(4, 'adress', address)

                    elif num_search == 5:
                        date_of_birth = input('\nВведите дату рождения сотрудника(ГГГГ-ММ-ДД): ')
                        read_employee(5, 'date_of_birth', date_of_birth)

                    elif num_search == 6:
                        email = input('\nВведите Email сотрудника: ')
                        read_employee(6, 'email', email)

                    elif num_search == 7:
                        salary = input('\nВведите заработную плату сотрудника: ')
                        read_employee(7, 'salary', salary)

                # Редактировать запись
                elif num_act == 3:
                    id_employee = input('\nВведите Id сотрудника: ')
                    print('\nКолонки:\n1. Id_employee\n2. Full_name\n3. Phone_number\n4. Address\n5. Date_of_birth\n6. Email\n7. Salary\n')
                    num_update = int(input('\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_employee = input('\nВведите новое Id сотрудника: ')
                        mycursor.execute(
                            "update employee set id_employee = " + new_id_employee + " where id_employee = " + id_employee)

                    elif num_update == 2:
                        new_full_name = input('\nВведите новое ФИО сотрудника: ')
                        mycursor.execute(
                            "update employee set full_name = " + "'" + new_full_name + "'" + " where id_employee = " + id_employee)

                    elif num_update == 3:
                        new_phone_number = input('\nВведите новый телефон сотрудника: ')
                        mycursor.execute(
                            "update employee set phone_number = " + "'" + new_phone_number + "'" + " where id_employee = " + id_employee)

                    elif num_update == 4:
                        new_address = input('\nВведите новый адрес сотрудника: ')
                        mycursor.execute(
                            "update employee set adress = " + "'" + new_address + "'" + " where id_employee = " + id_employee)

                    elif num_update == 5:
                        new_date_of_birth = input('\nВведите новую дату рождения сотрудника(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update employee set date_of_birth = " + "'" + new_date_of_birth + "'" + " where id_employee = " + id_employee)

                    elif num_update == 6:
                        new_email = input('\nВведите новый Email сотрудника: ')
                        mycursor.execute(
                            "update employee set email = " + "'" + new_email + "'" + " where id_employee = " + id_employee)

                    elif num_update == 7:
                        new_email = input('\nВведите новую заработную плату сотрудника: ')
                        mycursor.execute(
                            "update employee set email = " + "'" + new_email + "'" + " where id_employee = " + id_employee)

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись сотрудника успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\nКолонки:\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n7. Salary\n')
                    num_delete = int(
                        input('\nВведите номер колонки, по которой будет производиться удаление сотрудника: '))

                    if num_delete == 1:
                        id_employee = input('\nВведите Id сотрудника: ')
                        delete_employee(1, 'id_employee', id_employee)

                    elif num_delete == 2:
                        full_name = input('\nВведите ФИО сотрудника: ')
                        delete_employee(2, 'full_name', full_name)

                    elif num_delete == 3:
                        phone_number = input('Введите номер телефона сотрудника: ')
                        delete_employee(3, 'phone_number', phone_number)

                    elif num_delete == 4:
                        address = input('\nВведите адрес сотрудника: ')
                        delete_employee(4, 'adress', address)

                    elif num_delete == 5:
                        date_of_birth = input('\nВведите дату рождения сотрудника(ГГГГ-ММ-ДД): ')
                        delete_employee(5, 'date_of_birth', date_of_birth)

                    elif num_delete == 6:
                        email = input('\nВведите Email сотрудника: ')
                        delete_employee(6, 'email', email)

                    elif num_delete == 7:
                        salary = input('\nВведите заработную плату сотрудника: ')
                        delete_employee(7, 'salary', salary)

                    else:
                        print('\nНомера выбранной колонки не существует')

                    # Принять изменения
                    db_name.commit()

                else:
                    print('\nНомер выбранного действия не существует!')

            # Автомобиль
            elif num_table == 4:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('Введите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_car = input('\nВведите Id автомобиля: ')
                    brand = input('Введите марку автомобиля: ')
                    model = input('Введите модель автомобиля: ')
                    year_of_release = input('Введите год выпуска автомобиля(ГГГГ): ')
                    price = input('Введите цену автомобиля: ')
                    color = input('Введите цвет автомобиля: ')
                    id_equipment = input('Введите Id комплектации автомобиля: ')
                    id_insurance = input('Введите Id страховки автомобиля: ')

                    mycursor.execute(
                        'insert into car(id_car, brand, model, year_of_release, price, color, id_equipment, id_insurance) values (' + id_car + ',"' + brand + '","' + model + '","' + year_of_release + '",' + price + ',"' + color + '",' + id_equipment + ',' + id_insurance + ')')

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись автомобиля успешно добавлена')

                # Читать запись
                elif num_act == 2:

                    print('\nКолонки:\n1. Id\n2. Brand\n3. Brand and model\n4. Year of release\n5. Price\n6. Color\n')
                    num_search = int(input('\nВведите номер колонки, по которой будет производиться поиск автомобиля: '))

                    if num_search == 1:
                        id_car = input('\nВведите Id автомобиля: ')
                        read_car(1, 'id_car', id_car)

                    elif num_search == 2:
                        brand = input('\nВведите марку автомобиля: ')
                        read_car(2, 'brand', brand)

                    elif num_search == 3:
                        brand_and_model = input('\nВведите марку и модель автомобиля: ')
                        read_car(3, 'concat(brand, " ", model)', brand_and_model)

                    elif num_search == 4:
                        year_of_release = input('\nВведите год выпуска автомобиля(ГГГГ): ')
                        read_car(4, 'year_of_release', year_of_release)

                    elif num_search == 5:
                        price = input('\nВведите цену автомобиля: ')
                        read_car(5, 'price', price)

                    elif num_search == 6:
                        color = input('\nВведите цвет автомобиля: ')
                        read_car(6, 'color', color)

                # Редактировать запись
                elif num_act == 3:
                    id_car = input('\nВведите Id автомобиля: ')
                    print('\nКолонки:\n1. Id_car\n2. Brand and model\n3. Model\n4. Year of release\n5. Price\n6. Color\n7. Id equipment\n8. Id insurance\n')
                    num_update = int(input('\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_car = input('\nВведите новое Id автомобиля: ')
                        mycursor.execute(
                            "update car set id_car = " + new_id_car + " where id_car = " + id_car)

                    elif num_update == 2:
                        new_brand_and_model = input('\nВведите новую марку и модель автомобиля: ')
                        new_brand_and_model = new_brand_and_model.split()
                        new_brand = new_brand_and_model[0]
                        new_model = new_brand_and_model[1]
                        for value in new_brand_and_model[2:len(new_brand_and_model)]:
                            new_model = new_model + ' ' + value
                        mycursor.execute(
                            "update car set brand = " + "'" + new_brand + "'" + " where id_car = " + id_car)
                        mycursor.execute(
                            "update car set model = " + "'" + new_model + "'" + " where id_car = " + id_car)

                    elif num_update == 3:
                        new_model = input('\nВведите новую модель автомобиля: ')
                        mycursor.execute(
                            "update car set model = " + "'" + new_model + "'" + " where id_car = " + id_car)

                    elif num_update == 4:
                        new_year_of_release = input('\nВведите новый год выпуска автомобиля(ГГГГ): ')
                        mycursor.execute(
                            "update car set year_of_release = " + "'" + new_year_of_release + "'" + " where id_car = " + id_car)

                    elif num_update == 5:
                        new_price = input('\nВведите новую цену автомобиля: ')
                        mycursor.execute(
                            "update car set price = " + "'" + new_price + "'" + " where id_car = " + id_car)

                    elif num_update == 6:
                        new_color = input('\nВведите новый цвет автомобиля: ')
                        mycursor.execute(
                            "update car set color = " + "'" + new_color + "'" + " where id_car = " + id_car)

                    elif num_update == 7:
                        new_id_equipment = input('\nВведите новое Id комплектации: ')
                        mycursor.execute(
                            "update car set id_equipment = " + "'" + new_id_equipment + "'" + " where id_car = " + id_car)

                    elif num_update == 8:
                        new_id_insurance = input('\nВведите новое Id страховки: ')
                        mycursor.execute(
                            "update car set id_insurance = " + "'" + new_id_insurance + "'" + " where id_car = " + id_car)

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись автомобиля успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\nКолонки:\n1. Id\n2. Brand and model\n3. Year of release\n4. Price\n5. Color\n')
                    num_delete = int(input('\nВведите номер колонки, по которой будет производиться удаление автомобиля: '))

                    if num_delete == 1:
                        id_car = input('\nВведите Id автомобиля: ')
                        delete_car(1, 'id_car', id_car)

                    elif num_delete == 2:
                        brand_and_model = input('\nВведите марку и модель автомобиля: ')
                        delete_car(2, 'concat(brand, " ", model)', brand_and_model)

                    elif num_delete == 3:
                        year_of_release = input('\nВведите год релиза автомобиля(ГГГГ): ')
                        delete_car(3, 'year_of_release', year_of_release)

                    elif num_delete == 4:
                        price = input('\nВведите цену автомобиля: ')
                        delete_car(4, 'price', price)

                    elif num_delete == 5:
                        color = input('\nВведите цвет автомобиля: ')
                        delete_car(5, 'color', color)

                    else:
                        print('\nНомера выбранной колонки не существует')

                    # Принять изменения
                    db_name.commit()

                else:
                    print('\nНомер выбранного действия не существует!')

            # Комплектация автомобиля
            elif num_table == 5:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_equipment = input('\nВведите Id комплектации: ')
                    gearbox_type = input('Введите тип КПП комплектации: ')
                    car_interior = input('Введите отделку интерьера комплектации: ')
                    electrical_equipment = input('Введите электрооборудование комплектации: ')

                    mycursor.execute(
                        'insert into equipment(id_equipment, gearbox_type, car_interior, electrical_equipment) values (' + id_equipment + ',"' + gearbox_type + '","' + car_interior + '","' + electrical_equipment + '")')

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись комлектации успешно добавлена')

                # Читать запись
                elif num_act == 2:
                    id_equipment = input('\nВведите Id комплектации: ')
                    mycursor.execute(
                        "select * from equipment where id_equipment = " + id_equipment)
                    mytable = PrettyTable()
                    mytable.field_names = ['Id_equipment', 'Gearbox_type', 'Car_interior', 'Electrical_equipment']
                    mytable.add_rows(mycursor.fetchall())
                    print(mytable)

                # Редактировать запись
                elif num_act == 3:
                    id_equipment = input('\nВведите Id комплектации: ')
                    print('\nКолонки:\n1. Id_equipment\n2. Gearbox_type\n3. car_interior\n4. Electrical_equipment\n')
                    num_update = int(input('\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_equipment = input('\nВведите новое Id комлектации: ')
                        mycursor.execute(
                            "update equipment set id_equipment = " + new_id_equipment + " where id_equipment = " + id_equipment)

                    elif num_update == 2:
                        new_gearbox_type = input('\nВведите новый тип КПП комлектации: ')
                        mycursor.execute(
                            "update equipment set gearbox_type = " + "'" + new_gearbox_type + "'" + " where id_equipment = " + id_equipment)

                    elif num_update == 3:
                        new_car_interior = input('\nВведите новую отделку интерьера комлектации: ')
                        mycursor.execute(
                            "update equipment set car_interior = " + "'" + new_car_interior + "'" + " where id_equipment = " + id_equipment)

                    elif num_update == 4:
                        new_electrical_equipment = input('\nВведите новое электрооборудование комплектации: ')
                        mycursor.execute(
                            "update equipment set electrical_equipment = " + "'" + new_electrical_equipment + "'" + " where id_equipment = " + id_equipment)

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись комплектации успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    id_equipment = input('\nВведите Id комлектации: ')
                    mycursor.execute("delete from equipment where id_equipment = " + id_equipment)
                    print('\nЗапись комлектации успешно удалена')

                else:
                    print('\nНомер выбранного действия не существует!')

                # Принять изменения
                db_name.commit()

            # Страховка автомобиля
            elif num_table == 6:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_insurance = input('\nВведите Id страховки: ')
                    insurance_number = input('Введите номер страховки(16 цифр): ')
                    start_date = input('Введите дату начала действия страховки(ГГГГ-ММ-ДД): ')
                    end_date = input('Введите дату окончания действия страховки(ГГГГ-ММ-ДД): ')

                    mycursor.execute(
                        'insert into insurance(id_insurance, insurance_number, start_date, end_date) values (' + id_insurance + ',' + insurance_number + ',"' + start_date + '","' + end_date + '")')

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись страховки успешно добавлена')

                # Читать запись
                elif num_act == 2:
                    print('\nКолонки:\n1. Id\n2. Insurance number\n')
                    num_search = int(input('\nВведите номер колонки, по которой будет производиться поиск страховки: '))

                    if num_search == 1:
                        id_insurance = input('\nВведите Id страховки: ')
                        read_insurance('id_insurance', id_insurance)

                    elif num_search == 2:
                        insurance_number = input('\nВведите номер страховки(16 цифр): ')
                        read_insurance('insurance_number', insurance_number)

                # Редактировать запись
                elif num_act == 3:
                    id_insurance = input('\nВведите Id страховки: ')
                    print('\nКолонки:\n1. Id_insurance\n2. Insurance_number\n3. Start_date\n4. End_date\n')
                    num_update = int(input('\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_insurance = input('\nВведите новое Id страховки: ')
                        mycursor.execute(
                            "update insurance set id_insurance = " + new_id_insurance + " where id_insurance = " + id_insurance)

                    elif num_update == 2:
                        new_insurance_number = input('\nВведите новый номер страховки(16 цифр): ')
                        mycursor.execute(
                            "update insurance set insurance_number = " + "'" + new_insurance_number + "'" + " where id_insurance = " + id_insurance)

                    elif num_update == 3:
                        new_start_date = input('\nВведите новую дату начала действия страховки(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update insurance set start_date = " + "'" + new_start_date + "'" + " where id_insurance = " + id_insurance)

                    elif num_update == 4:
                        new_end_date = input('\nВведите новую дату окончания действия страховки(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update insurance set end_date = " + "'" + new_end_date + "'" + " where id_insurance = " + id_insurance)

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись страховки успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\nКолонки:\n1. Id\n2. Insurance number\n')
                    num_delete = int(input('\nВведите номер колонки, по которой будет производиться удаление страховки: '))

                    if num_delete == 1:
                        id_insurance = input('\nВведите Id страховки: ')
                        delete_insurance('id_insurance', id_insurance)

                    elif num_delete == 2:
                        insurance_number = input('\nВведите номер страховки(16 цифр): ')
                        delete_insurance('insurance_number', insurance_number)

                    else:
                        print('\nНомера выбранной колонки не существует')

                    # Принять изменения
                    db_name.commit()

                else:
                    print('\nНомер выбранного действия не существует!')

            # Поставщик
            elif num_table == 7:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_supplier = input('\nВведите Id поставщика: ')
                    company_name = input('Введите название компании: ')
                    phone_number = input('Введите номер поставщика: ')
                    address = input('Введите адрес поставщика: ')
                    full_name_contact_person = input('Введите ФИО контактного лица: ')

                    mycursor.execute(
                        'insert into supplier(id_supplier, company_name, phone_number, adress, full_name_contact_person) values (' + id_supplier + ',"' + company_name + '","' + phone_number + '","' + address + '","' + full_name_contact_person + '")')

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись поставщика успешно добавлена')

                # Читать запись
                elif num_act == 2:
                    print(
                        '\nКолонки:\n1. Id\n2. Company name\n3. Phone number\n4. Address\n5. Full name contact person\n')
                    num_search = int(
                        input('\nВведите номер колонки, по которой будет производиться поиск поставщика: '))

                    if num_search == 1:
                        id_supplier = input('\nВведите Id поставщика: ')
                        read_supplier(1, 'id_supplier', id_supplier)

                    elif num_search == 2:
                        company_name = input('\nВведите название компании: ')
                        read_supplier(2, 'company_name', company_name)

                    elif num_search == 3:
                        phone_number = input('\nВведите номер поставщика: ')
                        read_supplier(3, 'phone_number', phone_number)

                    elif num_search == 4:
                        address = input('\nВведите адрес поставщика: ')
                        read_supplier(4, 'adress', address)

                    elif num_search == 5:
                        full_name_contact_person = input('\nВведите ФИО контактного лица: ')
                        read_supplier(5, 'full_name_contact_person', full_name_contact_person)

                # Редактировать запись
                elif num_act == 3:
                    id_supplier = input('Введите Id поставщика: ')
                    print(
                        '\nКолонки:\n1. Id\n2. Company name\n3. Phone number\n4. Address\n5. Full name contact person\n')
                    num_update = int(input('\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_supplier = input('\nВведите новое Id поставщика: ')
                        mycursor.execute(
                            "update supplier set id_supplier = " + new_id_supplier + " where id_supplier = " + id_supplier)

                    elif num_update == 2:
                        new_company_name = input('\nВведите новое название компании: ')
                        mycursor.execute(
                            "update supplier set company_name = " + new_company_name + " where id_supplier = " + id_supplier)

                    elif num_update == 3:
                        new_phone_number = input('\nВведите новый номер поставщика: ')
                        mycursor.execute(
                            "update supplier set phone_number = " + new_phone_number + " where id_supplier = " + id_supplier)

                    elif num_update == 4:
                        new_address = input('\nВведите новый адрес поставщика: ')
                        mycursor.execute(
                            "update supplier set adress = " + new_address + " where id_supplier = " + id_supplier)

                    elif num_update == 5:
                        new_full_name_contact_person = input('\nВведите новое ФИО поставщика: ')
                        mycursor.execute(
                            "update supplier set full_name_contact_person = " + new_full_name_contact_person + " where id_supplier = " + id_supplier)

                    # Принять изменения
                    db_name.commit()
                    print('\nЗапись поставщика успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print(
                        '\nКолонки:\n1. Id\n2. Company name\n3. Phone number\n4. Address\n5. Full name contact person\n')
                    num_delete = int(
                        input('\nВведите номер колонки, по которой будет производиться удаление поставщика: '))

                    if num_delete == 1:
                        id_supplier = input('Введите Id поставщика: ')
                        delete_supplier(1, 'id_supplier', id_supplier)

                    elif num_delete == 2:
                        company_name = input('Введите название компании: ')
                        delete_supplier(2, 'company_name', company_name)

                    elif num_delete == 3:
                        phone_number = input('Введите номер поставщика: ')
                        delete_supplier(3, 'phone_number', phone_number)

                    elif num_delete == 4:
                        address = input('Введите адрес поставщика: ')
                        delete_supplier(4, 'adress', address)

                    elif num_delete == 5:
                        full_name_contact_person = input('Введите ФИО контактного лица: ')
                        delete_supplier(5, 'full_name_contact_person', full_name_contact_person)

                else:
                    print('\nНомер выбранного действия не существует!')

            # Поставщик_и_Доставка
            elif num_table == 8:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_supplier_to_delivery = input('\nВведите Id Поставщик-Доставка: ')
                    id_supplier = input('Введите Id поставщика: ')
                    id_delivery = input('Введите Id доставки: ')

                    mycursor.execute(
                        'insert into supplier_to_delivery(id_supplier_to_delivery, id_supplier, id_delivery) values (' + id_supplier_to_delivery + ',' + id_supplier + ',' + id_delivery + ')')

                    db_name.commit()
                    print('\nЗапись поставщик-доставка успешно добавлена')

                # Читать запись
                if num_act == 2:
                    print('\nКолонки:\n1. Id supplier to delivery\n2. Id supplier\n3. Id delivery\n')
                    num_search = int(input('\nВведите номер колонки, по которой будет производиться поиск записи: '))

                    if num_search == 1:
                        id_supplier_to_delivery = input('\nВведите Id Поставщик-Доставка: ')
                        read_supplier_to_delivery('id_supplier_to_delivery', id_supplier_to_delivery)

                    elif num_search == 2:
                        id_supplier = input('\nВведите Id поставщика: ')
                        read_supplier_to_delivery('id_supplier', id_supplier)

                    elif num_search == 3:
                        id_delivery = input('\nВведите Id доставки: ')
                        read_supplier_to_delivery('id_delivery', id_delivery)

                # Редактировать запись
                if num_act == 3:
                    id_supplier_to_delivery = input('\nВведите Id Поставщик-Доставка: ')
                    print('\nКолонки:\n1. id supplier to delivery\n2. Id supplier\n3. Id delivery\n')
                    num_update = int(input('\n\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_supplier_to_delivery = input('\nВведите новое Id Поставщик-Доставка: ')
                        mycursor.execute(
                            "update delivery set id_delivery = " + new_id_supplier_to_delivery + " where id_supplier_to_delivery = " + id_supplier_to_delivery)

                    elif num_update == 2:
                        new_id_supplier = input('\nВведите новое Id поставщика: ')
                        mycursor.execute(
                            "update delivery set id_supplier = " + new_id_supplier + " where id_supplier_to_delivery = " + id_supplier_to_delivery)

                    elif num_update == 3:
                        new_id_delivery = input('\nВведите новое Id доставки: ')
                        mycursor.execute(
                            "update delivery set id_delivery = " + new_id_delivery + " where id_supplier_to_delivery = " + id_supplier_to_delivery)

                    db_name.commit()
                    print('\nЗапись Поставщик-Доставка успешно изменена')

                # Удаление записи
                if num_act == 4:
                    id_supplier_to_delivery = input('\nВведите Id Поставщик-Доставка: ')
                    mycursor.execute("delete from supplier_to_delivery where id_supplier_to_delivery = " + id_supplier_to_delivery)

                    # Принять изменения
                    db_name.commit()
                    print('Запись Поставщик-Доставка успешно удалена')

            # Доставка
            elif num_table == 9:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('\nВведите номер действия: '))

                # Создать запись
                if num_act == 1:

                    id_delivery = input('\nВведите Id доставки: ')
                    order_date = input('Введите дату заказа(ГГГГ-ММ-ДД): ')
                    delivery_date = input('Введите дату доставки(ГГГГ-ММ-ДД): ')
                    delivery_place = 'ExpoCar'

                    mycursor.execute('insert into delivery(id_delivery, order_date, delivery_date, delivery_place) values (' + id_delivery + ',"' + order_date + '","' + delivery_date + '","' + delivery_place + '")')

                    db_name.commit()
                    print('\nЗапись доставки успешно добавлена')

                # Читать запись
                if num_act == 2:
                    print('\nКолонки:\n1. Id\n2. Order date\n3. Delivery date\n')
                    num_search = int(input('\nВведите номер колонки, по которой будет производиться поиск доставки: '))

                    if num_search == 1:
                        id_delivery = input('\nВведите Id доставки: ')
                        read_delivery('id_delivery', id_delivery)

                    elif num_search == 2:
                        order_date = input('\nВведите дату заказа(ГГГГ-ММ-ДД): ')
                        read_delivery('order_date', order_date)

                    elif num_search == 3:
                        delivery_date = input('\nВведите дату доставки(ГГГГ-ММ-ДД): ')
                        read_delivery('delivery_date', delivery_date)

                # Редактировать запись
                if num_act == 3:
                    id_delivery = input('\nВведите Id доставки: ')
                    print('\nКолонки:\n1. Id\n2. Order date\n3. Delivery date\n')
                    num_update = int(input('\n\nВведите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_delivery = input('Введите новое Id доставки: ')
                        mycursor.execute(
                            "update delivery set id_delivery = " + new_id_delivery + " where id_delivery = " + id_delivery)

                    elif num_update == 2:
                        new_order_date = input('\nВведите новую дату заказа: ')
                        mycursor.execute(
                            "update delivery set order_date = " + new_order_date + " where id_delivery = " + id_delivery)

                    elif num_update == 3:
                        new_delivery_date = input('\nВведите новую дату доставки: ')
                        mycursor.execute(
                            "update delivery set delivery_date = " + new_delivery_date + " where id_delivery = " + id_delivery)

                    db_name.commit()
                    print('\nЗапись доставки успешно изменена')

                # Удаление записи
                if num_act == 4:

                    id_delivery = input('\nВведите Id доставки: ')
                    mycursor.execute("delete from delivery where id_delivery = " + id_delivery)

                    # Принять изменения
                    db_name.commit()
                    print('Запись доставки успешно удалена')

            else:
                print('\nВыбранной таблицы не существует!')

        elif num == 2:
            print('\nАналитические запросы:\n1. Количество продаж определённой марки автомобиля\n2. Количество заказов оплаченных определённым способом(Б/Н)\n3. Количество продаж в определённом году')
            num_query = int(input('\nВведите номер аналитического запроса: '))

            if num_query == 1:
                brand = input('\nВведите марку автомобиля: ')
                mycursor.execute('select brand, count(*) from car where brand = "' + brand + '"')
                mytable = PrettyTable()
                mytable.field_names = ['Car_brand', 'Count_of_sales']
                mytable.add_rows(mycursor.fetchall())
                print(mytable)

            elif num_query == 2:
                payment_method = input('\nВведите способ оплаты(Б/Н): ')
                mycursor.execute('select payment_method, count(*) from ordering where payment_method = ' + '"' + payment_method + '"')
                mytable = PrettyTable()
                mytable.field_names = ['Payment_method', 'Count_of_sales']
                mytable.add_rows(mycursor.fetchall())
                print(mytable)

            elif num_query == 3:
                year_registration_date = input('\nВведите год регистрации заказа(ГГГГ): ')
                mycursor.execute('select year(registration_date), count(*) from ordering where year(registration_date) = ' + '"' + year_registration_date + '" group by year(registration_date)')
                mytable = PrettyTable()
                mytable.field_names = ['Year', 'Count_of_sales']
                mytable.add_rows(mycursor.fetchall())
                print(mytable)

            else:
                print('\nНомер выбранного запроса не существует!')

        elif num == 3:
            action = False

            # Закрытие курсора и БД
            mycursor.close()
            db_name.close()
            exit()

        else:
            print('\nВыбранного номера не существует!')

        # Закрытие курсора и БД
        mycursor.close()
        db_name.close()

except Exception as ex:
    print("Error...")
    print(ex)