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
    pass
    
def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    print(daySixteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()