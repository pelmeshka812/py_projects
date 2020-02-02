def black_or_white():
    f1 = int(input())
    f2 = int(input())
    f3 = int(input())
    f4 = int(input())
    if (f1 % 2 == 0 and f2 % 2 == 0) or (f1 % 2 != 0 and f2 % 2 != 0):
        if (f3 % 2 == 0 and f4 % 2 == 0) or (f3 % 2 != 0 and f4 % 2 != 0):
            print('YES')
        else:
            print('NO')
    if (f1 % 2 == 0 and f2 % 2 != 0) or (f1 % 2 != 0 and f2 % 2 == 0):
        if (f3 % 2 == 0 and f4 % 2 != 0) or (f3 % 2 != 0 and f4 % 2 == 0):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    black_or_white()
