import json



class CountryData:
    """
    Класс позволяющий читать файлы и доставать данные с помощью гет-методов
    """
    def __init__(self, filename):
        """
        Инициализационный метод, который читает файл и достает из него данные
        :param filename: путь к файлу
        """
        self.__filename = filename
        self.__data = self.read_data()
        self.__var = 50
        # self.country = self.data['country']
        # self.city = self.data['city']

    def __str__(self):
        return f"File {self.__filename} with data: {self.__data}"

    def __repr__(self):
        return f"File {self.__filename} with data: {self.__data}"

    @property
    def data(self):
        return self.__data

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, number):
        self.__var = number

    def read_data(self):
        """
        Метод преобразующий данный из файла в словарь
        :return: Словарь
        """
        with open(self.__filename) as f:
            data = f.read()
            data = json.loads(data)
            return data

    def get_country(self, _id):
        """
         Гетер достающий страну
        :param _id:  ID нужной записи из файла
        :return: Страна
        """""
        country = self.__data[str(_id)]['country']
        return country

    def get_city(self, _id):
        city = self.__data[str(_id)]['city']
        return city

class CountryDataWithTemp(CountryData):
    def __init__(self, filename):
        super().__init__(filename)

    def get_temp(self, _id):
        temp = self.data[str(_id)]['temp']
        return temp

data1 = CountryData('ola.txt')

# print(data1.data)

print(data1.get_country("3"))
print(data1.get_city("4"))

data2 = CountryDataWithTemp('ola_new_format')
print(data2.get_temp(1))
print(data2.data)
print(data2.var)
data2.var = 100
print(data2.var)

print(data1)