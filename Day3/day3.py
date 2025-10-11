def dayThree():
    res = 0
    word = ""
    num1 = ""
    num2 = ""
    read = 1
    with open("Day3/3_2.txt") as file:
        while 1:
            char = file.read(1)
            if not char:
                break
            else:
                if word == "" and char == 'm':
                    word += char
                elif word == "m" and char == 'u':
                    word += char
                elif word == "mu" and char == 'l':
                    word += char
                elif word == "mul" and char == '(':
                    word += char
                elif word == "mul(":
                    if read == 1 and char.isnumeric() and len(num1) < 3:
                        num1 += char
                    elif read == 1 and char == ',':
                        read = 2
                    elif read == 2 and char.isnumeric() and len(num2) < 3:
                        num2 += char
                    elif read == 2 and char == ')':
                        res += int(num1)*int(num2)
                        read = 1
                        word=num1=num2= ""
                    else:
                        read = 1
                        word=num1=num2= ""
                else:
                    read = 1
                    word=num1=num2= ""

    return res

def dayThree2():
    res = 0
    word = ""
    doword = ""
    num1 = ""
    num2 = ""
    read = 1
    active = True
    with open("Day3/3_2.txt") as file:
        while 1:
            char = file.read(1)
            if not char:
                break
            else:
                #do() and don't()
                if doword == "" and char == 'd':
                    doword += char
                elif doword == "d" and char == 'o':
                    doword += char
                elif doword == "do" and char == '(':
                    doword += char
                elif doword == "do(" and char == ')':
                    active = True
                    doword = ""
                elif doword == "do" and char == 'n':
                    doword += char
                elif doword == "don" and char == "'":    
                    doword += char
                elif doword == "don'" and char == 't':
                    doword += char
                elif doword == "don't" and char == "(":   
                    doword += char
                elif doword == "don't(" and char == ")":
                    active = False
                    doword = ""

                elif active == True:
                    doword = ""
                    if word == "" and char == 'm':
                        word += char
                    elif word == "m" and char == 'u':
                        word += char
                    elif word == "mu" and char == 'l':
                        word += char
                    elif word == "mul" and char == '(':
                        word += char
                    elif word == "mul(":
                        if read == 1 and char.isnumeric() and len(num1) < 3:
                            num1 += char
                        elif read == 1 and char == ',':
                            read = 2
                        elif read == 2 and char.isnumeric() and len(num2) < 3:
                            num2 += char
                        elif read == 2 and char == ')':
                            res += int(num1)*int(num2)
                            read = 1
                            word=num1=num2= ""
                        else:
                            read = 1
                            word=num1=num2= ""
                    else:
                        read = 1
                        word=num1=num2= ""
    return res

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()