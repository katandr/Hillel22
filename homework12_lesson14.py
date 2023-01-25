import os

class MyDirectory:
    """
    Инициализация класса с одним параметром - имя директории.
    """

    def __init__(self, dirname):
        """
        Инициализация класса с одним параметром - имя директории
        :param dirname:
        """
        self.dirname = dirname
        if os.path.isdir(dirname):
            print("directory exist")
        else:
            os.makedirs(dirname, exist_ok=True)
            print("new directory was created")
        print(f'working directory {self.dirname}')

    def create_dictionary(self,dir_path : str):
        """
        Написать метод класса, который создает атрибут класса в ввиде словаря
{'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
{'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
        :return:
        """

        if os.path.isdir(dir_path):  # only  if the  specific folder exists
            # get all files inside a specific folder
            list_of_files = []
            for path in os.scandir(dir_path):
                if path.is_file():
                    list_of_files.append(path.name)
            list_of_folders = []
            for i in os.listdir(dir_path):
                if os.path.isdir(i):
                    list_of_folders.append(i)

            self.directory_dict={
                'filenames' : list_of_files,
                'dirnames' : list_of_folders,
            }
        else:
            print("wrong directory name")

        return self.directory_dict

    def sort_dict(self,dictionary: dict,sort: bool):
        sort = not sort
        files_sorted = sorted(dictionary['filenames'],reverse=sort)
        folders_sorted = sorted(dictionary['dirnames'])
        # print(f'sorted list of files {files_sorted}')
        # print(f'sorted list of directories {folders_sorted}')
        self.directory_dict_sorted = {
            'filenames': files_sorted,
            'dirnames': folders_sorted,
        }
        return self.directory_dict_sorted

    def check_file_or_folder_and_add(self, name: str, current_dictionary: dict):
        list_of_files = current_dictionary['filenames']
        list_of_folders = current_dictionary['dirnames']
        if '.' in name:
            list_of_files.append(name)
        else:
            list_of_folders.append(name)

        self.directory_dict_extend = {
            'filenames': list_of_files,
            'dirnames': list_of_folders,
        }
        return self.directory_dict_extend





path = os.path.dirname(os.path.abspath(__file__))
working_dir = MyDirectory(path)

dic_files_catalogs = working_dir.create_dictionary(working_dir.dirname)

print(f'not sorted \n {dic_files_catalogs} \n')
sorted_dic_files_directories = working_dir.sort_dict(dic_files_catalogs, False)
print(f'sorted dictionary \n {sorted_dic_files_directories}')

name='aaaaaaaaaaaaa.txt'
extended_dictionary=working_dir.check_file_or_folder_and_add(name,dic_files_catalogs)
print(f'extended dictionary \n {extended_dictionary}')




