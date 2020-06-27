class Parser(object):
    """
    class Parser

    """

    def __init__(self):
        self.tokens = None

    def _node(self, pos):
        """
        return new node and pos

        """
        node = list()
        while self.tokens[pos].value != ')':
            if self.tokens[pos].value == '(':
                new_node, pos = self._node(pos + 1)
                node.append(new_node)

            else:
                node.append(self.tokens[pos])
            pos += 1

        return node, pos

    def build(self, tokens):
        """
        return ast

        """
        ast = list()
        if tokens:
            pos = 0
            self.tokens = tokens

            while pos < len(tokens):
                if tokens[pos].value == '(':
                    node, pos = self._node(pos + 1)
                    pos += 1
                    ast.append(node)

                else:
                    msg = 'Parser error! Expected "(" but given "%s"' % tokens[pos].value
                    msg += ' in line {}, column {}'.format(tokens[pos].col - 1, tokens[pos].row)
                    raise Exception(msg)

        return ast
