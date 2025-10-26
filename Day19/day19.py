from functools import cache
from typing import *

def dayNineteen():
    res = 0
    arr = []
    counter = 0
    
    def valid(word:str) -> bool:
        if word in arr:
            return True
        for part in arr:
            if word.startswith(part):
                if valid(word[len(part):]):
                    return True
        return False

    #read
    with open("Day19/19_2.txt") as file:
        for line in file:
            if counter == 0:
                arr = line.rstrip().split(', ')
            elif counter > 1:
                word = line.rstrip()
                if valid(word):
                    res += 1

            counter += 1

    return res

def dayNineteen2():
    res = 0
    arr = []
    counter = 0

    @cache
    def valid(word:str) -> int:
        if word == "":
            return 1
        count = 0

        for part in arr:
            if word.startswith(part):
                count += valid(word[len(part):])
        return count

    #read
    with open("Day19/19_2.txt") as file:
        for line in file:
            if counter == 0:
                arr = line.rstrip().split(', ')
            elif counter > 1:
                word = line.rstrip()
                res += valid(word)

            counter += 1

    return res
    
def main():
    print("Hallo")
    print(dayNineteen(), "ist die Lösung von Teil 1")
    print(dayNineteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()