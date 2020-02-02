def is_prime(number):
    for i in range(2, 1001):
        if i != number:
            if number % i == 0:
                return False
            else:
                return True


if __name__ == "__main__":
    print(is_prime(int(input("Enter"))))

