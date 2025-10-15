from typing import *

def dayFourteen():
    arr = []

    #create field
    width = 101
    height = 103

    for _ in range(height):
        arr.append(['.']*width)
    
    #read robots
    robots = []
    with open("Day14/14_2.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(' ')
            x,y = l[2:].split(',')
            v1,v2 = r[2:].split(',')
            robots.append( { "pos": [int(x),int(y)], "v": [int(v1),int(v2)] } )

    #intial state
    for r in robots:
        x,y = r["pos"]

        if arr[y][x] == '.':
            arr[y][x] = '1'
        else:
            arr[y][x] = str((int(arr[y][x])) + 1)

    '''
    print("Initial state:")
    for a in arr:
        a = ''.join(a)
        print(a)
    '''

    #i = seconds
    time = 100
    for i in range(1,time+1):
        
        for r in robots:
            x,y = r["pos"]

            #clean up
            if arr[y][x] == '1':
                arr[y][x] = '.'
            else:
                arr[y][x] = str((int(arr[y][x])) - 1)

            v1,v2 = r["v"]
            x += v1
            y += v2

            #check borders
            if x < 0 or x > width-1 or y < 0 or y > height-1:
                x = x%width
                y = y%height

            #set new
            if arr[y][x] == '.':
                arr[y][x] = '1'
            else:
                arr[y][x] = str((int(arr[y][x])) + 1)

            r["pos"] = [x,y]

        '''
        if i == 1:
            print(f"After {i} second:")
        else:
            print(f"After {i} seconds:")

        for a in arr:
            a = ''.join(a)
            print(a)
        '''

    #count quadrants
    #left
    q1,q2 = 0,0
    for i in range(width//2):
        h = height//2
        for j in range(height):
            if j == h:
                continue
            elif j < h:
                if arr[j][i] != '.':
                    q1 += int(arr[j][i])
            else:
                if arr[j][i] != '.':
                    q2 += int(arr[j][i])

    #right
    q3,q4 = 0,0
    for i in range(width//2+1, width):
        h = height//2
        for j in range(height):
            if j == h:
                continue
            elif j < h:
                if arr[j][i] != '.':
                    q3 += int(arr[j][i])
            else:
                if arr[j][i] != '.':
                    q4 += int(arr[j][i])

    return q1*q2*q3*q4

def dayFourteen2():
    arr = []

    #create field
    width = 101
    height = 103

    for _ in range(height):
        arr.append(['.']*width)
    
    #read robots
    robots = []
    with open("Day14/14_2.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(' ')
            x,y = l[2:].split(',')
            v1,v2 = r[2:].split(',')
            robots.append( { "pos": [int(x),int(y)], "v": [int(v1),int(v2)] } )

    #intial state
    for r in robots:
        x,y = r["pos"]

        if arr[y][x] == '.':
            arr[y][x] = '1'
        else:
            arr[y][x] = str( int(arr[y][x]) + 1 )

    min_sf = float('inf')
    best_i = 0
    for second in range(1,width*height):

        for r in robots:
            x,y = r["pos"]

            #clean up
            if arr[y][x] == '1':
                arr[y][x] = '.'
            else:
                arr[y][x] = str( int(arr[y][x]) - 1 )

            v1,v2 = r["v"]
            x += v1
            y += v2

            #check borders
            if x < 0 or x > width-1 or y < 0 or y > height-1:
                x = x%width
                y = y%height

            #set new
            if arr[y][x] == '.':
                arr[y][x] = '1'
            else:
                arr[y][x] = str( int(arr[y][x]) + 1 )

            r["pos"] = [x,y]

        #count quadrants
        #left
        q1,q2 = 0,0
        for i in range(width//2):
            h = height//2
            for j in range(height):
                if j == h:
                    continue
                elif j < h:
                    if arr[j][i] != '.':
                        q1 += int(arr[j][i])
                else:
                    if arr[j][i] != '.':
                        q2 += int(arr[j][i])

        #right
        q3,q4 = 0,0
        for i in range(width//2+1, width):
            h = height//2
            for j in range(height):
                if j == h:
                    continue
                elif j < h:
                    if arr[j][i] != '.':
                        q3 += int(arr[j][i])
                else:
                    if arr[j][i] != '.':
                        q4 += int(arr[j][i])

        sf = q1*q2*q3*q4

        if sf < min_sf:
            min_sf = sf
            best_i = second

        '''
        if second == 8258:
            for a in arr:
                print(''.join(a))
        '''

    return best_i
    
def main():
    print("Hallo")
    print(dayFourteen(), "ist die Lösung von Teil 1")
    print(dayFourteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()