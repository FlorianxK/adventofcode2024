from typing import *

def dayOne():
    with open("Day1/1_2.txt") as file:
        l,r = [],[]
        for line in file:
            arr = line.rstrip('\n').split('   ')
            l.append(int(arr[0]))
            r.append(int(arr[1]))

        l.sort()
        r.sort()
        diff = 0
        for i in range(min(len(l),len(r))):
            diff += abs(l[i]-r[i])
    return diff

def dayOne2():
    with open("Day1/1_2.txt") as file:
        l,r = [],[]
        for line in file:
            arr = line.rstrip('\n').split('   ')
            l.append(int(arr[0]))
            r.append(int(arr[1]))

        c = Counter(r)
        similarity = 0
        for i in range(len(l)):
            similarity += l[i] * c[l[i]]
    return similarity

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()