from typing import *

def daySeventeen():
    #read
    arr:List[int] = []
    reg = []
    first = True
    with open("Day17/17_2.txt") as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            
            line = line.rstrip()
            if first:
                t = line.split(": ")
                reg.append(int(t[1]))
            else:
                t = line[9:].split(',')
                arr = [int(x) for x in t]

    def combo(val:int) -> int:
        if 0 <= val <= 3:
            return val
        elif val == 4:
            return reg[0]
        elif val == 5:
            return reg[1]
        elif val == 6:
            return reg[2]
        elif val == 7:
            assert False
        else:
            return val

    def opcode0(operand:int) -> None:
        numerator = reg[0]
        denominator = 2**(combo(operand))
        reg[0] = numerator//denominator

    def opcode1(operand:int) -> None:
        reg[1] = reg[1]^operand

    def opcode2(operand:int) -> None:
        reg[1] = combo(operand)%8

    def opcode3(operand:int) -> int:
        if reg[0] != 0:
            return operand
        return -1

    def opcode4(operand:int) -> None:
        reg[1] = reg[1]^reg[2]

    def opcode5(operand:int) -> int:
        return combo(operand)%8

    def opcode6(operand:int) -> None:
        numerator = reg[0]
        denominator = 2**(combo(operand))
        reg[1] = numerator//denominator

    def opcode7(operand:int) -> None:
        numerator = reg[0]
        denominator = 2**(combo(operand))
        reg[2] = numerator//denominator

    #opcode,operand
    output = ""
    ip = 1
    while ip < len(arr):
        opcode = arr[ip-1]
        operand = arr[ip]
        if opcode == 0:
            opcode0(operand)
        elif opcode == 1:
            opcode1(operand)
        elif opcode == 2:
            opcode2(operand)
        elif opcode == 3:
            v = opcode3(operand)
            if v >= 0:
                ip = v-1
        elif opcode == 4:
            opcode4(operand)
        elif opcode == 5:
            output += str(opcode5(operand)) + ','
        elif opcode == 6:
            opcode6(operand)
        elif opcode == 7:
            opcode7(operand)
        ip += 2

    return output[:len(output)-1]

def daySeventeen2():
    #read
    arr:List[int] = []
    first = True

    with open("Day17/17_2.txt") as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            
            if not first:
                line = line.rstrip()
                expected = line[9:]
                t = expected.split(',')
                arr = [int(x) for x in t]


    def program(a:int,b:int=0,c:int=0):

        def combo(val:int) -> int:
            if 0 <= val <= 3:
                return val
            elif val == 4:
                return a
            elif val == 5:
                return b
            elif val == 6:
                return c
            else:
                assert False

        output = []
        ip = 0
        while ip < len(arr):
            opcode = arr[ip]
            operand = arr[ip + 1]
            match opcode:
                case 0:
                    a = a >> combo(operand)
                case 1:
                    b = b ^ operand
                case 2:
                    b = combo(operand) % 8
                case 3:
                    if a != 0:
                        ip = operand
                        continue
                case 4:
                    b = b ^ c
                case 5:
                    output.append(combo(operand) % 8)
                case 6:
                    b = a >> combo(operand)
                case 7:
                    c = a >> combo(operand)
            ip += 2
        return output

    candidates = [0]
    for l in range(len(arr)):
        next_can = []
        for val in candidates:
            for i in range(8):
                target = (val << 3) + i
                if program(target,0,0) == arr[-l-1:]:
                    next_can.append(target)
        candidates = next_can
    
    return min(candidates)
    
def main():
    print("Hallo")
    print(daySeventeen(), "ist die Lösung von Teil 1")
    print(daySeventeen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()