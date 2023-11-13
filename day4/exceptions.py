
try:
    num = 10 / 0
    print(num)
except:
    print('Something went wrong')
else: # it is optional
    print('Nothing went wrong')
finally: # it is optional
    print('finally block')


print('Test Completed')

print('-----------------------------------')

tuple1 = (10, 20, 30, 40)

try:
    print(tuple1[2])
except LookupError: # if you specify the type should be matched with error
    print('The index number is too large')
else:
    print('index number is valid')

print('-----------------------------------')

try:
    raise FileNotFoundError('no such a file')
except SyntaxError:
    print('it is a syntax error')
except OSError:
    print('It is an operating system error')
except ArithmeticError:
    print('aritmethic error')
finally:
    print('finally block')

