if __name__ == '__main__':
    records={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name]=score
    uniquescore=sorted(list(set(records.values())))
    seclow=uniquescore[1]
    modname=[]
    for a,b in records.items():
        if b==seclow:
            modname.append(a)
    modname=sorted(modname)
    for i in modname:
        print(i)