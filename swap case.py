def swap_case(s):
    s1=[]
    for char in s:
        if char.isalpha():
            if char.islower():
                s1.append(char.upper())
            else:
                s1.append(char.lower())
        elif char.isdigit():
            s1.append(char)
        else:
            s1.append(char)
    return ''.join(s1)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)