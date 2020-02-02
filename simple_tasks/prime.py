def prime(lst):
    for i in lst:
        if i % 2 == 0:
            yield i


if __name__ == "__main__":
    f = prime([1, 2, 3, 4, 5, 6, 7, 8])
    print(list(f))
