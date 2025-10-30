from collections import defaultdict
from typing import *

def dayTwentythree():
    d = defaultdict(set)
    firstL = 't'

    #read
    with open("Day23/23_2.txt", 'r') as file:
        for line in file:
            a,b = line.rstrip().split('-')
            d[a].add(b)
            d[b].add(a)

    triples = set()
    for first in d:
        for second in d[first]:
            for third in d[second]:
                if first in d[third]:
                    if first[0] == firstL or second[0] == firstL or third[0] == firstL:
                        t = [first,second,third]
                        t.sort()
                        triples.add( tuple(t) )
    return len(triples)

def dayTwentythree2():
    d = defaultdict(set)

    #read
    with open("Day23/23_2.txt", 'r') as file:
        for line in file:
            a,b = line.rstrip().split('-')
            d[a].add(b)
            d[b].add(a)

    groups = set()

    def build_group(node,group):
        password = ','.join(sorted(group))
        if password in groups:
            return
        groups.add(password)
        for neighbor in d[node]:
            #schon teil von gruppe
            if neighbor in group:
                continue
            #nicht vollständig
            if any(neighbor not in d[x] for x in group):
                continue
            build_group(neighbor, {*group,neighbor})

    for node in d:
        build_group(node,{node})
    return max(groups,key=len)

def main():
    print("Hallo")
    print(dayTwentythree(), "ist die Lösung von Teil 1")
    print(dayTwentythree2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()