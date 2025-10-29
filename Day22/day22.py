from collections import deque
from typing import *

def dayTwentytwo():

    def mix(secret:int,value:int) -> int:
        return secret^value

    def prune(secret:int) -> int:
        return secret%16777216

    def process(secret:int,times:int) -> int:
        for _ in range(times):
            first = prune(mix(secret,secret*64))
            second = prune(mix(first,first//32))
            third = prune(mix(second,second*2048))
            secret = third
        return secret

    res = 0
    #read
    with open("Day22/22_2.txt", 'r') as file:
        for line in file:
            secret = int(line.rstrip())
            v = process(secret,2000)
            res += v
    return res

def dayTwentytwo2():

    def mix(secret:int,value:int) -> int:
        return secret^value

    def prune(secret:int) -> int:
        return secret%16777216

    def process(secret:int,times:int) -> int:
        d = deque([])
        prev = secret
        h = {}
        for i in range(times):
            first = prune(mix(secret,secret*64))
            second = prune(mix(first,first//32))
            third = prune(mix(second,second*2048))
            if i > 0:
                d.append( (secret%10)-(prev%10) )
                prev = secret
            if len(d) == 4:
                if tuple(d) not in h:
                    h[ tuple(d) ] = secret%10

                d.popleft()

            secret = third

        return h

    #read
    with open("Day22/22_2.txt", 'r') as file:
        allChanges = {}
        for line in file:
            secret = int(line.rstrip())
            hmap:dict = process(secret,2000)
            for k,v in hmap.items():
                if k in allChanges:
                    allChanges[k] += v
                else:
                    allChanges[k] = v

        maxVal = 0
        for v in allChanges.values():
            if v > maxVal:
                maxVal = v
    return maxVal
    
def main():
    print("Hallo")
    print(dayTwentytwo(), "ist die Lösung von Teil 1")
    print(dayTwentytwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()