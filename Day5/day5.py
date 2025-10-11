from typing import DefaultDict

def dayFive():
    with open("Day5/5_2.txt") as file:
        d = DefaultDict(list)
        inp = 1
        res = 0
        for line in file:
            if line == '\n':
                inp = 2
            else:
                if inp == 1:
                    content = line.rstrip().split('|')
                    d[int(content[0])].append(int(content[1]))
                else:
                    content = line.rstrip().split(',')
                    arr = []
                    correctOrder = True
                    for i in range(len(content)):
                        val = int(content[i])
                        if set(arr) & set(d[val]) != set():
                            correctOrder = False
                            #print(content)
                        arr.append(val)
                    
                    if correctOrder:
                        res += arr[len(arr)//2]
        return res

def dayFive2():
    with open("Day5/5_2.txt") as file:
        d = DefaultDict(list)
        inp = 1
        res = 0
        for line in file:
            if line == '\n':
                inp = 2
            else:
                if inp == 1:
                    content = line.rstrip().split('|')
                    d[int(content[0])].append(int(content[1]))
                else:
                    content = line.rstrip().split(',')
                    arr = []
                    correctOrder = True
                    adden = False
                    for v in content:
                        val = int(v)
                        interj = set(arr) & set(d[val])
                        if interj != set():
                            correctOrder = False
                            adden = True

                        arr.append(val)
                        index = len(arr)-1

                        while correctOrder == False and index > 0:
                            if arr[index-1] in d[arr[index]]:
                                arr[index-1],arr[index] = arr[index],arr[index-1]
                                index -= 1
                            else:
                                correctOrder = True
                    if adden:
                        res += arr[len(arr)//2]
        return res

def main():
    print("Hallo")
    print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()