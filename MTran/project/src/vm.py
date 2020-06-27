import operator as op
from .lexer import ID, Token

GLOBAL = dict()
GLOBAL['+'] = lambda env, *x: obs(env, op.add, *x)
GLOBAL['-'] = lambda env, *x: obs(env, op.sub, *x)
GLOBAL['*'] = lambda env, *x: obs(env, op.mul, *x)
GLOBAL['/'] = lambda env, *x: obs(env, op.truediv, *x)
GLOBAL['//'] = lambda env, *x: obs(env, op.floordiv, *x)
GLOBAL['%'] = lambda env, *x: obs(env, op.mod, *x)
GLOBAL['='] = lambda env, *x: obs(env, op.eq, *x)
GLOBAL['/='] = lambda env, *x: obs(env, op.ne, *x)
GLOBAL['>'] = lambda env, *x: obs(env, op.gt, *x)
GLOBAL['<'] = lambda env, *x: obs(env, op.lt, *x)
GLOBAL['>='] = lambda env, *x: obs(env, op.ge, *x)
GLOBAL['<='] = lambda env, *x: obs(env, op.le, *x)
GLOBAL['~'] = lambda env, *x: obs(env, op.ne, *x)
GLOBAL['setq'] = lambda env, *x: setq(env, *x)
GLOBAL['defun'] = lambda env, *x: defun(env, *x)
GLOBAL['if'] = lambda env, *x: compare(env, *x)
GLOBAL['write'] = lambda env, *x: write(env, *x)
GLOBAL['print'] = lambda env, *x: write_line(env, *x)
GLOBAL['readint'] = lambda env, *x: readint(env, *x)


class Procedure(object):
    """
    procedure

    """

    def __init__(self, params, *body):
        """
        params, expr, env

        """
        self.params, self.body = params, body

    def __call__(self, env, *args):
        if len(args) != len(self.params):
            msg = "Too many args! Expected %s, given %s" % (len(self.params), len(args))
            msg += ' in line {}, column {}'.format(args[0].col, args[0].row)
            raise TypeError(msg)

        for i, par in enumerate(self.params):
            env[par.value] = execute(args[i], env)

        magic = False
        while True:
            if magic:
                for i, par in enumerate(self.params):
                    env[par.value] = args[i]
            # вычисляем тело функции
            length = len(self.body) - 1
            for i, expr in enumerate(self.body):
                if i < length:  # если это не последнее выражение
                    result = execute(expr, env)
                    magic = True
                    if magic and result:
                        return result
                else:
                    if isinstance(env[expr[0].value], Procedure):
                        proc = env[expr[0].value]
                        self.params = proc.params
                        self.body = proc.body
                        args = [execute(i, env) for i in expr[1:]]
                        magic = True
                    else:
                        result = execute(expr, env)
                        return result


def obs(env, fun, *args):
    """
    obs

    """
    result = execute(args[0], env)
    for i in args[1:]:
        result = fun(result, execute(i, env))
    return result


def defun(env, *args):
    """
    defune new function

    """
    name, params, *body = args
    proc = Procedure(params, *body)
    if not name.value in env:
        env[name.value] = proc
    else:
        msg = 'Function "%s" already exists!' % name.value
        msg += 'in line {}, column {}'.format(name.col, name.row)
        raise Exception(msg)


def compare(env, *args):
    """
    get condition and execute first or second body

    """
    if execute(args[0], env):
        return execute(args[1], env)
    elif len(args) == 3:
        return execute(args[2], env)


def write(env, *args):
    """
    write line

    """
    from sys import stdout
    stdout.write(str(execute(args[0], env)))
    stdout.flush()


def write_line(env, *args):
    """
    write new line

    """
    from sys import stdout
    stdout.write('%s\n' % str(execute(args[0], env)))
    stdout.flush()


def readint(env, *args):
    """
    read line

    """
    i = 0
    env[args[i].value] = int(input())

    from sys import stdout
    if isinstance(args[i].value, str):
        stdout.write(str(execute(args[0], env)))
        stdout.flush()


def setq(env, *args):
    """
    define new variables

    """
    i = 0
    while i < len(args):
        env[args[i].value] = execute(args[i + 1], env)
        i += 2


def execute(expr, env):
    """
    execute

    """
    if isinstance(expr, Token):
        if expr.tag == ID and expr.value in env:
            return env[expr.value]
        else:
            return expr.value
    else:
        first, *second = expr
        if first.value in env and callable(env[first.value]):
            return env[first.value](env, *second)
        else:
            msg = 'Function "%s" not exists!' % first.value
            msg += 'in line {}, column {}'.format(first.col, first.row)
            raise Exception(msg)
