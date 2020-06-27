RESERVED = 'RESERVED'
UNKNOWN = 'UNKNOWN'
NUMBER = 'NUMBER'
STRING = 'STRING'
QUOTE = 'QUOTE'
ID = 'ID'


class Token:
    """
    docstring for Token

    """
    def __init__(self, value, tag, row, col):
        self.value = value
        self.tag = tag
        self.row = row
        self.col = col

    def __str__(self):
        return '<{}, {}, {}, {}>'.format(self.value, self.tag, self.row, self.col)

    def __repr__(self):
        return self.__str__()


class Lexer(dict):
    """
    docstring for Lexer

    """

    def __init__(self, file, *args):
        super().__init__(*args)
        self.pos, self.row, self.col = 0, 1, 1
        self.char = ''
        self.file = open(file, 'r')
        self.string = self.file.readline()
        self.errors_list = list()

    def errors(self):
        """
        print all errors

        """
        import sys
        self.file.close()
        sys.stderr.write('Lexer errors:\n')

        for i in self.errors_list:
            sys.stderr.write('\t%s\n' % i)

        sys.stderr.flush()
        exit(1)

    def error(self, text):
        """
        print error

        """
        self.errors_list.append(
            '{} in line {}, column {}'.format(text, self.row, self.col))

    def next_char(self):
        """
        set next char

        """
        if self.pos < len(self.string):
            self.char = self.string[self.pos]
            if self.char != '\n':
                self.col += 1
                self.pos += 1

            else:
                self.string = self.file.readline()
                self.col = 1
                self.row += 1
                self.pos = 0

        else:
            self.char = '#0'

    def skip_space(self):
        """
        skip spaces

        """
        while self.char.isspace():
            self.next_char()

    def next_token(self):
        """
        return token

        """
        self.skip_space()
        lexem = ''
        # if current char is alpha or _
        if self.char.isalpha() or self.char == '_' or self.char in '+-*/%><=^!?':
            lexem = self.char
            self.next_char()

            # adding all alpha and digit
            while self.char.isalpha() or self.char.isdigit() or self.char in '+-*/%><=^!?':
                lexem += self.char
                self.next_char()
            return Token(lexem, ID, self.col, self.row)

        # if current char is digit
        elif self.char.isdigit():
            # while is digit
            count = 0

            while self.char.isdigit() or self.char == '.':
                if self.char == '.':
                    count += 1

                if count > 1:
                    self.error('Incorrect format of number: "%s"' % self.char)

                lexem += self.char
                self.next_char()
            return Token(int(lexem) if count == 0 else float(lexem), NUMBER, self.col, self.row)

        elif self.char in ('(', ')'):
            lexem = self.char
            self.next_char()
            return Token(lexem, RESERVED, self.col, self.row)

        elif self.char == '#0':
            return Token('EOF', None, self.col, self.row)

        elif self.char == '-':
            lexem = self.char
            self.next_char()

            if self.char.isdigit():
                count = 0

                while self.char.isdigit() or self.char == '.':
                    if self.char == '.':
                        count += 1

                    if count > 1:
                        self.error('Incorrect format of number: "%s"' %
                                   self.char)

                    lexem += self.char
                    self.next_char()
                return Token(int(lexem) if count == 0 else float(lexem), NUMBER, self.col, self.row)

        elif self.char in (';', '{'):
            # skip comments in file
            return self.skip_comments('\n' if self.char == ';' else '}')

        elif self.char == '"':
            self.next_char()

            while self.char != '"':
                if self.char == '\\':
                    lexem += self.char
                    self.next_char()
                    lexem += self.char
                    self.next_char()
                    continue

                lexem += self.char
                self.next_char()

            self.next_char()
            return Token(lexem, STRING, self.col, self.row)

        elif self.char == "'":
            lexem = self.get_quote()
            return Token(lexem[1:], QUOTE, self.col, self.row)

        elif self.char in self:
            lexem = self.char
            self.next_char()
            return Token(lexem, self[lexem], self.col, self.row)

        else:
            lexem = self.char
            self.error('Unknown character: "%s"' % self.char)
            self.next_char()
            return Token(lexem, UNKNOWN, self.col, self.row)
        return None

    def get_quote(self, skip_spaces=True):
        """
        return quote

        """
        lexem = self.char
        if skip_spaces:
            self.skip_space()
        self.next_char()
        while True:
            if self.char == '(':
                lexem += self.get_quote(False)

                if self.char == ')':
                    lexem += self.char
                    self.next_char()

            if self.char != ')':
                lexem += self.char
                self.next_char()

            else:
                return lexem

    def skip_comments(self, char):
        """
        skip comments

        """
        while self.char != char:
            self.next_char()

        self.next_char()
        return self.next_token()

    def gettoken(self):
        """
        return token

        """
        self.next_char()
        while True:
            result = self.next_token()
            if not result:
                continue

            if result.value == 'EOF':
                break

            yield result

    def tokens(self):
        """
        retun list of tokens


        """
        result = [i for i in self.gettoken()]
        return result

    def raw_input(self, user_string):
        """
        return raw user input

        """
        self.string = user_string
        return self.tokens()
