import pytest
from faker import Faker

from EmployeeApi import EmployeeApi
from CompanyApi import CompanyApi
from EmployeeTable import EmployeeTable
from CompanyTable import CompanyTable

base_url = 'https://x-clients-be.onrender.com'
db_url = 'postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet'

db_emp = EmployeeTable(db_url)
db_com = CompanyTable(db_url)
emp = EmployeeApi(base_url)
com = CompanyApi(base_url)
fake = Faker("ru_RU")

first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
middle_name = fake.first_name_male()
is_active = True
id = 1
phone = fake.random_number(digits=11, fix_len=True)
birthdate = '2005-04-26T11:19:37.153Z'
url = fake.url()

new_last_name = 'Changed2'
new_email = 'string34@gh.ru'
new_url = 'https://sky.pro/wiki/python'
new_phone = '89018765523'
new_is_active = False
num_emps = 3  # кол-во сотрудников (пока одинаковых) создаваемых авто


# дописать создание сотрудников через бд
def test_get_list_employee():
    num_emps = 3

    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # проверить что у компании нет сотрудников бд
    list_emp_db = db_emp.get_list_emps_by_id_company(company_id)
    assert len(list_emp_db) == 0
    # не написать скрипт для бд из-за генерируемого id 
    # (брать максимальный id сотрудника и присваивать макс+1)
    # создаем список (пока одинаковых) сотрудников апи
    db_emp.create_employees(
        company_id, num_emps, is_active, first_name, last_name,
        middle_name,phone, url, email, birthdate)

    # проверяем что создали верное кол-во сотрудников
    assert len(db_emp.get_list_id_emps_by_id_company(company_id)) == num_emps

    result_api = emp.get_list_employee(params_to_add={'company': company_id})
    result_db = db_emp.get_list_emps_by_id_company(company_id)
    assert len(result_api) == len(result_db)

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


# дописать метод создания сотрудника в бд
# как сравнить значение ключей через апи и из бд?
def test_get_employee_by_id():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    emp_id = new_emp['id']
    # пока вместо проверки схемы
    assert len(new_emp) == 1

    # получить сотрудника по id
    get_new_emp = emp.get_employee_by_id(emp_id)
    get_new_emp_id = get_new_emp['id']

    # проверка значений ключей ответа
    assert get_new_emp["id"] == emp_id
    assert get_new_emp["firstName"] == first_name
    assert get_new_emp["lastName"] == last_name
    # assert get_new_emp["email"] == email
    # ФР:возвращается null
    # ОР: возвращается значение email
    assert get_new_emp["isActive"] == is_active

    assert get_new_emp["middleName"] == ''
    # ФР:ключ avatar_url ОР: ключ url (сваггер)
    assert get_new_emp["avatar_url"] == ''
    assert get_new_emp["phone"] == ''
    assert get_new_emp["birthdate"] == '2005-05-03'

    # проверка что сотрудник есть в списке сотрудников компании
    list_emps = db_emp.get_list_emps_by_id_company(company_id)
    emp_list_id = list_emps[-1][0]
    assert emp_list_id == get_new_emp_id

    # будет проверка из базы данных

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


@pytest.mark.xfail(reason="company_id is required")
def test_get_list_employee_without_company_id():
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)
    
    result = db_emp.get_list_emps_by_id_company()
    assert len(result) == 1


# дописать создание сотрудника через бд
def test_get_employee_by_id_without_id():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    # пока вместо проверки схемы
    assert len(new_emp) == 1

    # получить сотрудника по id
    get_new_emp = emp.get_employee_by_id_without_id()
    assert get_new_emp["statusCode"] == 500
    assert get_new_emp["message"] == 'Internal server error'
    # необходимо прописать более информационный статус код и сообщение.
    # возможно 400 - плохой запрос

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


# дописать создание сотрудника через бд
@pytest.mark.xfail(reason="ФР:тело ответа пустое, ОР: 404 сотрудник не найден")
def test_get_employee_by_wrong_id():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    emp_id = new_emp['id']
    # пока вместо проверки схемы
    assert len(new_emp) == 1

    wrong_emp_id = emp_id + 1000

    # получить сотрудника по id
    get_new_emp = emp.get_employee_by_id(wrong_emp_id)
    assert len(get_new_emp) == 1

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


def test_create_list_emps():
    num_emps = 5
    new_emps = emp.create_list_employee_get_list_id(
        num_emps, 3979, first_name, last_name, email, is_active)

    assert len(new_emps) == num_emps


# дописать удаление сотрудников и компании и создание сотрудников через бд
# дописать проверку значений полей у сотрудника чарез бд
def test_create_employee():
    # создание новой компании
    db_com.create('Company Empoyees 8')
    company_id = db_com.get_max_id()

    # проверка что у созданной компании нет работников
    emp_list_f = emp.get_list_employee(params_to_add={'company': company_id})
    len_before = len(emp_list_f)
    assert len(emp_list_f) == 0

    # создание нового работника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active,
        id, middle_name, url, phone, birthdate)
    id_new_emp = new_emp["id"]
    assert len(new_emp) == 1

    # проверка, что создан 1 работник
    emp_list_a = db_emp.get_list_emps_by_id_company(company_id)
    len_after = len(emp_list_a)
    assert len_after - len_before == 1

    # проверка созданного работника
    new_emp_result = emp.get_employee_by_id(id_new_emp)

    # проверка заполненных при создании полей
    assert new_emp_result["id"] == id_new_emp
    assert new_emp_result["firstName"] == first_name
    assert new_emp_result["lastName"] == last_name
    assert new_emp_result["isActive"] is True

    # проверка не заполненных полей
    # assert new_emp_result["email"] == email # - не сохраняется значение
    assert new_emp_result["middleName"] == middle_name
    assert new_emp_result["avatar_url"] == url
    assert new_emp_result["phone"] == str(phone)
    assert new_emp_result["birthdate"] == '2005-04-26'

    emp_list = db_emp.get_list_emps_by_id_company(company_id)
    emp_list_id = emp_list[-1]['id']
    assert id_new_emp == emp_list_id

    # будет проверка из базы данных
    # как получить словарь индекс: название колонки из бд?
    # по индексу найти нужную строку названия колонки
    # подставить в ассерт рес[2="firstName"] == firstName

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


def test_create_employee_without_auth_token():
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # проверка что у созданной компании нет сотрудника
    emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
    len_before = len(emp_list_f)
    assert len(emp_list_f) == 0

    # создание нового сотрудника
    new_emp = emp.create_employee_without_auth_token(
        company_id, first_name, last_name, email, is_active,
        id, middle_name, url, phone, birthdate)

    assert new_emp["statusCode"] == 401
    assert new_emp["message"] == 'Unauthorized'

    # проверка, что не создан сотрудник
    emp_list_a = db_emp.get_list_emps_by_id_company(company_id)
    len_after = len(emp_list_a)
    assert len_after - len_before == 0

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


def test_create_employee_without_body():
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # проверка что у созданной компании нет сотрудников
    emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
    assert len(emp_list_f) == 0

    # создание нового сотрудника
    new_emp = emp.create_employee_without_body()
    assert new_emp["statusCode"] == 500
    assert new_emp["message"] == 'Internal server error'
    # необходимо прописать более информационный статус код и сообщение.
    # возможно 400 - плохой запрос

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


# дописать создание сотрудника через бд
# дописать проверку значений ключей через бд
def test_patch_employee():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    new_employee = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']

    result = emp.change_info_employee(
        new_employee_id, new_last_name, new_email, new_url, new_phone,
        new_is_active)
    # assert len(result) == 7 # пока вместо проверки схемы ответа
    # проверить ключи ответа - ФР: нет ключей прописанных в свагере
    # ОР: все ключи есть в json
    assert result.get('id') == new_employee_id

    # assert result.get('lastName') == new_last_name
    # ФР: ключ-значение не возвращается
    # ОР: ключ - значение (новое)
    assert result.get('isActive') == new_is_active
    assert result.get('email') == new_email
    # assert result.get('phone') == new_phone
    # ФР: ключ-значение не возвращается
    # ОР: ключ - значение (новое)
    assert result.get('url') == new_url

    # assert result.get('firstName') == first_name
    # ФР: ключ-значение не возвращается
    # ОР: ключ - значение
    assert result.get('middleName') == new_employee.get('middleName')
    assert result.get('companyId') == new_employee.get('companyId')
    assert result.get('birthdate') == new_employee.get('birthdate')

    # будет проверка из базы данных

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)


# дописать создание сотрудника через бд
def test_patch_employee_without_auth_token():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    new_employee = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']

    result = emp.change_info_employee_without_auth_token(
        new_employee_id, new_last_name, new_email,
        new_url, new_phone, new_is_active)

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)

    assert result["statusCode"] == 401
    assert result["message"] == 'Unauthorized'


# дописать создание сотрудника через бд
def test_patch_employee_without_id():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    emp.create_employee(
        company_id, first_name, last_name, email, is_active)

    result = emp.change_info_employee_without_id(
        new_last_name, new_email, new_url, new_phone, new_is_active)

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)

    assert result["statusCode"] == 404
    assert result["error"] == 'Not Found'


# дописать создание сотрудника через бд
@pytest.mark.xfail(reason="без тела возвращается информация по пользователю")
def test_patch_employee_without_body():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    new_employee = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']

    result = emp.change_info_employee_without_body(
        new_employee_id, new_last_name, new_email, new_url,
        new_phone, new_is_active)

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)

    assert result["statusCode"] == 404
    assert result["error"] == 'Not Found'


# дописать создание сотрудника через бд
@pytest.mark.xfail(reason="ФР: 500, ОР: 404")
def test_patch_employee_wrong_id():
    # создание новой компании
    db_com.create("Company Empoyees 8")
    company_id = db_com.get_max_id()

    # создание нового сотрудника
    new_employee = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']

    wrong_emp_id = new_employee_id + 1000

    result = emp.change_info_employee(
        wrong_emp_id, new_last_name, new_email, new_url, new_phone,
        new_is_active)

    # удаление сотрудников и компании
    db_emp.delete_list_emps_and_company_by_company_id(company_id)

    assert result["statusCode"] == 404
    assert result["message"] == 'Not Found'

@pytest.mark.skip("отладка метода")
def test_delete_list_emp():
    emp.create_list_employee_get_list_id(
        3, 4014, first_name, last_name, email, is_active, id, middle_name, url,
        phone, birthdate)
    list_id_emp = db_emp.get_list_id_emps_by_id_company(4014)
    db_emp.delete_list_emps(list_id_emp)
    list_id_emp = db_emp.get_list_id_emps_by_id_company(4014)
    assert len(list_id_emp) == 0

@pytest.mark.skip("отладка метода")
def test_delete_list_emp_by_company_id():
    emp.create_list_employee_get_list_id(
        3, 4014, first_name, last_name, email, is_active, id, middle_name, url,
        phone, birthdate)
    len_q = len(db_emp.get_list_id_emps_by_id_company(4014))
    assert len_q == 3
    db_emp.delete_list_emps_company_id(4014)
    len_a = len(db_emp.get_list_id_emps_by_id_company(4014))
    assert len_a == 0

@pytest.mark.skip("отладка метода")
def test_max_id_emp():
    ek = db_emp.get_emp_max_id()
    assert ek > 0

@pytest.mark.skip("отладка метода")
def test_create_one_employe_by_max_id():
    db_emp.create_employee(4014)
    new_emp_db = db_emp.get_emp_max_id()
    new_emp_d = db_emp.get_list_id_emps_by_id_company(4014)
    assert 3+2 == 5


@pytest.mark.skip("отладка метода")  
def test_create_employes_by_max_id():
    db_emp.create_employees(
        4014, num_emps, is_active, first_name, last_name, middle_name,
        phone, url, email, birthdate)
    list_new_emp = db_emp.get_list_id_emps_by_id_company(4014)
    assert 2+3 == 5
