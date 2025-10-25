from collections import deque
from typing import *

def dayEighteen():
    #read
    width, height = 70+1,70+1
    bytesAllowed = 1024
    arr = []
    for _ in range(height):
        arr.append(width*['.'])

    with open("Day18/18_2.txt") as file:
        for line in file:
            if bytesAllowed == 0:
                break
            x,y = [int(a) for a in line.rstrip().split(',')]
            arr[y][x] = '#'
            bytesAllowed -= 1

    res = []
    q = deque([ ((0,0),0) ])
    visited = set()
    visited.add( (0,0) )
    while q:
        curr,steps = q.popleft()
        y,x = curr
        for dx,dy in [ [-1,0],[1,0],[0,-1],[0,1] ]:
            nx,ny = x+dx,y+dy
            #not valid
            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                continue
            #valid but wrong
            if arr[ny][nx] == '#' or (ny,nx) in visited:
                continue 

            if nx == width-1 and ny == height-1:
                res.append(steps+1)
            elif arr[ny][nx] == '.':
                q.append( ((ny,nx),steps+1) )
            visited.add( (ny,nx) )

    return min(res)

def dayEighteen2():
    #read
    width, height = 70+1,70+1
    arr = []
    bitStack = []
    for _ in range(height):
        arr.append(width*['.'])

    with open("Day18/18_2.txt") as file:
        for line in file:
            x,y = [int(a) for a in line.rstrip().split(',')]
            arr[y][x] = '#'
            bitStack.append( (x,y) )

    res = 0
    changed = ""

    while res == 0:
        q = deque([ ((0,0),0) ])
        visited = set()
        visited.add( (0,0) )
        while q:
            curr,steps = q.popleft()
            y,x = curr
            for dx,dy in [ [-1,0],[1,0],[0,-1],[0,1] ]:
                nx,ny = x+dx,y+dy
                #not valid
                if ny < 0 or ny >= height or nx < 0 or nx >= width:
                    continue
                #valid but wrong
                if arr[ny][nx] == '#' or (ny,nx) in visited:
                    continue 

                if nx == width-1 and ny == height-1:
                    res = steps+1
                    return changed
                elif arr[ny][nx] == '.':
                    q.append( ((ny,nx),steps+1) )
                visited.add( (ny,nx) )

        x,y = bitStack.pop()
        arr[y][x] = '.'
        changed = f"{x},{y}"
    
def main():
    print("Hallo")
    #print(dayEighteen(), "ist die Lösung von Teil 1")
    print(dayEighteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()