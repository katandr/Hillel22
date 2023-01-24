import json
import csv

class Employee:
    '''
       employee description class
    '''

    def __init__(self):
        self.firstname = 'firstname'
        self.lastname = 'lastname'
        self.email = 'email'
        self.age = 0
        self.skills = []
        self.people_lang = []
        self.coding_lang = []

    def add_employee_from_json(self, file):
        """method to create employee from json file"""
        with open(file, "r") as file:
            data = json.load(file)

        if type(data) is dict:
            keys = tuple(data.keys())
            if keys != ('first_name', 'last_name', 'email', 'age', 'skills', 'people_lang', 'coding_lang'):
                print("error with incoming data format")
            else:
                self.firstname = data['first_name']
                self.lastname = data['last_name']
                self.email = data['email']
                self.age = data['age']
                self.skills = data['skills']
                self.people_lang = data['people_lang']
                self.coding_lang = data['coding_lang']

class Employer:
    '''class for employer'''
    def __init__(self,name='Roga i kopita', address='some address'):
        ''' definition for init method or constructor with default argument'''
        self.name = name
        self.address = address
        self.employees = []

    def add_employee(self,name):
        person1 = Employee()
        file = 'people.json'
        new_person = Employee()
        new_person.add_employee_from_json(file)
        print("imported from file person", new_person.firstname)

    def add_employee_to_employer(self,employee):
        employees_list = self.employees
        print(employees_list)
        print(employee)
        updated_list = employees_list.append(employee)

        self.employees = updated_list



person2=Employee()

file = 'people.json'
person3 = Employee()
person3.add_employee_from_json(file)

print("imported from file person",person3.firstname)

employer1=Employer()
print("added employer",employer1.name)

# adding employee to employer
employer1.add_employee_to_employer(person3)

print(employer1.employees)
