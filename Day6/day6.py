
def daySix():
    with open("Day6/6_2.txt") as file:
        arr = []
        n = 0
        i = 0
        dir = [(-1,0),(0,1),(1,0),(0,-1)]
        vdir = 0
        pos = (0,0)

        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                n = len(content)+2
                arr.append('0'*n)
            arr.append('0'+content+'0')

            if  '^' in content:
                pos = (i+1,content.index('^')+1)
                vdir = 0
            elif '>' in content:
                pos = (i+1,content.index('>')+1)
                vdir = 1
            elif 'v' in content:
                pos = (i+1,content.index('v')+1)
                vdir = 2
            elif '<' in content:
                pos = (i+1,content.index('<')+1)
                vdir = 3
            i += 1
        arr.append('0'*n)

        res = 0
        visited = set()
        while arr[pos[0]][pos[1]] != '0':

            nextPos = (pos[0]+dir[vdir][0],pos[1]+dir[vdir][1])
            element = arr[nextPos[0]][nextPos[1]]
            if element == '#':
                if vdir == 3:
                    vdir = 0
                else:
                    vdir += 1
            else:
                if pos not in visited:
                    visited.add(pos)
                    res += 1
                pos = nextPos
        return res

def daySix2():
    with open("Day6/6_2.txt") as file:
        arr = []
        n = 0
        i = 0
        dir = [(-1,0),(0,1),(1,0),(0,-1)]
        vdir = 0
        pos = (0,0)

        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                n = len(content)+2
                arr.append('0'*n)
            arr.append('0'+content+'0')

            if  '^' in content:
                pos = (i+1,content.index('^')+1)
                vdir = 0
            elif '>' in content:
                pos = (i+1,content.index('>')+1)
                vdir = 1
            elif 'v' in content:
                pos = (i+1,content.index('v')+1)
                vdir = 2
            elif '<' in content:
                pos = (i+1,content.index('<')+1)
                vdir = 3
            i += 1
        arr.append('0'*n)

        start = (pos,vdir)
        visited = set()
        while arr[pos[0]][pos[1]] != '0':

            nextPos = (pos[0]+dir[vdir][0],pos[1]+dir[vdir][1])
            element = arr[nextPos[0]][nextPos[1]]
            if element == '#':
                if vdir == 3:
                    vdir = 0
                else:
                    vdir += 1
            else:
                if pos not in visited:
                    visited.add(pos)
                pos = nextPos
        
        res = 0
        for a,b in visited:
            v = list(arr[a])
            v[b] = '#'
            arr[a] = "".join(v)

            pos = start[0]
            vdir = start[1]
            vanddir = set()

            loop = False
            while arr[pos[0]][pos[1]] != '0' and loop == False:
                nextPos = (pos[0]+dir[vdir][0],pos[1]+dir[vdir][1])
                element = arr[nextPos[0]][nextPos[1]]
                if element == '#':
                    if vdir == 3:
                        vdir = 0
                    else:
                        vdir += 1
                else:
                    if (pos,vdir) not in vanddir:
                        vanddir.add( (pos,vdir) )
                    else:
                        loop = True
                    pos = nextPos

            if loop == True:
                res += 1
                loop = False

            v = list(arr[a])
            v[b] = '.'
            arr[a] = "".join(v)
        return res

def main():
    print("Hallo")
    print(daySix(), "ist die Lösung von Teil 1")
    print(daySix2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()