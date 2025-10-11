def dayTwo():
    with open("Day2/2_2.txt") as file:
        input = []
        for line in file:
            arr = line.rstrip('\n').split(' ')
            input.append([int(x) for x in arr])

        def isOrder(arr):
            desc,asc = 0,0
            for i in range(1,len(arr)):
                val = arr[i] - arr[i-1]
                if 1 <= val and val <= 3:
                    asc += 1
                elif -3 <= val and val <= -1:
                    desc += 1
                else:
                    break

            return max(desc+1,asc+1) == len(arr)     

        res = 0
        for report in input:
            if isOrder(report):
                res += 1
                    
    return res

def dayTwo2():
    with open("Day2/2_2.txt") as file:
        input = []
        for line in file:
            arr = line.rstrip('\n').split(' ')
            input.append([int(x) for x in arr])
        
        def isOrder(arr):
            desc,asc = 0,0
            for i in range(1,len(arr)):
                val = arr[i] - arr[i-1]
                if 1 <= val and val <= 3:
                    asc += 1
                elif -3 <= val and val <= -1:
                    desc += 1
                else:
                    break

            return max(desc+1,asc+1) == len(arr)

        res = 0
        for report in input:
            if isOrder(report):
                res += 1
            else:
                for i in range(len(report)):
                    temp = report[::]
                    temp.pop(i)
                    if isOrder(temp):
                        res += 1
                        break

    return res

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()