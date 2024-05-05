[{'id': 6900}, {'id': 6901}, {'id': 6901}]

# будет проверка из базы данных
def test_create_list_emps():
    new_emps = emp.create_list_employee(
        5, 3916, first_name, last_name, email, is_active)

    assert new_emps[0] == 1

        # можно завернуть в метод
    # получаем 
    for i in range(len(new_emps_id)):
        emp_full = db_emp.get_emp_by_id(new_emps_id[i])
        list_emp_full_info.append(emp_full)