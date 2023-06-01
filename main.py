from prettytable import PrettyTable
import mysql.connector
from config import host, user, password, database
import CRUD

# Соединение с БД
try:
    db_name = mysql.connector.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = database
    )
    print("Successfully connected...")
    action = True
    while action == True:
        print('\n1. Таблицы\n2. Аналитические запросы\n3. Закончить работу')
        num = int(input('\nВведите номер для продолжения: '))
        mycursor = db_name.cursor()  # Объявление курсора

        if num == 1:

            # Выбор таблицы для взаимодействия
            print('\nТаблицы:\n1. Customer\n2. Ordering\n3. Employee\n4. Car\n5. Equipment\n6. Insurance\n')
            num_table = int(input('Введите номер таблицы для взаимодействия: '))

            # Клиент
            if num_table == 1:
                print('\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('Введите номер действия: '))

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

                    print('Запись клиента успешно добавлена')

                # Читать запись
                elif num_act == 2:
                    print('\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email')
                    num_search = int(input('Введите номер колонки, по которой будет производиться поиск клиента: '))

                    if num_search == 1:
                        id_customer = input('\nВведите Id клиента: ')
                        CRUD.read_customer(num_search, 'id_customer', id_customer)

                    if num_search == 2:
                        full_name = input('\nВведите ФИО клиента: ')
                        CRUD.read_customer(num_search, 'full_name', full_name)

                    if num_search == 3:
                        phone_number = input('\nВведите номер телефона клиента: ')
                        CRUD.read_customer(num_search, 'phone_number', phone_number)

                    if num_search == 4:
                        address = input('\nВведите адрес клиента: ')
                        CRUD.read_customer(4, 'adress', address)

                    if num_search == 5:
                        date_of_birth = input('\nВведите дату рождения клиента(ГГГГ-ММ-ДД): ')
                        CRUD.read_customer(5, 'date_of_birth', date_of_birth)

                    if num_search == 6:
                        email = input('\nВведите Email клиента: ')
                        CRUD.read_customer(6, 'email', email)

                # Редактировать запись
                elif num_act == 3:
                    id_customer = input('Введите Id клиента: ')
                    print('\nКолонки:\n1. Id customer\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n')
                    num_update = int(input('Введите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_customer = input('Введите новое Id клиента: ')
                        mycursor.execute("update customer set id_customer = " + new_id_customer + " where id_customer = " + id_customer)

                    if num_update == 2:
                        new_full_name = input('Введите новое ФИО клиента: ')
                        mycursor.execute("update customer set full_name = " + "'" + new_full_name + "'" + " where id_customer = " + id_customer)

                    if num_update == 3:
                        new_phone_number = input('Введите новый телефон клиента: ')
                        mycursor.execute("update customer set phone_number = " + "'" + new_phone_number + "'" + " where id_customer = " + id_customer)

                    if num_update == 4:
                        new_address = input('Введите новый адрес клиента: ')
                        mycursor.execute("update customer set adress = " + "'" + new_address + "'" + " where id_customer = " + id_customer)

                    if num_update == 5:
                        new_date_of_birth = input('Введите новую дату рождения клиента(ГГГГ-ММ-ДД): ')
                        mycursor.execute("update customer set date_of_birth = " + "'" + new_date_of_birth + "'" + " where id_customer = " + id_customer)

                    if num_update == 6:
                        new_email = input('Введите новый Email клиента: ')
                        mycursor.execute("update customer set email = " + "'" + new_email + "'" + " where id_customer = " + id_customer)

                    # Принять изменения
                    db_name.commit()

                    print('Запись клиента успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email')
                    num_delete = int(input('\nВведите номер колонки, по которой будет производиться удаление клиента: '))

                    if num_delete == 1:
                        id_customer = input('Введите Id клиента: ')
                        CRUD.delete_customer(1, 'id_customer', id_customer)

                    elif num_delete == 2:
                        full_name = input('\nВведите ФИО клиента: ')
                        CRUD.delete_customer(2, 'full_name', full_name)

                    elif num_delete == 3:
                        phone_number = input('Введите номер телефона клиента: ')
                        CRUD.delete_customer(3, 'phone_number', phone_number)

                    elif num_delete == 4:
                        address = input('Введите адрес клиента: ')
                        CRUD.delete_customer(3, 'adress', address)

                    elif num_delete == 5:
                        date_of_birth = input('Введите дату рождения клиента: ')
                        CRUD.delete_customer(4, 'date_of_birth', date_of_birth)

                    elif num_delete == 6:
                        email = input('Введите Email клиента: ')
                        CRUD.delete_customer(5, 'email', email)

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
                num_act = int(input('Введите номер действия: '))

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
                        'insert into Ordering(id_order, payment_method, registration_date, total_amount, id_customer, id_car, id_employee) values (' + id_order + ',"' + payment_method + '","' + registration_date + '","' + total_amount + '",' + id_customer + ',' + id_car + ',' + id_employee + ')')

                    print('Запись заказа успешно добавлена')

                # Читать запись
                elif num_act == 2:

                    print('\n1. Id\n2. Payment method\n3. Registration date\n4. Total amount\n5. Full name customer\n6. Full name employee\n7. Car brand\n')
                    num_search = int(input('Введите номер колонки, по которой будет производиться поиск заказа: '))

                    if num_search == 1:
                        id_order = input('\nВведите Id заказа: ')
                        CRUD.read_order(1, 'Id_ordering', id_order)

                    if num_search == 2:
                        payment_method = input('\nВведите способ оплаты заказа(Б/Н): ')
                        CRUD.read_order(2, 'payment_method', payment_method)

                    if num_search == 3:
                        registration_date = input('\nВведите дату регистрации заказа(Б/Н): ')
                        CRUD.read_order(3, 'registration_date', registration_date)

                    if num_search == 4:
                        total_amount = input('\nВведите итоговую цену заказа: ')
                        CRUD.read_order(3, 'total_amount', total_amount)

                    if num_search == 5:
                        full_name_customer = input('\nВведите ФИО клиента: ')
                        CRUD.read_order(3, 'customer.full_name', full_name_customer)

                    if num_search == 6:
                        full_name_employee = input('\nВведите ФИО сотруника: ')
                        CRUD.read_order(3, 'employee.full_name', full_name_employee)

                    if num_search == 7:
                        brand = input('Введите марку автомобиля: ')
                        CRUD.read_order(3, 'car.brand', brand)

                # Редактировать запись
                elif num_act == 3:
                    id_order = input('\nВведите Id заказа: ')
                    print('\nКолонки:\n1. Id order\n2. Payment method\n3. Registration date\n4. Total amount\n5. Id customer\n6. Id employee\n7. Id car\n')
                    num_update = int(input('Введите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_order = input('\nВведите новое Id заказа: ')
                        mycursor.execute(
                            "update ordering set id_ordering = " + new_id_order + " where id_ordering = " + id_order)

                    if num_update == 2:
                        new_payment_method = input('Введите новый метод оплаты заказа(Б/Н): ')
                        mycursor.execute(
                            "update ordering set payment_method = " + "'" + new_payment_method + "'" + " where id_ordering = " + id_order)

                    if num_update == 3:
                        new_registration_date = input('Введите новую дату регистрации заказа(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update ordering set registration_date = " + "'" + new_registration_date + "'" + " where id_ordering = " + id_order)

                    if num_update == 4:
                        new_total_amount = input('Введите новую итоговую цену заказа: ')
                        mycursor.execute(
                            "update ordering set total_amount = " + "'" + new_total_amount + "'" + " where id_ordering = " + id_order)

                    if num_update == 5:
                        new_id_customer = input('Введите новое Id клиента: ')
                        mycursor.execute(
                            "update ordering set id_customer = " + "'" + new_id_customer + "'" + " where id_ordering = " + id_order)

                    if num_update == 6:
                        new_id_employee = input('Введите новое Id сотрудника: ')
                        mycursor.execute(
                            "update ordering set id_employee = " + "'" + new_id_employee + "'" + " where id_ordering = " + id_order)

                    if num_update == 7:
                        new_id_car = input('Введите новое Id автомобиля: ')
                        mycursor.execute(
                            "update ordering set id_car = " + "'" + new_id_car + "'" + " where id_ordering = " + id_order)

                    print('Запись заказа успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\n1. Id order\n2. Payment method\n3. Registartion date\n4. Total amount\n5. Full name customer\n6. Brand and model car\n7. Full name employee')

                    num_delete = int(
                        input('\nВведите номер колонки, по которой будет производиться удаление заказа: '))

                    if num_delete == 1:
                        id_order = input('Введите Id заказа: ')
                        mycursor.execute("delete from ordering where id_ordering = " + id_order)

                    elif num_delete == 2:
                        payment_method = input('\nВведите способ оплаты заказа(Б/Н): ')
                        CRUD.delete_order(2, 'payment_method', payment_method)

                    elif num_delete == 3:
                        registration_date = input('Введите дату регистрации заказа: ')
                        CRUD.delete_order(3, 'registration_date', registration_date)

                    elif num_delete == 4:
                        total_amount = input('Введите итоговую цену заказа: ')
                        CRUD.delete_order(4, 'total_amount', total_amount)

                    elif num_delete == 5:
                        full_name_customer = input('Введите ФИО клиента: ')
                        CRUD.delete_order(5, 'customer.full_name', full_name_customer)

                    elif num_delete == 6:
                        brand_and_model = input('Введите марку и модель автомобиля: ')
                        CRUD.delete_order(5, 'concat(car.brand, " ", car.model)', brand_and_model)

                    elif num_delete == 7:
                        full_name_employee = input('Введите ФИО сотрудника: ')
                        CRUD.delete_order(5, 'employee.full_name', full_name_employee)

                    else:
                        print('\nНомера выбранной колонки не существует')

                else:
                    print('\nНомер выбранного действия не существует!')

            # Сотрудник
            elif num_table == 3:
                print('\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('Введите номер действия: '))

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

                    print('Запись сотрудника успешно добавлена')

                # Читать запись
                elif num_act == 2:

                    print('\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n7. Salary')
                    num_search = int(input('Введите номер колонки, по которой будет производиться поиск сотрудника: '))

                    if num_search == 1:
                        id_employee = input('\nВведите Id сотрудника: ')
                        CRUD.read_employee(1, 'id_employee', id_employee)

                    if num_search == 2:
                        full_name = input('\nВведите ФИО сотрудника: ')
                        CRUD.read_employee(2, 'full_name', full_name)

                    if num_search == 3:
                        phone_number = input('\nВведите номер телефона сотрудника: ')
                        CRUD.read_employee(3, 'phone_number', phone_number)

                    if num_search == 4:
                        address = input('\nВведите адрес сотрудника: ')
                        CRUD.read_employee(4, 'adress', address)

                    if num_search == 5:
                        date_of_birth = input('\nВведите дату рождения сотрудника: ')
                        CRUD.read_employee(5, 'date_of_birth', date_of_birth)

                    if num_search == 6:
                        email = input('\nВведите Email сотрудника: ')
                        CRUD.read_employee(6, 'email', email)

                    if num_search == 7:
                        salary = input('\nВведите заработную плату сотрудника: ')
                        CRUD.read_employee(7, 'salary', salary)

                # Редактировать запись
                elif num_act == 3:
                    id_employee = input('\nВведите Id сотрудника: ')
                    print('\nКолонки:\n1. Id_employee\n2. Full_name\n3. Phone_number\n4. Address\n5. Date_of_birth\n6. Email\n7. Salary\n')
                    num_update = int(input('Введите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_employee = input('\nВведите новое Id сотрудника: ')
                        mycursor.execute(
                            "update employee set id_employee = " + new_id_employee + " where id_employee = " + id_employee)

                    if num_update == 2:
                        new_full_name = input('Введите новое ФИО сотрудника: ')
                        mycursor.execute(
                            "update employee set full_name = " + "'" + new_full_name + "'" + " where id_employee = " + id_employee)

                    if num_update == 3:
                        new_phone_number = input('Введите новый телефон сотрудника: ')
                        mycursor.execute(
                            "update employee set phone_number = " + "'" + new_phone_number + "'" + " where id_employee = " + id_employee)

                    if num_update == 4:
                        new_address = input('Введите новый адрес сотрудника: ')
                        mycursor.execute(
                            "update employee set adress = " + "'" + new_address + "'" + " where id_employee = " + id_employee)

                    if num_update == 5:
                        new_date_of_birth = input('Введите новую дату рождения сотрудника(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update employee set date_of_birth = " + "'" + new_date_of_birth + "'" + " where id_employee = " + id_employee)

                    if num_update == 6:
                        new_email = input('Введите новый Email сотрудника: ')
                        mycursor.execute(
                            "update employee set email = " + "'" + new_email + "'" + " where id_employee = " + id_employee)

                    if num_update == 7:
                        new_email = input('Введите новую заработную плату сотрудника: ')
                        mycursor.execute(
                            "update employee set email = " + "'" + new_email + "'" + " where id_employee = " + id_employee)

                    print('Запись сотрудника успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\n1. Id\n2. Full name\n3. Phone number\n4. Address\n5. Date of birth\n6. Email\n7. Salary')
                    num_delete = int(
                        input('\nВведите номер колонки, по которой будет производиться удаление сотрудника: '))

                    if num_delete == 1:
                        id_employee = input('Введите Id сотрудника: ')
                        CRUD.delete_employee(1, 'id_employee', id_employee)

                    elif num_delete == 2:
                        full_name = input('\nВведите ФИО сотрудника: ')
                        CRUD.delete_employee(2, 'full_name', full_name)

                    elif num_delete == 3:
                        phone_number = input('Введите номер телефона сотрудника: ')
                        CRUD.delete_employee(3, 'phone_number', phone_number)

                    elif num_delete == 4:
                        address = input('Введите адрес сотрудника: ')
                        CRUD.delete_employee(4, 'adress', address)

                    elif num_delete == 5:
                        date_of_birth = input('Введите дату рождения сотрудника: ')
                        CRUD.delete_employee(5, 'date_of_birth', date_of_birth)

                    elif num_delete == 6:
                        email = input('Введите Email сотрудника: ')
                        CRUD.delete_employee(6, 'email', email)

                    elif num_delete == 7:
                        salary = input('Введите заработную плату сотрудника: ')
                        CRUD.delete_employee(7, 'salary', salary)

                    else:
                        print('\nНомера выбранной колонки не существует')

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
                    year_of_release = input('Введите дату выпуска автомобиля(ГГГГ-ММ-ДД): ')
                    price = input('Введите цену автомобиля: ')
                    color = input('Введите цвет автомобиля: ')
                    id_equipment = input('Введите Id комплектации автомобиля: ')
                    id_insurance = input('Введите Id страховки автомобиля: ')

                    mycursor.execute(
                        'insert into сar(id_car, brand, model, year_of_release, price, color, id_equipment, id_insurance) values (' + id_car + ',"' + brand + '","' + model + '","' + year_of_release + '","' + price + '",' + id_equipment + ',' + id_insurance + ')')

                    print('Запись заказа успешно добавлена')

                # Читать запись
                elif num_act == 2:

                    print('\n1. Id\n2. Brand\n3. Model\n4. Year of release\n5. Price\n6. Color\n')
                    num_search = int(input('Введите номер колонки, по которой будет производиться поиск автомобиля: '))

                    if num_search == 1:
                        id_car = input('Введите Id автомобиля: ')
                        CRUD.read_car(1, 'id_car', id_car)

                    if num_search == 2:
                        brand = input('Введите марку автомобиля: ')
                        CRUD.read_car(2, 'brand', brand)

                    if num_search == 3:
                        brand_and_model = input('Введите марку и модель автомобиля: ')
                        CRUD.read_car(3, 'concat(brand, " ", model)', brand_and_model)

                    if num_search == 4:
                        year_of_release = input('Введите год выпуска автомобиля: ')
                        CRUD.read_car(4, 'year_of_release', year_of_release)

                    if num_search == 5:
                        price = input('Введите цену автомобиля: ')
                        CRUD.read_car(5, 'price', price)

                    if num_search == 6:
                        color = input('Введите цвет автомобиля: ')
                        CRUD.read_car(6, 'color', color)

                # Редактировать запись
                elif num_act == 3:
                    id_car = input('\nВведите Id автомобиля: ')
                    print('\nКолонки:\n1. Id_car\n2. Brand and model\n3. Model\n4. Year of release\n5. Price\n6. Color\n7. Id equipment\n8. Id insurance\n')
                    num_update = int(input('Введите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_car = input('Введите новое Id заказа: ')
                        mycursor.execute(
                            "update car set id_ordering = " + new_id_car + " where id_car = " + id_car)

                    if num_update == 2:
                        new_brand_and_model = input('Введите новую марку и модель автомобиля: ')
                        new_brand_and_model = new_brand_and_model.split()
                        new_brand = new_brand_and_model[0]
                        new_model = new_brand_and_model[1]
                        for value in new_brand_and_model[2:len(new_brand_and_model)]:
                            new_model = new_model + ' ' + value
                        mycursor.execute(
                            "update car set brand = " + "'" + new_brand + "'" + " where id_car = " + id_car)
                        mycursor.execute(
                            "update car set model = " + "'" + new_model + "'" + " where id_car = " + id_car)

                    if num_update == 3:
                        new_model = input('Введите новую модель автомобиля: ')
                        mycursor.execute(
                            "update car set model = " + "'" + new_model + "'" + " where id_car = " + id_car)

                    if num_update == 4:
                        new_year_of_release = input('Введите новую дату выпуска автомобиля(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update car set year_of_release = " + "'" + new_year_of_release + "'" + " where id_car = " + id_car)

                    if num_update == 5:
                        new_price = input('Введите новую цену автомобиля: ')
                        mycursor.execute(
                            "update car set price = " + "'" + new_price + "'" + " where id_car = " + id_car)

                    if num_update == 6:
                        new_color = input('Введите новый цвет автомобиля: ')
                        mycursor.execute(
                            "update car set color = " + "'" + new_color + "'" + " where id_car = " + id_car)

                    if num_update == 7:
                        new_id_equipment = input('Введите новое Id комплектации: ')
                        mycursor.execute(
                            "update car set id_equipment = " + "'" + new_id_equipment + "'" + " where id_car = " + id_car)

                    if num_update == 8:
                        new_id_insurance = input('Введите новое Id страховки: ')
                        mycursor.execute(
                            "update car set id_insurance = " + "'" + new_id_insurance + "'" + " where id_car = " + id_car)

                    print('Запись автомобиля успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    print('\n1. Id\n2. Brand and model\n3. Year of release\n4. Price\n5. Color\n')
                    num_delete = int(input('\nВведите номер колонки, по которой будет производиться удаление клиента: '))

                    if num_delete == 1:
                        id_car = input('Введите Id автомобиля: ')
                        CRUD.delete_car(1, 'id_car', id_car)

                    elif num_delete == 2:
                        brand_and_model = input('Введите марку и модель автомобиля: ')
                        CRUD.delete_car(2, 'concat(brand, " ", model)', brand_and_model)

                    elif num_delete == 3:
                        year_of_release = input('Введите год релиза автомобиля(ГГГГ-ММ-ДД): ')
                        CRUD.delete_car(3, 'year_of_release', year_of_release)

                    elif num_delete == 4:
                        price = input('Введите цену автомобиля: ')
                        CRUD.delete_car(4, 'price', price)

                    elif num_delete == 5:
                        color = input('Введите цвет автомобиля')
                        CRUD.delete_car(5, 'color', color)

                    else:
                        print('\nНомера выбранной колонки не существует')

                else:
                    print('\nНомер выбранного действия не существует!')

            # Комплектация автомобиля
            elif num_table == 5:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('Введите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_equipment = input('\nВведите Id комплектации: ')
                    gearbox_type = input('Введите тип КПП комплектации: ')
                    car_interior = input('Введите отделку интерьера комплектации: ')
                    electrical_equipment = input('Введите электрооборудование комплектации: ')

                    mycursor.execute(
                        'insert into equipment(id_equipment, gearbox_type, car_interior, electrical_equipment) values (' + id_equipment + ',"' + gearbox_type + '","' + car_interior + '","' + electrical_equipment + '")')
                    print('Запись комлектации успешно добавлена')

                # Читать запись
                elif num_act == 2:
                    id_equipment = input('Введите Id комплектации: ')
                    mycursor.execute(
                        "select * from equipment where id_equipment = " + id_equipment)
                    mytable = PrettyTable()
                    mytable.field_names = ['Id_equipment', 'Gearbox_type', 'Car_interior', 'Electrical_equipment']
                    mytable.add_rows(mycursor.fetchall())
                    print(mytable)

                # Редактировать запись
                elif num_act == 3:
                    id_equipment = input('\nВведите Id комплектации: ')
                    print('\nКолонки:\n1. Id_equipment\n2. Gearbox_type\n3. Car_interior\n4. Electrical_equipment\n')
                    num_update = int(input('Введите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_equipment = input('Введите новое Id комлектации: ')
                        mycursor.execute(
                            "update equipment set id_equipment = " + new_id_equipment + " where id_equipment = " + id_equipment)

                    if num_update == 2:
                        new_gearbox_type = input('Введите новый тип КПП комлектации: ')
                        mycursor.execute(
                            "update equipment set gearbox_type = " + "'" + new_gearbox_type + "'" + " where id_equipment = " + id_equipment)

                    if num_update == 3:
                        new_car_interior = input('Введите новую отделку интерьера комлектации: ')
                        mycursor.execute(
                            "update equipment set car_interior = " + "'" + new_car_interior + "'" + " where id_equipment = " + id_equipment)

                    if num_update == 4:
                        new_electrical_equipment = input('Введите новое электрооборудование комплектации: ')
                        mycursor.execute(
                            "update equipment set electrical_equipment = " + "'" + new_electrical_equipment + "'" + " where id_equipment = " + id_equipment)

                    print('Запись комплектации успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    id_equipment = input('Введите Id комлектации: ')
                    mycursor.execute("delete from equipment where id_equipment = " + id_equipment)
                    print('Запись комлектации успешно удалена')

                else:
                    print('\nНомер выбранного действия не существует!')

            # Страховка автомобиля
            elif num_table == 6:
                print(
                    '\nДействия с таблицей:\n1. Создать запись\n2. Читать запись\n3. Редактировать запись\n4. Удалить запись\n')
                num_act = int(input('Введите номер действия: '))

                # Создать запись
                if num_act == 1:
                    id_insurance = input('\nВведите Id страховки: ')
                    insurance_number = input('Введите номер страховки: ')
                    start_date = input('Введите дату начала действия страховки(ГГГГ-ММ-ДД): ')
                    end_date = input('Введите дату окончания действия страховки(ГГГГ-ММ-ДД): ')

                    mycursor.execute(
                        'insert into insurance(id_insurance, insurance_number, start_date, end_date) values (' + id_insurance + ',' + insurance_number + ',"' + start_date + '","' + end_date + '")')
                    print('Запись страховки успешно добавлена')

                # Читать запись
                elif num_act == 2:
                    print('\n1. Id\n2. Insurance number\n')
                    num_search = int(input('Введите номер колонки, по которой будет производиться поиск сотрудника: '))

                    if num_search == 1:
                        id_insurance = input('Введите Id страховки: ')
                        mycursor.execute(
                            "select * from insurance where id_insurance = " + id_insurance)
                        mytable = PrettyTable()
                        mytable.field_names = ['Id_insurance', 'Insurance_number', 'Start_date', 'End_date']
                        mytable.add_rows(mycursor.fetchall())
                        print(mytable)

                    if num_search == 2:
                        insurance_number = input('Введите номер страховки: ')
                        mycursor.execute(
                            "select * from insurance where insurance_number = " + insurance_number)
                        mytable = PrettyTable()
                        mytable.field_names = ['Id_insurance', 'Insurance_number', 'Start_date', 'End_date']
                        mytable.add_rows(mycursor.fetchall())
                        print(mytable)

                # Редактировать запись
                elif num_act == 3:
                    id_insurance = input('\nВведите Id страховки: ')
                    print('\nКолонки:\n1. Id_insurance\n2. Insurance_number\n3. Start_date\n4. End_date\n')
                    num_update = int(input('Введите номер колонки для изменения: '))

                    if num_update == 1:
                        new_id_insurance = input('Введите новое Id страховки: ')
                        mycursor.execute(
                            "update insurance set id_insurance = " + new_id_insurance + " where id_insurance = " + id_insurance)

                    if num_update == 2:
                        new_insurance_number = input('Введите новый номер страховки: ')
                        mycursor.execute(
                            "update insurance set insurance_number = " + "'" + new_insurance_number + "'" + " where id_insurance = " + id_insurance)

                    if num_update == 3:
                        new_start_date = input('Введите новую дату начала действия страховки(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update insurance set start_date = " + "'" + new_start_date + "'" + " where id_insurance = " + id_insurance)

                    if num_update == 4:
                        new_end_date = input('Введите новую дату окончания действия страховки(ГГГГ-ММ-ДД): ')
                        mycursor.execute(
                            "update insurance set end_date = " + "'" + new_end_date + "'" + " where id_insurance = " + id_insurance)

                    print('Запись страховки успешно изменена')

                # Удалить запись
                elif num_act == 4:
                    id_insurance = input('Введите Id страховки: ')
                    mycursor.execute("delete from insurance where id_insurance = " + id_insurance)
                    print('Запись страховки успешно удалена')

                else:
                    print('\nНомер выбранного действия не существует!')

            else:
                print('\nВыбранной таблицы не существует!')

            # Принять изменения
            db_name.commit()
        
        elif num == 2:
            print('\nАналитические запросы:\n1. Количество продаж определённой марки автомобиля\n2. Вывести количество заказов оплаченных определённым способом(Б/Н)\n3. Вывести количество продаж в определённом году')
            num_query = int(input('\nВведите номер аналитического запроса: '))

            if num_query == 1:
                brand = input('Введите марку автомобиля: ')
                mycursor.execute('select brand, count(*) from car where brand = "' + brand + '"')
                mytable = PrettyTable()
                mytable.field_names = ['Car_brand', 'Count_of_sales']
                mytable.add_rows(mycursor.fetchall())
                print(mytable)

            elif num_query == 2:
                payment_method = input('Введите способ оплаты(Б/Н): ')
                mycursor.execute('select payment_method, count(*) from ordering where payment_method = ' + '"' + payment_method + '"')
                mytable = PrettyTable()
                mytable.field_names = ['Payment_method', 'Count_of_sales']
                mytable.add_rows(mycursor.fetchall())
                print(mytable)

            elif num_query == 3:
                year_registration_date = input('Введите год регистрации заказа(ГГГГ): ')
                mycursor.execute('select year(registration_date), count(*) from ordering where year(registration_date) = ' + '"' + year_registration_date + '" group by year(registration_date)')
                mytable = PrettyTable()
                mytable.field_names = ['Year', 'Count_of_sales']
                mytable.add_rows(mycursor.fetchall())
                print(mytable)

            else:
                print('\nНомер выбранного запроса не существует!')

        elif num == 3:
            action = False
            exit()

        else:
            print('\nВыбранного номера не существует!')

        mycursor.close()

except Exception as ex:
    print("Error...")
    print(ex)

finally:
    db_name.close()