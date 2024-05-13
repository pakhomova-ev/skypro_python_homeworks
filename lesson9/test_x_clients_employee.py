import pytest
from faker import Faker
import allure

from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable
from CompanyTable import CompanyTable


base_url = 'https://x-clients-be.onrender.com'
db_url = 'postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet'

db_emp = EmployeeTable(db_url)
db_com = CompanyTable(db_url)
emp = EmployeeApi(base_url)
fake = Faker("ru_RU")

api_creds_emp = {
    'lastName': fake.last_name(),
    'email': fake.email(),
    'url': fake.url(),
    'phone': fake.random_number(digits=11, fix_len=True),
    'isActive': False
    }

dict_creds_emp = {
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
    'email': fake.email(),
    'middle_name': fake.first_name_male(),
    'is_active': True,
    'id': 1,
    'phone': fake.random_number(digits=11, fix_len=True),
    'birthdate': '2005-04-26',
    'url': fake.url()
    }
is_active = True

num_emps = 3  # кол-во сотрудников (пока одинаковых) создаваемых авто


@allure.epic("hw9")
@allure.feature("сотрудник компании")
class TestEmployee:

    @allure.story("получить сотрудника/список сотрудников")
    def test_get_list_employees():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # проверить что у компании нет сотрудников бд
        list_emp_db = db_emp.get_list_emps_by_id_company(company_id)
        assert len(list_emp_db) == 0

        # создать нескольких сотрудников
        for i in range(num_emps):
            db_emp.create_employee(
                company_id, is_active, dict_creds_emp)

        # проверить что создали верное кол-во сотрудников
        assert len(db_emp.get_list_id_emps_by_id_company(company_id)) == num_emps

        result_api = emp.get_list_employee(params_to_add={'company': company_id})
        result_db = db_emp.get_list_emps_by_id_company(company_id)
        assert len(result_api) == len(result_db)

        # сравнить значения ключа id сотрудников,
        # полученных по апи и через запрос к бд
        # считаем, что списки отсортированы по
        # возрастанию по id сотрудника
        for i in range(num_emps):
            assert result_api[i]["id"] == result_db[i]["id"]

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    # как сравнить значение ключей через апи и из бд?
    @allure.story("получить сотрудника/список сотрудников")
    def test_get_employee_by_id():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # получить сотрудника по id
        get_new_emp = emp.get_employee_by_id(id_new_emp)

        # проверка значений ключей ответа
        assert get_new_emp["id"] == id_new_emp
        assert get_new_emp["firstName"] == list_id_new_emp[0][4]
        assert get_new_emp["lastName"] == list_id_new_emp[0][5]
        # assert get_new_emp["email"] == list_id_new_emp[0][8]
        # ФР:возвращается null
        # ОР: возвращается значение email
        assert get_new_emp["isActive"] == list_id_new_emp[0][1]

        assert get_new_emp["middleName"] == list_id_new_emp[0][6]
        # ФР:ключ avatar_url ОР: ключ url (сваггер)
        assert get_new_emp["avatar_url"] == list_id_new_emp[0][10]
        assert get_new_emp["phone"] == list_id_new_emp[0][7]
        assert get_new_emp["birthdate"] == '2005-04-26'

        # проверка что сотрудник есть в списке сотрудников компании
        list_emps = db_emp.get_list_emps_by_id_company(company_id)
        emp_list_id = list_emps[-1][0]
        assert emp_list_id == get_new_emp["id"]

        # удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.получить сотрудника/список сотрудников")
    def test_get_employee_by_id_without_id():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(
            company_id, is_active, dict_creds_emp)

        # получить сотрудника по id
        get_new_emp = emp.get_employee_by_id_without_id()
        assert get_new_emp["statusCode"] == 500
        assert get_new_emp["message"] == 'Internal server error'
        # необходимо прописать более информационный статус код и сообщение.
        # возможно 400 - плохой запрос

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.получить сотрудника/список сотрудников")
    @pytest.mark.xfail(reason="ФР:тело ответа пустое, ОР: 404 сотрудник не найден")
    def test_get_employee_by_wrong_id():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_emp = db_emp.create_employee(
            company_id, is_active, dict_creds_emp)
        id_new_emp = new_emp[0][0]
        # пока вместо проверки схемы
        assert len(new_emp) == 1

        wrong_emp_id = id_new_emp + 1000

        # получить сотрудника по id
        get_new_emp = emp.get_employee_by_id(wrong_emp_id)
        assert len(get_new_emp) == 0  # что приходит в ответе?

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.получить сотрудника/список сотрудников")
    @pytest.mark.xfail(reason="company_id is required")
    def test_get_list_employee_without_company_id():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        result = db_emp.get_list_emps_by_id_company()
        assert len(result) == 1

        # удалить компанию
        db_com.delete_company(company_id)

    # дописать проверку значений полей у сотрудника чарез бд
    @allure.story("создание сотрудника/сотрудников")
    def test_create_employee():
        # создать новую компанию
        db_com.create('Company Empoyees 8')
        company_id = db_com.get_max_id()

        # проверить, что у созданной компании нет работников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)
        assert len_before == 0

        # создать нового работника
        new_emp = db_emp.create_employee(company_id, is_active, dict_creds_emp)
        id_new_emp = new_emp['id']
        assert len(new_emp) == 1

        # проверка, что создан 1 работник
        emp_list = db_emp.get_list_emps_by_id_company(company_id)
        id_emp_create = emp_list[-1]['id']
        len_after = len(emp_list)
        assert len_after - len_before == 1

        # проверка созданного работника
        result_api = emp.get_employee_by_id(id_new_emp)

        # проверка заполненных
        assert result_api["id"] == id_new_emp
        assert result_api["firstName"] == dict_creds_emp["first_name"]
        assert result_api["lastName"] == dict_creds_emp["last_name"]
        assert result_api["isActive"] is True

        # - не сохраняется значение
        # assert result_api ["email"] == dict_creds_emp["email"]
        assert result_api["middleName"] == dict_creds_emp["middle_name"]
        assert result_api["avatar_url"] == dict_creds_emp["url"]
        assert result_api["phone"] == dict_creds_emp["phone"]
        assert result_api["birthdate"] == dict_creds_emp["birthdate"]

        # проверить, что последний id сотрудника равен созданному сотруднику
        assert id_new_emp == id_emp_create

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.создание сотрудника/сотрудников")
    def test_create_employee_without_auth_token():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # проверить что у созданной компании нет сотрудника
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)
        assert len(emp_list_f) == 0

        # создать нового сотрудника
        new_emp = emp.create_employee_without_auth_token(
            company_id, dict_creds_emp)

        assert new_emp["statusCode"] == 401
        assert new_emp["message"] == 'Unauthorized'

        # проверка, что не создан сотрудник
        emp_list_a = db_emp.get_list_emps_by_id_company(company_id)
        len_after = len(emp_list_a)
        assert len_after - len_before == 0

        # удаление компании
        db_com.delete_company(company_id)

    @allure.story("negative.создание сотрудника/сотрудников")
    def test_create_employee_without_body():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # проверка что у созданной компании нет сотрудников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        assert len(emp_list_f) == 0

        # создать нового сотрудника
        new_emp = emp.create_employee_without_body()
        assert new_emp["statusCode"] == 500
        assert new_emp["message"] == 'Internal server error'
        # необходимо прописать более информационный статус код и сообщение.
        # возможно 400 - плохой запрос

        # удаление компании
        db_com.delete_soft(company_id)

    @allure.story("редактировать сотрудника/сотрудников")
    def test_patch_employee():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_emp = db_emp.create_employee(company_id, is_active, dict_creds_emp)
        id_new_emp = new_emp['id']

        result_db = db_emp.patch_employee(
            id_new_emp, is_active, dict_creds_emp)
        # assert len(result) == 7 # пока вместо проверки схемы ответа
        # проверить ключи ответа - ФР: нет ключей прописанных в свагере
        # ОР: все ключи есть в json
        assert result_db.get('id') == id_new_emp
        result_api = emp.get_employee_by_id(id_new_emp)

        # assert result.get('lastName') == new_emp['lastName']
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение (новое)
        assert result_db.get('isActive') == result_api['is_active']
        assert result_db.get('email') == result_api['email']
        # assert result_db.get('phone') == result_api['phone']
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение (новое)
        assert result_db.get('url') == result_api['url']

        # assert result_db.get('firstName') == result_api['firstName']
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение
        assert result_db.get('middleName') == result_api.get['middleName']
        assert result_db.get('companyId') == result_api.get['companyId']
        assert result_db.get('birthdate') == result_api.get['birthdate']

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_without_auth_token():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_emp = db_emp.create_employee(company_id, is_active, dict_creds_emp)
        id_new_emp = new_emp['id']

        result = emp.change_info_employee_without_auth_token(
            id_new_emp, api_creds_emp)

        assert result["statusCode"] == 401
        assert result["message"] == 'Unauthorized'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_without_id():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)

        result = emp.change_info_employee_without_id(api_creds_emp)

        assert result["statusCode"] == 404
        assert result["error"] == 'Not Found'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="без тела возвращается информация по пользователю")
    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_without_body():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_emp = db_emp.create_employee(company_id, is_active, dict_creds_emp)
        id_new_emp = new_emp['id']

        result = emp.change_info_employee_without_body(
            id_new_emp)

        assert result["statusCode"] == 404
        assert result["error"] == 'Not Found'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="ФР: 500, ОР: 404")
    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_wrong_id():
        # создать новую компанию
        db_com.create("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_emp = db_emp.create_employee(company_id, is_active, dict_creds_emp)
        id_new_emp = new_emp['id']

        wrong_emp_id = id_new_emp + 1000

        result = db_emp.patch_employee(wrong_emp_id, is_active)

        assert result["statusCode"] == 404
        assert result["message"] == 'Not Found'

        # удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_soft(company_id)

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

    # @pytest.mark.skip("отладка метода")
    def test_max_id_emp():
        ek = db_emp.get_emp_max_id()
        ek = ek + 1
        assert ek > 0

    @pytest.mark.skip("отладка метода")
    def test_create_one_employe_by_max_id():
        db_emp.create_employee(4014)
        new_emp_db = db_emp.get_emp_max_id()
        new_emp_d = db_emp.get_list_id_emps_by_id_company(4014)
        f = 5


    @pytest.mark.skip("отладка метода")  
    def test_create_employes_by_max_id():
        db_emp.create_employees(
            4014, num_emps, is_active, first_name, last_name, middle_name,
            phone, url, email, )
        list_new_emp = db_emp.get_list_id_emps_by_id_company(4014)
        f = 5

    @pytest.mark.skip("отладка метода")
    def test_create_employes_by_max_id_mult():
        db_emp.create_employees_mult(
            4014, num_emps, is_active)
        list_new_emp = db_emp.get_list_id_emps_by_id_company(4014)
        assert 2+3 == 5

    @pytest.mark.skip("отладка метода")
    def test_gen():
        list = db_emp.generate_all_fields_emp(3, True, 110)
        assert 2+3==5