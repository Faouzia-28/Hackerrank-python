if __name__ == '__main__':
    N = int(input())
    li=[]
    for i in range(N):
        s=input().split()
        if s[0].lower()=="insert":
            li.insert(int(s[1]),int(s[2]))
        if s[0].lower()=="print":
            print(li)
        if s[0].lower()=="remove":
            li.remove(int(s[1]))
        if s[0].lower()=="append":
            li.append(int(s[1]))
        if s[0].lower()=="sort":
            li.sort()
        if s[0].lower()=="pop":
            li.pop()
        if s[0].lower()=="reverse":
            li.reverse()