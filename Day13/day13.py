from sympy import *

def dayThirteen():
    tokens = 0
    with open("Day13/13_1.txt") as file:
        fLine = []
        sLine = []
        counter = 0
        for line in file:
            if line.strip():
                if counter < 2:
                    content = line.rstrip().split(' ')
                    fLine.append(int(content[2][2:-1]))
                    sLine.append(int(content[3][2:]))
                else:
                    content = line.rstrip().split(' ')
                    fLine.append(int(content[1][2:-1]))
                    sLine.append(int(content[2][2:]))

                counter += 1
                if counter == 3:
                    x, y = symbols('x,y')
                    eq1 = Eq( fLine[0]*x+fLine[1]*y, fLine[2])
                    eq2 = Eq( sLine[0]*x+sLine[1]*y, sLine[2])
                    res = solve((eq1, eq2), (x, y))
                    if res[x] <= 100 and res[y] <= 100 and res[x] == int(res[x]) and res[y] == int(res[y]):
                        tokens += res[x]*3 + res[y]*1

                    #processed
                    fLine = []
                    sLine = []
                    counter = 0
    return tokens

def dayThirteen2():
    tokens = 0
    with open("Day13/13_2.txt") as file:
        fLine = []
        sLine = []
        counter = 0
        for line in file:
            if line.strip():
                if counter < 2:
                    content = line.rstrip().split(' ')
                    fLine.append(int(content[2][2:-1]))
                    sLine.append(int(content[3][2:]))
                else:
                    content = line.rstrip().split(' ')
                    fLine.append(int(content[1][2:-1]) + 10000000000000 )
                    sLine.append(int(content[2][2:]) + 10000000000000 )

                counter += 1
                if counter == 3:
                    x, y = symbols('x,y')
                    eq1 = Eq( fLine[0]*x+fLine[1]*y, fLine[2])
                    eq2 = Eq( sLine[0]*x+sLine[1]*y, sLine[2])
                    res = solve((eq1, eq2), (x, y))
                    if res[x] == int(res[x]) and res[y] == int(res[y]):
                        tokens += res[x]*3 + res[y]*1

                    #processed
                    fLine = []
                    sLine = []
                    counter = 0
    return tokens

def main():
    print("Hallo")
    print(dayThirteen(), "ist die Lösung von Teil 1")
    print(dayThirteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()