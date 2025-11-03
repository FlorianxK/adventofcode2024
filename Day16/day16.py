import heapq
from typing import *

def daySixteen():
    arr = []
    looking = 1 # 0 Norden, 1 Osten, 2 Süden, 3 Westen
    start = (0,0)
    dirMap = {0:0, 1:1000, 2:2000, 3:1000}
    with open("Day16/16_2.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            temp = []
            for j,v in enumerate(line):
                if v == 'S':
                    start = (len(arr), j)
                temp += v
            arr.append(temp)

        '''
        for a in arr:
            print(''.join(a))
        '''
        h = []
        # value pos dir
        heapq.heappush(h, (0,start,1) )
        visited = set()
        visited.add(start)
        ways = []
        while h:
            value,pos,looking = heapq.heappop(h)
            dir = 0
            for i,j in [ [pos[0]-1,pos[1]],[pos[0],pos[1]+1],[pos[0]+1,pos[1]],[pos[0],pos[1]-1] ]:
                
                v = (looking - dir) % 4

                if arr[i][j] == '.' and (i,j) not in visited:
                    visited.add( (i,j) )
                    heapq.heappush(h, (value+1+dirMap[v],(i,j),dir) )
                elif arr[i][j] == 'E':
                    ways.append(value+1+dirMap[v])
                dir += 1
        return min(ways)

def daySixteen2():
    arr = []
    looking = 1 # 0 Norden, 1 Osten, 2 Süden, 3 Westen
    start = (0,0)
    dirMap = {0:0, 1:1000, 2:2000, 3:1000}
    with open("Day16/16_2.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            temp = []
            for j,v in enumerate(line):
                if v == 'S':
                    start = (len(arr), j)
                temp += v
            arr.append(temp)

        h = []
        # value pos dir path
        heapq.heappush(h, (0,start,1,[start]) )
        # pos dir
        visited = {}
        visited[(start,1)] = 0

        best_cost = float('inf')
        points = set()
        while h:
            value,pos,looking,path = heapq.heappop(h)
            if value > visited.get((pos, looking), float('inf')):
                continue
            dir = 0
            for i,j in [ [pos[0]-1,pos[1]],[pos[0],pos[1]+1],[pos[0]+1,pos[1]],[pos[0],pos[1]-1] ]:
                v = (looking - dir) % 4
                step_cost = 1 + dirMap[v]

                if arr[i][j] == '.':
                    new_cost = value + step_cost
                    prev_cost = visited.get(((i,j), dir), float('inf'))
                    if new_cost < prev_cost:
                        visited[((i,j), dir)] = new_cost
                        heapq.heappush(h, (new_cost,(i,j),dir,path+[(i,j)]) )
                    elif new_cost == prev_cost:
                        heapq.heappush(h, (new_cost,(i,j),dir,path+[(i,j)]) )
                elif arr[i][j] == 'E':
                    total_cost = value + step_cost
                    if total_cost < best_cost:
                        best_cost = total_cost
                        points = set(path + [(i,j)])
                    elif total_cost == best_cost:
                        points.update(path + [(i,j)])
                dir += 1
        '''
        for i,j in points:
            arr[i][j] = 'O'
        for a in arr:
            print(''.join(a))
        '''
        return len(points)

def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    print(daySixteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()