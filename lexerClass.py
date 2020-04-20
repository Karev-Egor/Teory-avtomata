import PLY.lex as lex

class MyLexer(object):
    states = (
        ('colon', 'exclusive'),
        ('tninlist', 'exclusive'),
        ('err', 'exclusive')
    )

    tokens = (
        'TARGETNAME', 'COLON', 'TNINLIST', 'ERR', 'NL'
    )

    def t_TARGETNAME(self, t):
        r'[a-zA-Z._][a-zA-Z0-9._]*'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('colon')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_ERR(self, t):
        r'.'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('err')
        return t

    def t_colon_COLON(self, t):
        r':'
        t.lexer.begin('tninlist')
        return t

    def t_colon_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_colon_ERR(self, t):
        r'.'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('err')
        return t

    def t_tninlist_TNINLIST(self, t):
        r'[ ]*[a-zA-Z._][a-zA-Z0-9._]*[ ]*'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('tninlist')
        return t

    def t_tninlist_NL(self, t):
        r'\n'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_tninlist_ERR(self, t):
        r'.'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('err')
        return t

    def t_err_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_err_ERR(self, t):
        r'.'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('err')
        return t

    def t_colon_error(self, t):
        print("Illegal character in COLON'%s'" % t.value[0])
        t.lexer.begin('err')

    def t_tninlist_error(self, t):
        print("Illegal character in TNINLIST'%s'" % t.value[0])
        t.lexer.begin('err')

    def t_err_error(self, t):
        print("Illegal character in ERR'%s'" % t.value[0])
        t.lexer.begin('err')

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('err')

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def __init__(self):
        self.lexer = lex.lex(module=self)
