import re
import generator
import time
import os

class Recognizer:
    def __init__(self, strings):
        self.strings = strings
        self._result = {}

    def AddToDict(self, key):
        num = self._result.get(key)
        if num is None:
            self._result[key] = 1
        else:
            self._result[key] = num + 1

    def GetStatus(self, target_name, list):
        status = 1;  # признак корректной строки
        for i in range(len(list)):
            if list[i] == target_name:
                status = 0
                break
        if status == 1:
            # Если строка корректна после первой проверки, то проверим - нет ли повторяющихся слов в списке имён целей
            i = 0;
            while i < (len(list) - 1):
                j = i + 1
                while j < len(list):
                    if list[i] == list[j]:
                        status = 0
                        break
                    else:
                        j = j + 1
                i = i + 1
        return status

    def recognize(self):
        self._f = open(os.path.join(os.getcwd(), 'RegExp', "result.txt"), 'w')
        begtime = time.perf_counter()
        # проинициализируем счётчик правильных строк
        j = 0
        for i in range(len(self.strings)):
            # Получим 2 группы. Первая - имя цели, вторая - строка со списком имён целей
            match = re.fullmatch(r'([a-zA-Z._]?[a-zA-Z0-9._]+):([a-zA-Z0-9._ ]+)', self.strings[i])
            if match is not None:
                target_name = match.group(1)
                # Преобразуем строку со списком целей в список
                list = re.findall(r'([a-zA-Z._]?[a-zA-Z0-9._]+\s*)', match.group(2))
                if list is not None:
                    # Проверим - нет ли в списке имён целей имени самой цели
                    status = self.GetStatus(target_name, list)
                    if status == 1:
                        self.AddToDict(target_name);
                        for i in range(len(list)):
                            self.AddToDict(list[i]);
                        j += 1
                        self._f.write(self.strings[i] + ' - yes' + '\n')
                    else:
                        self._f.write(self.strings[i] + ' - no' + '\n')
                else:
                    self._f.write(self.strings[i] + ' - no' + '\n')
            else:
                self._f.write(self.strings[i] + ' - no' + '\n')
        endtime = time.perf_counter()
        self.printDict()
        self.saveRes()
        self.saveTime(endtime - begtime, j)
        self._result = {}
        print(endtime - begtime, j)
        self._f.close()

    def recognise(self, str):
        # Получим 2 группы. Первая - имя цели, вторая - строка со списком имён целей
        match = re.fullmatch(r'([a-zA-Z._]?[a-zA-Z0-9._]+):([a-zA-Z0-9._ ]+)', str)
        if match is not None:
            target_name = match.group(1)
            # Преобразуем строку со списком целей в список
            list = re.findall(r'([a-zA-Z._]?[a-zA-Z0-9._]+\s*)', match.group(2))
            if list is not None:
                # Проверим - нет ли в списке имён целей имени самой цели
                status = self.GetStatus(target_name, list)
                if status == 1:
                    self.AddToDict(target_name);
                    for i in range(len(list)):
                        self.AddToDict(list[i]);
                    print('Good string')
                else:
                    print('Bad string')
            else:
                print('Bad string')
        else:
            print('Bad string')

    def printDict(self):
        for key, item in self._result.items():
            print(key + ' - ' + str(item))

    def saveRes(self):
        for key, item in self._result.items():
            self._f.write(key + ' - ' + str(item) + '\n')

    def saveTime(self, time, number):
        f = open(os.path.join(os.getcwd(), 'RegExp', "time.txt"), 'w')
        f.write(str(time)+'\n')
        f.write(str(number))
        f.close()


if __name__ == '__main__':
    print('Please, choose where to read data from:\n'
          '1 - from file\n'
          '2 - from console\n')
    n = int(input())
    if n == 1:
        gen = generator.Generator()
        gen._f = open(gen.path, 'r')
        print('Reading from file...')
        addr = gen.getFileContent()
        print('...Reading from file is OK')
        rec = Recognizer(addr)
        rec.recognize()
    if n == 2:
        string = ''
        rec = Recognizer('')
        while True:
            print('Enter the string. To exit, enter "end"')
            string = input()
            if string != 'end':
                rec.recognise(str=string)
            else:
                break
        rec.printDict()
    print('Program ended.')

#if __name__ == '__main__':
#    print('Reading from file...')
#    gen = generator.Generator()
#    list = gen.getFileContent()
#    print('...Reading from file is OK')
#    rec = Recognizer(list)
#    rec.recognize()