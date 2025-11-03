from collections import deque
from typing import *

def dayTwenty():
    res = 0
    arr = []
    dir = [ [-1,0],[1,0],[0,-1],[0,1] ]

    #read
    start = (0,0)
    with open("Day20/20_2.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            temp = []
            for j,v in enumerate(line):
                if v == 'S':
                    start = (len(arr), j)
                temp += v
            arr.append(temp)

    #find correct way first
    way = [start]
    value = 0
    q = deque([start])
    while q:
        i,j = q.popleft()
        for dx,dy in dir:
            nx,ny = i+dx,j+dy
            nxt = (nx,ny)
            #wrong
            if arr[nx][ny] == '#' or nxt in way:
                continue
            #correct
            way.append(nxt)
            value += 1

            if arr[nx][ny] == 'E':
                break
            else:
                q.append(nxt)

    index = 0
    for i,j in way:
        for dx,dy in dir:
            if arr[i+dx][j+dy] == '#':
                nx,ny = i+dx*2,j+dy*2
                #still in bounds
                if nx < 0 or nx >= len(arr[0]) or ny < 0 or ny >= len(arr):
                    continue
                #is thin wall
                if arr[nx][ny] == '.' or arr[nx][ny] == 'E': 
                    nxt = (nx,ny)
                    if nxt in way:
                        normalWay = way.index(nxt)
                        sameSpot = index+2
                        if sameSpot < normalWay:
                            savedSecs = normalWay-sameSpot
                            if savedSecs >= 100:
                                res += 1
        index += 1

    return res

def dayTwenty2():
    arr = []
    dir = [ [-1,0],[1,0],[0,-1],[0,1] ]

    #read
    start = (0,0)
    with open("Day20/20_2.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            temp = []
            for j,v in enumerate(line):
                if v == 'S':
                    start = (len(arr), j)
                temp += v
            arr.append(temp)

    n,m = len(arr[0]),len(arr)
    dists = [ [-1]*n for _ in range(m) ]
    s1,s2 = start
    dists[s1][s2] = 0
    q = deque([start])
    while q:
        cr,cc = q.popleft()
        for dr,dc in dir:
            nr,nc = cr+dr,cc+dc
            if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
            if arr[nr][nc] == '#': continue
            if dists[nr][nc] != -1: continue
            dists[nr][nc] = dists[cr][cc]+1
            q.append( (nr,nc) )

    count = 0
    for r in range(m):
        for c in range(n):
            if arr[r][c] == '#': continue
            for radius in range(2,21):
                for dr in range(radius+1):
                    dc = radius-dr
                    for nr,nc in set([ (r+dr, c+dc), (r+dr, c-dc),(r-dr, c+dc), (r-dr, c-dc) ]):
                        if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                        if arr[nr][nc] == '#': continue
                        if dists[r][c] - dists[nr][nc] >= 100+radius: count += 1
    return count

def main():
    print("Hallo")
    print(dayTwenty(), "ist die Lösung von Teil 1")
    print(dayTwenty2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()