from collections import deque

def dayTwelve():
    visit = set()
    arr = []
    dir = [(-1,0), (1,0), (0,-1), (0,1)]

    #read
    with open("Day12/12.txt") as file:
        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                arr.append('#'*(len(content)+2))
            arr.append('#'+content+'#')
        arr.append('#'*(len(content)+2))
    for a in arr:
        print(a)
    
    #return area*peri for group
    def bfs(i,j):
        d = deque([(i,j)])
        visit.add((i,j))
        area = 0
        peri = 0

        while d:
            curr = d.popleft()
            area += 1

            for dx,dy in dir:
                nxt = arr[curr[0]+dx][curr[1]+dy]
                if arr[curr[0]][curr[1]] != nxt:
                    peri +=1
                else:
                    tmp = (curr[0]+dx,curr[1]+dy)
                    if tmp not in visit:
                        d.append(tmp)
                        visit.add(tmp)
        return area*peri

    m,n = len(arr),len(arr[0])
    res = 0
    for i in range(1,m-1):
        for j in range(1,n-1):
            if (i,j) not in visit:
                res += bfs(i,j)
    return res

#notfinished
def dayTwelve2():
    visit = set()
    arr = []
    dir = [(-1,0), (1,0), (0,-1), (0,1)]

    #read
    with open("Day12/12.txt") as file:
        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                arr.append('#'*(len(content)+2))
            arr.append('#'+content+'#')
        arr.append('#'*(len(content)+2))
    for a in arr:
        print(a)
    
    #return area*side for group
    def bfs(i,j):
        d = deque([(i,j)])
        visit.add((i,j))
        area = 0
        side = 0
        group = set()
        group.add((i,j))
        #nur die seiten zählen nicht perimeter
        while d:
            curr = d.popleft()
            area += 1

            for dx,dy in dir:
                nxt = arr[curr[0]+dx][curr[1]+dy]

                if arr[curr[0]][curr[1]] == nxt:
                    tmp = (curr[0]+dx,curr[1]+dy)
                    if tmp not in visit:
                        d.append(tmp)
                        visit.add(tmp)

                        group.add(tmp)
        
        print(group)
        #mario kart einmal rumfahren
        #for x,y in group:
        #    print()

        print(str(area) + " and " + str(side))
        return area*side

    m,n = len(arr),len(arr[0])
    res = 0
    for i in range(1,m-1):
        for j in range(1,n-1):
            if (i,j) not in visit:
                tmp = bfs(i,j)
                #print(tmp)
                res += tmp
    return res

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    print(dayTwelve2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()