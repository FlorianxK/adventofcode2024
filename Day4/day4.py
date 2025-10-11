def dayFour():
    with open("Day4/4_2.txt") as file:
        arr = []
        dir = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        n = 0
        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                n = len(content)+2
                arr.append('0'*n)
            arr.append('0'+content+'0')
        arr.append('0'*n)

    res = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == 'X':
                for x,y in dir:
                    pattern = ""
                    pos = (i,j)
                    for _ in range(4):
                        if arr[pos[0]][pos[1]] == '0':
                            break
                        else:
                            pattern += arr[pos[0]][pos[1]]
                            pos = (pos[0]+x,pos[1]+y)
                    if pattern == "XMAS":
                        res += 1

    return res

def dayFour2():
    with open("Day4/4_2.txt") as file:
        arr = []
        dir = [(1,1), (1,-1), (-1,-1), (-1,1)]
        n = 0
        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                n = len(content)+2
                arr.append('0'*n)
            arr.append('0'+content+'0')
        arr.append('0'*n)

    res = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == 'A':
                pair = 0
                for x,y in dir:
                    if arr[i+x][j+y] == 'M' and arr[i+x*(-1)][j+y*(-1)] == 'S':
                        pair += 1

                if pair == 2:
                    res += 1
    return res

def main():
    print("Hallo")
    print(dayFour(), "ist die Lösung von Teil 1")
    print(dayFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()