import random
import string
import os


class Generator:

    def __init__(self, num=1000000):
        self._num = num
        self.path = os.path.join(os.getcwd(),'Test',"strings.txt")

    def generateFile(self):
        # откроем файл на запись
        self._f = open(self.path, 'w')
        for i in range(self._num):
            if i < (self._num - 1):
                string = self.name() + self.colon() + self.generateListName() + '\n'
            else:
                string = self.name() + self.colon() + self.generateListName()
            self._f.write(string)
        self._f.close()

    def choices(self, pattern, length=10):
        string = ''
        for i in range(length):
            string = string + random.choice(pattern)
        return string

    def generateListName(self):
        list_name = ''
        cycle_rand = random.randint(1, 4)
        for i in range(cycle_rand):
            length = random.randint(1, 20)
            rand = random.random()
            if rand < 0.33:
                list_name = list_name + self.space() + self.choices(string.ascii_letters + string.digits + '._', length)
            elif rand < 0.66:
                list_name = list_name + self.space() + self.choices(string.ascii_letters + '._', length)
            else:
                list_name = list_name + self.space() + self.choices(string.digits, length)
        return list_name

    def name(self):
        length = random.randint(1, 30)
        target_name = self.choices(string.ascii_letters + string.digits + '._', length)
        return target_name

    def colon(self):
        if random.random() > 0.5:
            return ':'
        else:
            return ''

    def space(self):
        if random.random() > 0.5:
            return ' '
        else:
            return ''

    def getFileContent(self):
        list = self._f.read().split('\n')
        self._num = len(list)
        return list


if __name__ == '__main__':
    gen = Generator()
    gen.generateFile()
