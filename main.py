import os
import sys

cv = 0
cond = ''
then = ''
val = 0
elseTrue = ''
num = 0
more = ''
comment = ''
py = ''
func = 'func()'
thenLog = ''
mathE = False
inputE = False
inputA = ''

def for1():
        try:
            times = int(input('times:  '))
        except ValueError as e:
            print(f'Error: {e}')
            return
        do = input('do:  ')
        if do == 'log':
            log = input('log:  ')
            for i in range(times):
                print(log)
        elif do == 'alert':
            try:
                times1 = int(input('times:  '))
            except ValueError as e:
                print(f'Error: {e}')
                return
            alert = input('alert:  ')
            for i in range(times + times1):
                print(alert)
        elif do.strip() == '':
            print('Error: empty')
        else:
            print('Error: not a valid block')

while True:
    cmd = input('> ')
    if cmd == 'log':
        cmd = input('log:  ')
        if cmd == 'cv':
            print(cv)
        else:
            print(cmd)
    elif cmd == 'alert':
        cmd = input('alert:  ')
        num = int(input('times:  '))
        if cmd == 'cv':
            for i in range(num):
                print(cv)
        else:
            for i in range(num):
                print(cmd)
    elif cmd.strip() == '':
        print('Error: empty line of code')
    elif cmd == 'get':
        print('only use ints and only use cv for the var')
        cv = int(input('int:  '))
    elif cmd == 'if':
        cond = input('condition:  ')
        then = input('then:  ')
        elseTrue = input('want else y/n:  ')
        if cond == f'cv == {cv}':
            if then == 'log':
                val = input('input:  ')
                print(val)
            elif then == 'alert':
                val = then
                cmd = int(input('times:  '))
                for i in range(cmd):
                    print(val)
        else:
            if elseTrue == 'y':
                if cond == f'cv == {cv}':
                    if then == 'log':
                        val = input('input:  ')
                        print(val)
                elif then == 'alert':
                    val = then
                    cmd = int(input('times:  '))
                    for i in range(cmd):
                        print(val)
                val = input('else: ')
                if val == 'log':
                    if then == 'log':
                        val = input('input:  ')
                        print(val)
                elif val == 'alert':
                    val = then
                    cmd = int(input('times:  '))
                    for i in range(cmd):
                        print(val)
    elif cmd == 'more':
        more = input('more:  ')
        if more == 'c':
            os.system('clear')
        elif more == 'p':
            print('use q to exit')
            while True:
                py = input('>>> ')
                if py == 'q':
                    break
                try:
                    exec(py)
                except Exception as e:
                    print(f'Error: {e}')
        elif more.strip() == '':
            print(f'Error: line is empty')
        elif more == 'f':
            if thenLog == 'cv':
                print(cv)
            else:
                print(thenLog)
        elif more == 'q':
            sys.exit()
        elif more == 'e':
            pass
        else:
            print(f'Error: {more} does not exist')
    elif cmd == '#':
        comment = input('comment:  ')
    elif cmd == 'func':
        func = input('name:  ')
        if func.endswith('()'):
            print(f'use {func} to call')
            wV = bool(input('with var? (True/False):  '))
            if wV == True:
                print('log your variable called fv')
                fv = input('fv value:  ')
            thenLog = input('then log:  ')
        else:
            print('failed')
            func = 'func()'
    elif cmd == func:
        if thenLog == 'fv':
            print(fv)
        elif thenLog == 'cv':
            print('Error: invalid cv scope is in functions')
        else:
            print(thenLog)
    elif cmd == 'for':
        for1()
    elif cmd == 'import':
        importS = input('import:  ')
        if importS == 'math':
            mathE = True
        elif importS == 'input':
            inputE = True
        else:
            print(f'Error: {importS} does not exist')
    elif mathE == True and cmd == 'math.logadd':
        try:
            print(int(input('1:  ')) + int(input('2:  ')))
        except ValueError as e:
            print(f'Error: {e}')
    elif mathE == True and cmd == 'math.logsubtract':
        try:
            print(int(input('1:  ')) - int(input('2:  ')))
        except ValueError as e:
            print(f'Error: {e}')
    elif inputE == True and cmd == 'input.get':
        get = input('get:  ')
        inputA = input(get)
    elif inputE == True and cmd == 'input.return':
        print(inputA)
    elif cmd == 'unimport':
        unimportS = input('unimport:  ')
        if unimportS == 'math':
            mathE = False
        elif unimportS == 'input':
            inputE = False
        elif unimportS.strip() == '':
            print('Error:  empty line')
        else:
            print(f'Error: {unimportS} does not exist')
    elif cmd == 'libs':
        print('librarys: math, input')
    else:
        print(f'Error: {cmd} is not a valid block')
