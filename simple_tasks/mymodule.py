def die():
    print("DIE")


# def christmas_tree():

STRAR = '*'
SPACE = ' '

if __name__ == "__main__":
    rows = input(">>")
    spaces = len(rows) - 1
    stars = 1

    for i in rows:
        print((SPACE*spaces)+(i*stars) + (SPACE*spaces)
        )
        stars +=2
        spaces -=1