def season(month_number):
    if 2 < month_number < 6:
        print("spring")
    elif 5 < month_number < 9:
        print("summer")
    elif 8 < month_number < 12:
        print("autumn")
    else:
        print("winter")


if __name__ == "__main__":
    season(int(input("Enter month number")))
