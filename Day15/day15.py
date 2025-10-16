from collections import deque
from typing import *

def dayFifteen():
    #write field into arr
    arr = []
    robot = [0,0]
    dir = { '^': (-1,0), 'v': (1,0), '>': (0,1), '<': (0,-1) }
    with open("Day15/15_2.txt", 'r') as file:
        firstMode = True
        for line in file:
            if line == '\n':
                firstMode = False
                print("Initial state:")
                for a in arr:
                    print(''.join(a))
                continue

            line = line.rstrip()
            if firstMode:
                temp = []
                for j,v in enumerate(line):
                    if v == '@':
                        robot = [len(arr), j]
                    temp += v
                arr.append(temp)
            else:
                for move in line:
                    i,j = dir[move]
                    ri,rj = robot
                    ni,nj = i+ri,j+rj

                    #moves auf ein freies feld
                    if arr[ni][nj] =='.':
                        arr[ri][rj] = '.'
                        arr[ni][nj] = '@'
                        robot = [ni,nj]

                    #moves gegen box
                    if arr[ni][nj] == 'O':
                        stack = ['@','O']
                        while stack:
                            ni,nj = i+ni,j+nj
                            if arr[ni][nj] == '#':
                                break 
                            elif arr[ni][nj] == 'O':
                                stack.append('O')
                            elif arr[ni][nj] == '.':
                                bi,bj = ni,nj
                                while stack:
                                    arr[bi][bj] = stack.pop()
                                    bi,bj = bi-i,bj-j

                                arr[ri][rj] = '.'
                                robot = [bi+i,bj+j]
                    '''
                    print(f"Move {move}:")
                    for a in arr:
                        print(''.join(a))
                    '''
    print("Final field:")
    for a in arr:
        print(''.join(a))

    #count boxes
    res = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == 'O':
                res += 100 * i + j
    return res

def dayFifteen2():
    #write field into arr
    arr = []
    robot = [0,0]
    dir = { '^': (-1,0), 'v': (1,0), '>': (0,1), '<': (0,-1) }
    with open("Day15/15_3.txt", 'r') as file:
        firstMode = True
        for line in file:
            if line == '\n':
                firstMode = False
                print("Initial state:")
                for a in arr:
                    print(''.join(a))
                continue

            line = line.rstrip()
            if firstMode:
                temp = []
                for j,v in enumerate(line):
                    if v == '@':
                        robot = [len(arr), j*2]
                    if v == '#':
                        temp += "##"
                    elif v == 'O':
                        temp += "[]"
                    elif v == '.':
                        temp += ".."
                    elif v == '@':
                        temp += "@."
                arr.append(temp)
            else:
                for move in line:
                    i,j = dir[move]
                    ri,rj = robot
                    ni,nj = i+ri,j+rj

                    #moves auf ein freies feld
                    if arr[ni][nj] =='.':
                        arr[ri][rj] = '.'
                        arr[ni][nj] = '@'
                        robot = [ni,nj]

                    #moves gegen box
                    if arr[ni][nj] == '[' or arr[ni][nj] == ']':
                        if i == 0: #links und rechts
                            stack = ['@',']','[']
                            while stack:
                                nj = 2*j+nj
                                if arr[ni][nj] == '#':
                                    break 
                                elif arr[ni][nj] == '[' or arr[ni][nj] == ']':
                                    stack.append(']')
                                    stack.append('[')
                                elif arr[ni][nj] == '.':
                                    bj = nj
                                    while stack:
                                        arr[ni][bj] = stack.pop()
                                        bj = bj-j

                                    arr[ri][rj] = '.'
                                    robot = [ni,bj+j]

                        elif j == 0: #oben und unten
                            blocked = False
                            q = deque()
                            if arr[ni][nj] == '[':
                                q.append( [(ni,nj),(ni,nj+1)] )
                            elif arr[ni][nj] == ']':
                                q.append( [(ni,nj-1),(ni,nj)] )

                            allLevel = [q[0]]
                            while q:
                                tempLevel = q.copy()
                                nextLevel = deque()
                                while tempLevel:
                                    curr = tempLevel.popleft()
                                    for v1,v2 in curr:
                                        v1 += i
                                        if arr[v1][v2] == '#':
                                            nextLevel.clear()
                                            break
                                        elif arr[v1][v2] == '[' and arr[v1][v2+1] == ']':
                                            newPair = [(v1,v2),(v1,v2+1)]
                                            if newPair not in nextLevel:
                                                nextLevel.append( newPair )
                                        elif arr[v1][v2-1] == '[' and arr[v1][v2] == ']':
                                            newPair = [(v1,v2-1),(v1,v2)]
                                            if newPair not in nextLevel:
                                                nextLevel.append( newPair )
                                if nextLevel:
                                    q = nextLevel
                                    allLevel.extend(nextLevel)
                                else:
                                    blocked = True
                                    break
                            print(allLevel)
                            #von hinten durchgehen und soweit in richtung v1+i bis blocked
                            if not blocked:
                                pass

                    print(f"Move {move}:")
                    for a in arr:
                        print(''.join(a))
                    
    '''
    print("Final field:")
    for a in arr:
        print(''.join(a))

    #count boxes
    res = 0
    
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == 'O':
                res += 100 * i + j
    '''
    return 0
    
def main():
    print("Hallo")
    print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()