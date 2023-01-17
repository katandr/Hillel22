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

    def add_employee_from_json(self,file):
        """method to create employee from json file"""
        with open(file,"r") as file:
            data = json.load(file)
        if type(data) is dict:
            keys=data.keys()
            for key in keys:
                print(key)
                self.[key] = data.setdefault(key)






person1=Employee()
file = 'people.json'
new_person = Employee()
new_person.add_employee_from_json(file)
print("yyy",new_person.firstname)



