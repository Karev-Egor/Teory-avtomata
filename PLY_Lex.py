import PLY.parserClass as parser
import string
import generator
import time
import os


class PLY():

    def __init__(self, file = None):
        self._f = file
        self.parser = parser.MyParser(self._f)
        self._result = {}

    def AddToDict(self, key):
        num = self._result.get(key)
        if num is None:
            self._result[key] = 1
        else:
            self._result[key] = num + 1

    def printDict(self):
        for key, item in self._result.items():
            print(key + ' - ' + str(item))

    def saveRes(self):
        for key, item in self._result.items():
            self._f.write(key + ' - ' + str(item) + '\n')

if __name__ == '__main__':
    print('What do you want:\n'
          '1. Read from file\n'
          '2. Read from console\n')
    n = int(input())
    if n == 1:
        check = PLY(open(os.path.join(os.getcwd(), 'PLYTask', 'result_PLY.txt'), 'w'))
        print('Reading from file...')
        gen = generator.Generator()
        gen._f = open(gen.path, 'r')
        list = gen.getFileContent()
        n1 = time.perf_counter()
        for i in range(len(list)):
            if list[i] != '':
                list[i] += '\n';
            check.parser.check_string(list[i])
            if check.parser.get_dict().keys():
                for res in check.parser.get_dict():
                    check.AddToDict(res)
        n2 = time.perf_counter()
        check.saveRes()
        check._f.close()
        print(n2 - n1, 'correct string count = "' + str(check.parser.count) + '"')
    if n == 2:
        _str = ''
        check = PLY()
        while True:
            print('Enter the string. To exit, enter "end"')
            _str = input()
            if _str != 'end':
                if _str != '':
                    _str += '\n';
                check.parser.check_string(_str)
                if check.parser.get_dict().keys():
                    print('Good string')
                    for res in check.parser.get_dict():
                        check.AddToDict(res)
#                if check.parser.get_dict().keys():
#                    print('Good string')
#                    for res in list(check.parser.get_dict().keys()):
#                        check.AddToDict(res)
                else:
                    print('Bad string')
            else:
                break
        print('Total: \n')
        check.printDict();
    print('Bye')