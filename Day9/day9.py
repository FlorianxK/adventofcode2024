import heapq

def dayNine():
    arr = []
    with open("Day9/9_2.txt") as file:
        id = 0
        isFile = True
        while 1:
            char = file.read(1)
            if not char:
                break
            else:
                if isFile:
                    isFile = False
                    for _ in range(int(char)):
                        arr.append(id)
                    id += 1
                else:
                    isFile = True
                    for _ in range(int(char)):
                        arr.append('.')

    i,j = 0,len(arr)-1
    while i < j:
        if arr[i] == '.' and arr[j] != '.': #left . , right num
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
        elif arr[i] == '.' and arr[j] == '.': #left . , right .
            j -= 1
        elif arr[i] != '.' and arr[j] != '.': #left num , right num
            i += 1
        elif arr[i] != '.' and arr[j] == '.': #left num , right .
            i += 1
            j -= 1

    res = 0
    for i in range(len(arr)):
        if arr[i] == '.':
            break
        else:
            res += int(arr[i])*i
    return res

def dayNine2():

    def calcRes(arr):
        res = 0
        for i in range(len(arr)):
            if arr[i] != '.':
                res += int(arr[i])*i
        return res

    arr = []
    with open("Day9/9_2.txt") as file:
        id = 0
        isFile = True
        while 1:
            char = file.read(1)
            if not char:
                break
            else:
                if isFile:
                    isFile = False
                    for _ in range(int(char)):
                        arr.append(id)
                    id += 1
                else:
                    isFile = True
                    for _ in range(int(char)):
                        arr.append('.')

    arrFree = []
    curr = 0
    index = 0
    for i in range(len(arr)):
        if curr == 0 and arr[i] == '.':
            index = i
            curr = 1
        elif curr > 0 and arr[i] == '.':
            curr += 1
        elif arr[i] != '.' and curr > 0:
            heapq.heappush(arrFree, (index,curr) )
            curr = 0        
    if arr[-1] == '.':
        heapq.heappush(arrFree, (index,curr) )

    l,r = len(arr)-1,len(arr)-1
    while 0 <= l and 0 <= r:
        if l == r and arr[r] == '.':
            l-=1
            r-=1
        elif l == r and arr[r] != '.':
            toMove = 0
            while arr[l] == arr[r]:
                toMove += 1
                l-=1

            # r nach links moven bis r==l and dabei die elemente verschieben
            temp = []
            while arrFree:
                index,space = heapq.heappop(arrFree)

                if l < index:
                    temp.append( (index,space) )
                    break
                elif toMove > space:
                    temp.append( (index,space) )
                elif toMove <= space:
                    moved = 0
                    while toMove > 0:
                        arr[r],arr[index] = arr[index],arr[r]
                        index+=1
                        r-=1
                        moved += 1
                        toMove -= 1
                    if moved > 0:
                        heapq.heappush(arrFree, (index,space-moved) )
                    break
            
            for v in temp:
                heapq.heappush(arrFree,v)
            r = l

    return calcRes(arr)

def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()