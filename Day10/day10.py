from collections import deque

def dayTen():
    with open("Day10/10_2.txt") as file:
        arr = []
        n = 0
        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                n = len(content)+2
                arr.append('#'*n)
            arr.append('#'+content+'#')
        arr.append('#'*n)

    def bfs(i,j):
        q = deque( [(i,j)] )
        visited = set()
        visited.add( (i,j) )
        peaks = 0
        while q:
            i2,j2 = q.popleft()
            for ni,nj in [ (i2-1,j2),(i2+1,j2),(i2,j2-1),(i2,j2+1) ]:
                if arr[ni][nj] == '#' or arr[ni][nj] == '.':
                    continue
                elif int(arr[ni][nj]) != int(arr[i2][j2])+1:
                    continue
                elif (ni,nj) in visited:
                    continue

                visited.add( (ni,nj) )
                if arr[ni][nj] == '9':
                    peaks += 1
                else:
                    q.append( (ni,nj) )
        return peaks

    res = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == '0':
                res += bfs(i,j)
    return res

def dayTen2():
    with open("Day10/10_2.txt") as file:
        arr = []
        n = 0
        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                n = len(content)+2
                arr.append('#'*n)
            arr.append('#'+content+'#')
        arr.append('#'*n)

    def bfs(i,j):
        q = deque( [(i,j)] )
        visited = { (i,j): 1 }
        peaks = 0
        while q:
            i2,j2 = q.popleft()
            if arr[i2][j2] == '9':
                peaks += visited[(i2,j2)]
            for ni,nj in [ (i2-1,j2),(i2+1,j2),(i2,j2-1),(i2,j2+1) ]:
                if arr[ni][nj] == '#' or arr[ni][nj] == '.':
                    continue
                elif int(arr[ni][nj]) != int(arr[i2][j2])+1:
                    continue
                elif (ni,nj) in visited:
                    visited[ (ni,nj) ] += visited[ (i2,j2) ]
                    continue

                visited[ (ni,nj) ] = visited[ (i2,j2) ]
                q.append( (ni,nj) )
        return peaks

    res = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == '0':
                res += bfs(i,j)
    return res

def main():
    print("Hallo")
    print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()