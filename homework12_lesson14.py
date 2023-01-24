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
                    print(path.name)
                    list_of_files.append(path.name)
            list_of_directories = []
            p = os.listdir(dir_path)
            for i in p:
                if os.path.isdir(i):
                    list_of_directories.append(i)


            self.directory_dict={
                'filenames' : list_of_files,
                'dirnames' : list_of_directories,
            }
        else:
            print("wrong directory name")

        print(self.directory_dict)
        return


path = os.path.dirname(os.path.abspath(__file__))
working_dir = MyDirectory(path)
working_dir.create_dictionary(working_dir.dirname)



