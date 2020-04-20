from PLY.lexerClass import MyLexer
import PLY.yacc as yacc
import string

class MyParser(object):
    tokens = MyLexer.tokens
    a = dict()
    count = 0

    def get_dict(self):
        return self.a

    def __init__(self, file = None):
        self._f = file
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        #self.parser = yacc.yacc(module=self)

    def check_string(self, code):
        self.a.clear()
        result = self.parser.parse(code)
        return result

    def p_targetname(self, p):
        """targetname : TARGETNAME COLON targetname_list NL"""
        status = self.GetStatus(p[1], p[3].split(' '))
        if status == 1:
            # Добавим (если нет) targetname в список
            if self.a.get(p[1].strip()) is None:
                self.a.setdefault(p[1].strip(), 1)
            else:
                self.a[p[1].strip()] += 1
            if self._f is not None:
                self._f.write(p.lexer.lexdata.strip() + ' - yes\n')
            self.count += 1
        else:
            self.a.clear()
            if self._f is not None:
                self._f.write(p.lexer.lexdata.strip() + ' - no\n')

    def p_targetname_error(self, p):
        """targetname : err_str"""
        self.a.clear()

    def p_targetname_list(self, p):
        """targetname_list : TNINLIST
                           | targetname_list TNINLIST"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[2]
        if len(p) == 3:
            i = 2
        else:
            i = 1
        if (p[i] is not None) and (len(p[i].strip()) > 0):
            if self.a.get(p[i].strip()) is None:
                self.a.setdefault(p[i].strip(),1)
            else:
                self.a[p[i].strip()] += 1

    def p_err_str(self, p):
        """err_str : NL
                   | err_list NL
                   | TARGETNAME err_list NL
                   | TARGETNAME COLON err_list NL
                   | TARGETNAME COLON TNINLIST err_list NL"""
        self.a.clear()
        if self._f is not None:
            '''if (len(p) > 1) and (p[1] is not None) and (len(p[1].strip()) > 0):
                p[0] = p[1]
            if (len(p) > 2) and (p[2] is not None) and (len(p[2].strip()) > 0):
                if p[0] is None:
                    p[0] = p[2]
                else:
                    p[0] += p[2]
            if (len(p) > 3) and (p[3] is not None) and (len(p[3].strip()) > 0):
                if p[0] is None:
                    p[0] = p[3]
                else:
                    p[0] += p[3]
            if p[0] is not None:'''
            self._f.write(p.lexer.lexdata.strip() + ' - no\n')

    def p_err_list(self, p):
        """err_list : 
                    | err
                    | err_list err"""
        if len(p) > 1:
            if len(p) == 2:
                p[0] = p[1]
            else:
                p[0] = p[1] + p[2]

    def p_err(self, p):
        """err : ERR"""
        p[0] = p[1]

    def p_error(self, p):
        s_err = True
        #print('Unexpected token', p)

    def GetStatus(self, target_name, list):
        status = 1;  # признак корректной строки
        for i in range(len(list)):
            if len(list[i]) > 0:
                if list[i] == target_name:
                    status = 0
                    break
        if status == 1:
            # Если строка корректна после первой проверки, то проверим - нет ли повторяющихся слов в списке имён целей
            i = 0;
            while i < (len(list) - 1):
                if len(list[i]) > 0:
                    j = i + 1
                    while j < len(list):
                        if len(list[j]) > 0:
                            if list[i] == list[j]:
                                status = 0
                                break
                        j = j + 1
                i = i + 1
        return status



