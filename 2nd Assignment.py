
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Choose arithmetic operator: ")
a = int(a)
b = int(b)
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == '**':
    print(a ** b)
elif c == '%':
    print(a % b)
elif c == '=':
    print(a == b)
elif c == '//':
    print(a // b)
else:
    print("PLEASE CHOOSE AN ARITHMETIC OPERATOR!")
