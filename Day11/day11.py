
from functools import cache
from typing import DefaultDict

def dayEleven(pAmount:int):
    with open("Day11/11_2.txt") as file:
        d = DefaultDict(int)
        for stone in map(int, file.read().strip().split(' ')):
            d[stone] += 1

        @cache
        def oneStone(stone):
            if stone == 0:
                return [1]
            
            s = str(stone)
            if len(s) % 2 == 0:
                first = s[:len(s)//2]
                second = s[len(s)//2:]
                return [int(first), int(second)]

            return [stone*2024]

        for _ in range(1, pAmount+1):
            d_new = DefaultDict(int)
            for k,v in d.items():
                for value in oneStone(k):
                    d_new[value] += v
            d = d_new

        return sum(d.values())

def main():
    print("Hallo")
    print(dayEleven(25), "ist die Lösung von Teil 1")
    print(dayEleven(75), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()