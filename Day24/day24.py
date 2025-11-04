from collections import defaultdict, deque
from typing import *

def dayTwentyfour():
    d = defaultdict(int)
    rules = deque([])
    #read
    firstMode = True
    with open("Day24/24_2.txt", 'r') as file:
        for line in file:
            if line == '\n':
                firstMode = False
                continue

            if firstMode:
                k,v = line.rstrip().split(': ')
                d[k] = int(v)
            else:
                l,r = line.rstrip().split(' -> ')
                f,op,s = l.split(' ')
                if f in d.keys() and s in d.keys():
                    if op == "AND":
                        d[r] = d[f] & d[s]
                    elif op == "XOR":
                        d[r] = d[f] ^ d[s]
                    elif op == "OR":
                        d[r] = d[f] | d[s]
                else:
                    rules.append( [l,r] )

    while rules:
        l,r = rules.popleft()
        f,op,s = l.split(' ')
        if f in d.keys() and s in d.keys():
            if op == "AND":
                d[r] = d[f] & d[s]
            elif op == "XOR":
                d[r] = d[f] ^ d[s]
            elif op == "OR":
                d[r] = d[f] | d[s]
        else:
            rules.append( [l,r] )

    d = dict(sorted(d.items()))
    res = ""
    for k,v in d.items():
        if k[0] == 'z':
            res += str(v)

    return int(res[::-1],2)

def dayTwentyfour2():
    d = defaultdict(tuple)
    #read
    firstMode = True
    with open("Day24/24_2.txt", 'r') as file:
        for line in file:
            if line == '\n':
                firstMode = False
                continue

            if not firstMode:
                l,r = line.rstrip().split(' -> ')
                f,op,s = l.split(' ')
                d[r] = (op,f,s)

    def make_wire(char,num):
        return char + str(num).rjust(2,"0")

    def verify_z(wire,num):
        if wire not in d: return False
        op,x,y = d[wire]
        if op != "XOR": return False
        if num == 0: return sorted([x,y]) == ["x00", "y00"]
        return verify_intermediate_xor(x,num) and verify_carry_bit(y,num) or verify_intermediate_xor(y,num) and verify_carry_bit(x,num)
    
    def verify_intermediate_xor(wire,num):
        if wire not in d: return False
        op,x,y = d[wire]
        if op != "XOR": return False
        return sorted([x,y]) == [make_wire("x",num), make_wire("y",num)]

    def verify_carry_bit(wire,num):
        if wire not in d: return False
        op,x,y = d[wire]
        if num == 1:
            if op != "AND": return False
            return sorted([x,y]) == ["x00","y00"]
        if op != "OR": return False
        return verify_direct_carry(x,num-1) and verify_recarry(y,num-1) or verify_direct_carry(y,num-1) and verify_recarry(x,num-1)
    
    def verify_direct_carry(wire,num):
        if wire not in d: return False
        op,x,y = d[wire]
        if op != "AND": return False
        return sorted([x,y]) == [make_wire("x",num), make_wire("y",num)]

    def verify_recarry(wire,num):
        if wire not in d: return False
        op,x,y = d[wire]
        if op != "AND": return False
        return verify_intermediate_xor(x,num) and verify_carry_bit(y,num) or verify_intermediate_xor(y,num) and verify_carry_bit(x,num)

    def verify(num):
        return verify_z(make_wire("z",num),num)

    def progress():
        i = 0
        while True:
            if not verify(i): break
            i += 1
        return i

    swaps = []
    for _ in range(4):
        baseline = progress()
        for x in d:
            for y in d:
                if x==y:continue
                d[x],d[y] = d[y],d[x]
                if progress() > baseline:
                    break
                d[x],d[y] = d[y],d[x]
            else:
                continue
            break
        swaps += [x,y]
    return ','.join(sorted(swaps))

def main():
    print("Hallo")
    print(dayTwentyfour(), "ist die Lösung von Teil 1")
    print(dayTwentyfour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()