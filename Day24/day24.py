from collections import defaultdict, deque
from typing import *

def dayTwentyfour():
    d = defaultdict(int)
    rules = deque([])
    #read
    firstMode = True
    with open("Day24/24_2.txt", 'r') as file:
        for line in file:
            if line == '\n':
                firstMode = False
                continue

            if firstMode:
                k,v = line.rstrip().split(': ')
                d[k] = int(v)
            else:
                l,r = line.rstrip().split(' -> ')
                f,op,s = l.split(' ')
                if f in d.keys() and s in d.keys():
                    if op == "AND":
                        d[r] = d[f] & d[s]
                    elif op == "XOR":
                        d[r] = d[f] ^ d[s]
                    elif op == "OR":
                        d[r] = d[f] | d[s]
                else:
                    rules.append( [l,r] )

    while rules:
        l,r = rules.popleft()
        f,op,s = l.split(' ')
        if f in d.keys() and s in d.keys():
            if op == "AND":
                d[r] = d[f] & d[s]
            elif op == "XOR":
                d[r] = d[f] ^ d[s]
            elif op == "OR":
                d[r] = d[f] | d[s]
        else:
            rules.append( [l,r] )

    d = dict(sorted(d.items()))
    res = ""
    for k,v in d.items():
        if k[0] == 'z':
            res += str(v)

    return int(res[::-1],2)

def dayTwentyfour2():
    pass

def main():
    print("Hallo")
    print(dayTwentyfour(), "ist die Lösung von Teil 1")
    print(dayTwentyfour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()