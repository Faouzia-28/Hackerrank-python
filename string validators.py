def alpnu(s):
    for char in s:
        if char.isalnum():
            return True
    return False
def alp(s):
    for char in s:
        if char.isalpha():
            return True
    return False
def digi(s):
    for char in s:
        if char.isdigit():
            return True
    return False
def low(s):
    for char in s:
        if char.islower():
            return True
    return False
def up(s):
    for char in s:
        if char.isupper():
            return True
    return False

if __name__ == '__main__':
    s = input()
    print(alpnu(s))
    print(alp(s))
    print(digi(s))
    print(low(s))
    print(up(s))
