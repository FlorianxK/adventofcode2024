from typing import *

def dayTwentyfive():
    locks = []
    keys = []
    height = 0
    #read
    with open("Day25/25_2.txt", 'r') as file:
        firstLine = True
        firstRead = True
        key = True
        for line in file:
            if line != '\n':
                if firstRead:
                    height += 1
                line = line.rstrip()
                n = len(line)
                if firstLine:
                    temp = [-1]*n
                    if line == '#'*n:
                        key = False
                    firstLine = False
                
                for i in range(n):
                    if line[i] == '#':
                        temp[i] += 1
            else:
                if key:
                    keys.append(temp)
                else:
                    locks.append(temp)
                firstLine = True
                firstRead = False
                key = True
        if key:
            keys.append(temp)
        else:
            locks.append(temp)

    #compare
    pairs = 0
    for k in keys:
        for l in locks:
            pair = True
            for i in range(len(l)):
                if k[i]+l[i]+2 > height:
                    pair = False
                    break
            if pair:
                pairs += 1
    return pairs    

def dayTwentyfive2():
    pass

def main():
    print("Hallo")
    print(dayTwentyfive(), "ist die Lösung von Teil 1")
    #print(dayTwentyfive2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()