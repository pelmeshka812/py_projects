def xor_cipher(str, key):
    res = ''
    for i in str:
        res += chr(ord(i) ^ key)
    return res


if __name__ == "__main__":
    a = xor_cipher(input("Enter"), 25)
    print(a)
    b = xor_cipher(a, 25)
    print(b)

