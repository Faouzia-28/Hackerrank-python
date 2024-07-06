def solve(s):
    words = s.strip()
    words=words+" "
    result=""
    for i in range(len(words)):
        if words[i].isalpha and words[i-1]==" ":
            result+=words[i].upper()
        else:
            result+=words[i]
    return result.strip()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
