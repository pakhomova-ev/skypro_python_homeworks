import requests


class EmployeeApi:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    def create_employee(
            self, company_id, first_name, last_name, email, isActive, id=1,
            middle_name='', url='', phone='',
            birthdate='2005-05-03T11:19:37.153Z'):
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName':  last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/employee', headers=my_headers, json=creds)
        return resp.json()

    def create_list_employee_get_list_id(
            self, num_emp, company_id, first_name, last_name, email, isActive, id=1,
            middle_name='', url='', phone='',
            birthdate='2005-05-03T11:19:37.153Z'):
        list_new_emp = []
        list_new_emp_id = []
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName':  last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        for i in range(num_emp):
            resp = requests.post(
                self.url + '/employee', headers=my_headers, json=creds)
            resp_json = resp.json()
            list_new_emp.append(resp_json)

        for i in range(len(list_new_emp)):
            emp_full = list_new_emp[i]["id"]
            list_new_emp_id.append(emp_full)

        return list_new_emp_id

    def create_employee_without_auth_token(
            self, company_id, first_name, last_name, email, isActive, id=1,
            middle_name='', url='', phone='',
            birthdate='2005-05-03T11:19:37.153Z'):
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName':  last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        resp = requests.post(
            self.url + '/employee', json=creds)
        return resp.json()

    def create_employee_without_body(self):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/employee', headers=my_headers)
        return resp.json()

    def get_list_employee(self, params_to_add):
        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()

    def get_employee_by_id(self, emp_id):
        resp = requests.get(self.url + '/employee/' + str(emp_id))
        return resp.json()

    def get_employee_by_id_without_id(self):
        resp = requests.get(self.url + '/employee/')
        return resp.json()

    def change_info_employee(
            self, emp_id, last_name, email, url, phone, is_active):
        cred = {
            'lastName': last_name,
            'email': email,
            'url': url,
            'phone': phone,
            'isActive': is_active
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id), headers=my_headers,
            json=cred)
        return resp.json()

    def change_info_employee_without_auth_token(
            self, emp_id, last_name, email, url, phone, is_active):
        cred = {
            'lastName': last_name,
            'email': email,
            'url': url,
            'phone': phone,
            'isActive': is_active
        }

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id),
            json=cred)
        return resp.json()

    def change_info_employee_without_id(
            self, last_name, email, url, phone, is_active):
        cred = {
            'lastName': last_name,
            'email': email,
            'url': url,
            'phone': phone,
            'isActive': is_active
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/', headers=my_headers,
            json=cred)
        return resp.json()

    def change_info_employee_without_body(
            self, emp_id, last_name, email, url, phone, is_active):

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id), headers=my_headers)
        return resp.json()
