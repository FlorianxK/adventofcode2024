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

#notfinished
def dayNine2():
    arr = []
    with open("Day9/9.txt") as file:
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

    #WTF vielleicht mit hashmap die länge von blöcken oder jedesmal mit n^2 den richtigen block suchen??
    #nur den block drunter ändern
    i,j = 0,len(arr)-1
    free = 0
    c = ''
    use = 0
    while i < j:
        if arr[i] == '.':
            free += 1
            i += 1
        elif arr[j] != '.' and c == '':
            c = arr[j]
            use = 1
            j -= 1
        elif arr[j] != '.' and c == arr[j]:
            use += 1
            j -= 1        
        elif arr[i] != '.' and use <= free and free > 0 and use > 0:
            arr[i-free],arr[j+use] = arr[j+use],arr[i-free]
            free -= 1
            use -= 1
        elif arr[j] == '.':
            j -= 1
        elif arr[i] != '.' and free == 0:
            i += 1
        else:
            free = 0
            use = 0
            i+=1
            j-=1

    res = 0
    for i in range(len(arr)):
        if arr[i] == '.':
            break
        else:
            res += int(arr[i])*i
    return res


def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()