from typing import DefaultDict

def dayEight():
    n,m = 0,0
    with open("Day8/8_2.txt") as file:
        arr = []
        d = DefaultDict(list)
        i,j = 0,0
        for line in file:
            content = line.rstrip()
            arr.append(content)

            for c in content:
                if c != '.':
                    d[c].append( (i,j) )
                j+=1

            if m == 0:
                m = j
            j = 0
            i+=1

        n = i

    setNodes = set()
    for v in d.values():
        for i in range(len(v)-1):
            for j in range(i+1,len(v)):
                diff_x = v[i][0]-v[j][0]
                diff_y = v[i][1]-v[j][1]
                anti1 = (v[i][0]+diff_x, v[i][1]+diff_y)
                anti2 = (v[j][0]-diff_x, v[j][1]-diff_y)

                if anti1 not in setNodes and anti1[0] >= 0 and anti1[0] < n and anti1[1] >= 0 and anti1[1] < m:
                    setNodes.add(anti1)
                if anti2 not in setNodes and anti2[0] >= 0 and anti2[0] < n and anti2[1] >= 0 and anti2[1] < m:
                    setNodes.add(anti2)

    return len(setNodes)

def dayEight2():
    n,m = 0,0
    with open("Day8/8_2.txt") as file:
        arr = []
        d = DefaultDict(list)
        i,j = 0,0
        for line in file:
            content = line.rstrip()
            arr.append(content)

            for c in content:
                if c != '.':
                    d[c].append( (i,j) )
                j+=1

            if m == 0:
                m = j
            j = 0
            i+=1

        n = i

    setNodes = set()
    for v in d.values():
        for i in range(len(v)-1):
            for j in range(i+1,len(v)):
                diff_x = v[i][0]-v[j][0]
                diff_y = v[i][1]-v[j][1]

                anti1 = (v[i][0], v[i][1])
                anti2 = (v[j][0], v[j][1])

                while anti1[0] >= 0 and anti1[0] < n and anti1[1] >= 0 and anti1[1] < m:
                    if anti1 not in setNodes:
                        setNodes.add(anti1)
                    anti1 = (anti1[0]+diff_x, anti1[1]+diff_y)
                
                while anti2[0] >= 0 and anti2[0] < n and anti2[1] >= 0 and anti2[1] < m:
                    if anti2 not in setNodes:
                        setNodes.add(anti2)
                    anti2 = (anti2[0]-diff_x, anti2[1]-diff_y)

    return len(setNodes)

def main():
    print("Hallo")
    print(dayEight(), "ist die Lösung von Teil 1")
    print(dayEight2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()