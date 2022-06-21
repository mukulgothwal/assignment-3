n1 = float(input('Enter first number: '))
a = input('Enter sign(+, -, *, / or q for quit): ')

while (a!='q'):
    if a=='+':
        n1 = n1 + float(input('Next number: '))
    elif a == '-':
        n1 = n1 - float(input('Next number: '))
    elif a == '*':
        n1 == n1 * float(input('Next number: '))
    elif a == '/':
        n1 = n1 / float(input('Next number: '))
    else:
        print('Invalid operator, try again')
    a = input('Enter next sign(+, -, *, / or q for quit): ')

print(n1)
