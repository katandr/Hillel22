import json
import csv


class Employee:
    '''
    employee description class
    '''

    def __init__(self, firstname='Ivasik',
                 lastname='Telesik',
                 age=13,
                 email='vasik-telesik1732@izkurnanog.ua',
                 skills=['ходить', 'говорить', "кодить"],
                 people_lang=['Україньська', "Англійська"],
                 coding_lang=['Python', "C++", "lisp"]):
        """Инициализация employee с значением по умолчанию"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.age = age
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def get_data(self):
        """printing data abount employee"""
        print(f'{self.firstname}  {self.lastname}  {self.age}')
        print(f'skills: {self.skills} languages: {self.people_lang} coding: {self.coding_lang}')

    def skills_count(self):
        """counf of the number of the skills for the specific employee"""
        print (f'{self.firstname} has {len(self.skills)} skills')

    def speak_language(self,ask_language):
        """check of the language is spoken by employee"""
        if ask_language in self.people_lang:
            return True
        else:
            return False

    def save_person_to_jason(self,file='people.json'):
        """save person into to jason file, append of it is already created"""
        with open(file,'a',encoding='utf-8') as file:
            to_json_string={'first_name': self.firstname,
                            'last_name': self.lastname,
                            'email': self.email,
                            'age': self.age,
                            'skills': self.skills,
                            'people_lang': self.people_lang,
                            'coding_lang': self.coding_lang}
            json.dump(to_json_string, file, indent=2,ensure_ascii=False)

    def save_header_csvfile(self, file='people.csv'):
        """part of the save to csv process. Save headers to the file. Should be run onece per file"""
        header = ['first name', 'last name', 'email', 'age', 'skills', 'people_languages', 'coding languages']
        with open(file, 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)

    def save_person_to_csv(self,file='people.csv'):
        """save person info to csv file"""
        to_csv = [self.firstname,self.lastname,self.email, self.age,self.skills, self.people_lang,self.coding_lang]
        with open(file, 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(to_csv)

    def new_employee_from_file_json(file):
        """create object based on json file"""
        with open(file,'r') as file:
            file_contents = file.read()
            parsed_json = json.loads(file_contents)

        new_employee=Employee()
        print(type(parsed_json))

    def add_employee_from_json(self,file):
        """method to create employee from json file"""
        with open(file,"r") as file:
            data = json.load(file)

        if type(data) is dict:
            keys=tuple(data.keys())
            print(keys)
            print(type(keys))
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

default_employee={
    'firstname': 'Ivasik',
    'lastname': 'Telesik',
    'age': 13,
    'e-mail': 'ivasik-telesik1732@izkurnanog.ua',
    'skills': ['ходить', "говорить", "кодить"],
    'people_lang': ['Україньська', "Англійська"],
    'coding_lang': ['Python', "C++", "lisp"],
}


person1 = Employee('Ivasik','Telesik')
person1.get_data()
person1.skills_count()
person1.save_person_to_jason()
person1.save_header_csvfile()
person1.save_person_to_csv()

person2 = Employee('Marusya','Krasa', 56,'none',['шить','вышивать'],['Україньська'],['basic'])
person2.get_data()
ask_language = 'Україньська'

if person2.speak_language(ask_language):
    print(f'{person2.firstname} speaks {ask_language}')


file = 'people.json'
new_person = Employee()
new_person.add_employee_from_json(file)
print("imported from file person",new_person.firstname)
