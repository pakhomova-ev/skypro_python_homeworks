from sqlalchemy import create_engine
from sqlalchemy.sql import text
from CompanyTable import CompanyTable
from faker import Faker

class EmployeeTable:
    __scripts = {
        "select by id": text("select * from employee where id =:id_to_select"),
        "select list emp by id company": text("select * from employee where company_id =:company_id order by id"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "get max id": "select MAX(id) from employee",
        "insert new": text("insert into employee(id, first_name, last_name, company_id, is_active, phone, email, middle_name, birthdate, avatar_url) values (:id, :first_name, :last_name, :company_id, :is_active, :phone, :email, :middle_name, :birthday, :url)")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_emp_by_id(self, emp_id):
        return self.__db.execute(
           self.__scripts["select by id"], id_to_select=emp_id).fetchall()
    
    def get_list_emps_by_id_company(self, com_id):
        return self.__db.execute(
            self.__scripts["select list emp by id company"], company_id=com_id).fetchall()
    
    def get_list_id_emps_by_id_company(self, com_id):
        list_id_emp = []

        id_emp = self.get_list_emps_by_id_company(com_id)
        for i in range(len(id_emp)):
            get_id_emp = id_emp[i][0]
            list_id_emp.append(get_id_emp)

        return list_id_emp
    
    def delete(self, emp_id):
        return self.__db.execute(self.__scripts["delete by id"], id_to_delete=emp_id)
    
    def delete_list_emps(self, list):
        for i in range(len(list)):
            self.__db.execute(self.__scripts["delete by id"], id_to_delete=list[i])

    def delete_list_emps_and_company_by_company_id(self, company_id):
        list_id_emp = self.get_list_id_emps_by_id_company(company_id)
        for i in range(len(list_id_emp)):
            self.__db.execute(self.__scripts["delete by id"], id_to_delete=list_id_emp[i])

    def get_emp_max_id(self):
        id_emp = self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]
        return id_emp
    
    def create_employee(self, com_id):
        max_id_b = self.get_emp_max_id()
        max_id = max_id_b + 1
        self.__db.execute(self.__scripts["insert new"], id=max_id, company_id=com_id)

    def create_employees(self, com_id, num_emp, is_active, first_name, last_name, middle_name, phone, url, email, birthday):
        for i in range(num_emp):
            max_id_b = self.get_emp_max_id()
            max_id = max_id_b + 1
            self.__db.execute(self.__scripts["insert new"], id=max_id, company_id=com_id, first_name=first_name, last_name=last_name, is_active=is_active, phone=phone, url=url, birthday=birthday, email=email, middle_name=middle_name)


    #  "insert new": text("insert into employee ("company_id","first_name",)")
    # не понятно как получать id так как он генерируется при добавлении в базу
    # а в запросе к бд нужен правильный id сотрудника как в апи не работает
    




    

