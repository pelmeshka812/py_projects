str = input("Enter:")
try:
    splited_str = str.split(" ")
    f = int(splited_str[1])
    s = int(splited_str[2])
    if str[0] == '+':
        print(f + s)
    elif str[0] == '-':
        print(f - s)
    elif str[0] == '*':
        print(f * s)
    elif str[0] == '/':
        try:
            print(f / s)
        except ZeroDivisionError:
            print("Zero Division Error")
except ValueError:
    print("Value Error")
