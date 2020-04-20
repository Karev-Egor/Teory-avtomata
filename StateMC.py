from SMC import version2_sm
import string
import generator
import time
import os


class Version2:

    def __init__(self):
        self._fsm = version2_sm.AppClass_sm(self)
        self._is_acceptable = True
        self._counter = 0
        self._name = ''
        self._fsm.enterStartState()
        self._result = {}
        self.targetname = ''
        self.list = {}

    # Uncomment to see debug output.
    # self._fsm.setDebugFlag(True)

    def counterInc(self):
        self._counter += 1

    def AddToName(self, letter):
        self._name += letter

    def GetNonFirstSymbol(self):
        return self._counter > 0

    def SetTargetName(self):
        self.targetname = self._name;
        self._name = '';
        self._counter = 0;

    def Zero(self):
        return self._counter == 0

    def NonZero(self):
        return self._counter > 0

    def AddToDict(self, key):
        num = self._result.get(key)
        if num is None:
            self._result[key] = 1
        else:
            self._result[key] = num + 1

    def AddToTNList(self):
        self.list[len(self.list)] = self._name
#        num = self.list.get(self._name)
#        if num is None:
#            self.list[self._name] = 1
#        else:
#            self.list[self._name] = num + 1
        self._name = '';
        self._counter = 0;

    def Clear(self):
        self._is_acceptable = True
        self._counter = 0
        self._name = ''
        self.targetname = ''
        self.list = {}

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

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

    def check_string(self, str):
        self._fsm.TargetName_1()
        for c in str:
            if not self._is_acceptable:
                break
            if c in string.ascii_letters:
                self._fsm.Letter(c)
            elif c in string.digits:
                self._fsm.Digit(c)
            elif c == ':':
                self._fsm.Colom()
            elif c == '.':
                self._fsm.Dot(c)
            elif c == '_':
                self._fsm.UnderLine(c)
            elif c == ' ':
                self._fsm.Space()
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        if self._is_acceptable:
            # Проверим - нет ли в списке имён целей имени самой цели
            status = self.GetStatus(self.targetname, self.list)
            if status == 1:
                self.AddToDict(self.targetname);
                for i in range(len(self.list)):
                    self.AddToDict(self.list[i]);
            else:
                self._is_acceptable = False
        return self._is_acceptable, self.list


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
        check = Version2()
        check._f = open(os.path.join(os.getcwd(), 'SMCTask', "result_SMC.txt"), 'w')
        print('Reading from file...')
        gen = generator.Generator()
        gen._f = open(gen.path, 'r')
        list = gen.getFileContent()
        correct_cnt = 0
        n1 = time.perf_counter()
        correct_cnt = 0
        for i in range(len(list)):
            t = check.check_string(list[i])
            if t[0]:
                check._f.write(list[i] + ' - yes' + '\n')
                correct_cnt += 1
            else:
                check._f.write(list[i] + ' - no' + '\n')
        n2 = time.perf_counter()
        check.saveRes()
        check._f.close()
        print(n2 - n1, 'correct string count = "' + str(correct_cnt) + '"')
    if n == 2:
        _str = ''
        check = Version2()
        correct_cnt = 0;
        while True:
            print('Enter the string. To exit, enter "end"')
            _str = input()
            if _str != 'end':
                t = check.check_string(_str)
                if t[0]:
                    print('Good string')
                    correct_cnt += 1
                else:
                    print('Bad string')
            else:
                break
        if correct_cnt > 0:
            check.printDict()
    print('Bye')