def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_year_leap(int(input("Enter year"))))
