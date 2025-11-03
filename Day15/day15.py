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
                    di,dj = dir[move]
                    ri,rj = robot
                    do_move = True
                    to_move = [(ri,rj)]
                    counter = 0
                    while counter < len(to_move):
                        ci,cj = to_move[counter]
                        counter += 1
                        ni,nj = di+ci,dj+cj
                        if (ni,nj) in to_move:
                            continue
                        if arr[ni][nj] == '#':
                            do_move = False
                            break
                        if arr[ni][nj] == '.':
                            continue
                        if arr[ni][nj] == 'O':
                            to_move.append((ni,nj))
                        else:
                            assert False
                    
                    if do_move:
                        grid_copy = [list(row) for row in arr]
                        robot = (ri+di,rj+dj)
                        for rr,cc in to_move:
                            arr[rr][cc] = '.'
                        for rr,cc in to_move:
                            arr[rr+di][cc+dj] = grid_copy[rr][cc]

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
    with open("Day15/15_2.txt", 'r') as file:
        firstMode = True
        for line in file:
            if line == '\n':
                firstMode = False
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
                    di,dj = dir[move]
                    ri,rj = robot
                    do_move = True
                    to_move = [(ri,rj)]
                    counter = 0
                    while counter < len(to_move):
                        ci,cj = to_move[counter]
                        counter += 1
                        ni,nj = di+ci,dj+cj
                        if (ni,nj) in to_move:
                            continue
                        if arr[ni][nj] == '#':
                            do_move = False
                            break
                        if arr[ni][nj] == '.':
                            continue

                        if arr[ni][nj] == '[':
                            to_move.extend([(ni,nj),(ni,nj+1)])
                        elif arr[ni][nj] == ']':
                            to_move.extend([(ni,nj),(ni,nj-1)])
                        else:
                            assert False

                    if do_move:
                        grid_copy = [list(row) for row in arr]
                        robot = (ri+di,rj+dj)
                        for rr,cc in to_move:
                            arr[rr][cc] = '.'
                        for rr,cc in to_move:
                            arr[rr+di][cc+dj] = grid_copy[rr][cc]

    #count boxes
    res = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == '[':
                res += 100 * i + j

    return res

def main():
    print("Hallo")
    print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()