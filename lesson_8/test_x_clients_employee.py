import pytest

from EmployeeApi import EmployeeApi
from CompanyApi import CompanyApi

base_url = 'https://x-clients-be.onrender.com'

emp = EmployeeApi(base_url)
com = CompanyApi(base_url)


def test_get_list_employee():
    first_name = 'Arkasha'
    last_name = 'Smook'
    email = 'ghr@ghf.ty'
    is_active = True

    new_company = com.create_company('Company for getting list of empoyees 8')
    company_id = new_company["id"]

    for i in range(3):
        emp.create_employee(
            company_id, first_name, last_name, email, is_active)

    result = emp.get_list_employee(params_to_add={'company': company_id})

    assert len(result) == 3


def test_create_employee():
    new_company = com.create_company('Company for new employee8')
    company_id = new_company["id"]

    emp_list_f = emp.get_list_employee(params_to_add={'company': company_id})
    len_before = len(emp_list_f)
    assert len(emp_list_f) == 0

    new_emp = emp.create_employee(
        company_id, 'Mark8', 'Mgy', 'ghhg@fhg.ty', True)
    id_new_emp = new_emp['id']
    emp_list_a = emp.get_list_employee(params_to_add={'company': company_id})
    len_after = len(emp_list_a)
    assert len_after - len_before == 1

    emp_list = emp.get_list_employee(params_to_add={'company': company_id})
    emp_list_id = emp_list[-1]['id']
    assert id_new_emp == emp_list_id


def test_get_employee_by_id():
    first_name = 'Markusha'
    last_name = 'Moonlake'
    email = 'ghhg@fhg.ty'
    is_active = True
    new_company = com.create_company('Company for id employee8')
    company_id = new_company["id"]

    new_emp = emp.create_employee(company_id,
                                  first_name, last_name, email, is_active)
    emp_id = new_emp['id']

    get_new_emp = emp.get_employee_by_id(emp_id)
    get_new_emp_id = get_new_emp['id']

    list_emps = emp.get_list_employee(params_to_add={'company': company_id})
    emp_list_id = list_emps[-1]['id']

    assert get_new_emp_id == emp_list_id
    assert list_emps[-1]['firstName'] == first_name
    assert list_emps[-1]['lastName'] == last_name
    with pytest.raises(AssertionError):
        assert list_emps[-1]['email'] == email
    # ОР строка равна строке. ошибка. ФР поле не принимает эмайл ghhg@fhg.ty
    assert list_emps[-1]['isActive'] == is_active


def test_patch_employee():
    first_name = 'Aaron'
    last_name = 'VPR'
    email = 'aaron980@yht.com'
    isActive = True
    new_last_name = 'Changed2'
    new_email = 'string34@gh.ru'
    new_url = 'https://sky.pro/wiki/python'
    new_phone = '89018765523'
    new_isActive = False

    new_company = com.create_company(
        'Company for changing employee', 'check all keys and values')
    new_company_id = new_company['id']

    new_employee = emp.create_employee(
        new_company_id, first_name, last_name, email, isActive)
    new_employee_id = new_employee['id']

    result = emp.change_info_employee(
        new_employee_id, new_last_name, new_email, new_url, new_phone,
        new_isActive)
    # проверить ключи ответа - ФР: нет ключей прописанных в свагере
    # ОР: все ключи есть в json
    assert result.get('id') == new_employee_id
    with pytest.raises(AssertionError):
        assert result.get('firstName') is not None
    with pytest.raises(AssertionError):
        assert result.get('lastName') == new_last_name
    with pytest.raises(AssertionError):
        assert result.get('middleName') is not None
    with pytest.raises(AssertionError):
        assert result.get('companyId') is not None
    assert result.get('email') == new_email
    assert result.get('url') == new_url
    with pytest.raises(AssertionError):
        assert result.get('phone') == new_phone
    # ФР: не поменялся номер телефона ОР: поменялся номер телефона
    with pytest.raises(AssertionError):
        assert result.get('birthdate') is not None
    assert result.get('isActive') == new_isActive

    # проверка значений измененных ключей
    result_get_id = emp.get_employee_by_id(new_employee_id)
    assert result_get_id['lastName'] == new_last_name
    assert result_get_id['email'] == new_email
    assert result_get_id['avatar_url'] == new_url
    with pytest.raises(AssertionError):
        assert result_get_id['phone'] == new_phone
    assert result_get_id['isActive'] == new_isActive
