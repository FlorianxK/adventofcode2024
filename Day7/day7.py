
from collections import deque

def daySeven():
    with open("Day7/7.txt") as file:
        all = 0
        def rec(res,nums,tempres):
            if tempres == res and len(nums) < 1:
                return True
            if len(nums) < 1:
                return False
            else:
                if tempres == 0 and len(nums) >= 2:
                    f = nums.popleft()
                    s = nums.popleft()
                    return rec(res,nums.copy(),f+s) or rec(res,nums.copy(),f*s)
                else:
                    nxt = nums.popleft()
                    return rec(res,nums.copy(),tempres+nxt) or rec(res,nums.copy(),tempres*nxt)

        for line in file:
            content = line.rstrip()
            first = content.split(': ')
            second = first[1].split(' ')
            res = int(first[0])
            vals = deque([int(i) for i in second])
            match = rec(res,vals,0)
            if match:
                all += res
    return all

def daySeven2():
    with open("Day7/7.txt") as file:
        all = 0
        def rec(res,nums,tempres):
            if tempres == res and len(nums) < 1:
                return True
            if len(nums) < 1:
                return False
            else:
                if tempres == 0 and len(nums) >= 2:
                    f = nums.popleft()
                    s = nums.popleft()
                    return rec(res,nums.copy(),f+s) or rec(res,nums.copy(),f*s) or rec(res,nums.copy(),int(str(f)+str(s)))
                else:
                    nxt = nums.popleft()
                    return rec(res,nums.copy(),tempres+nxt) or rec(res,nums.copy(),tempres*nxt) or rec(res,nums.copy(),int(str(tempres)+str(nxt)))

        for line in file:
            content = line.rstrip()
            first = content.split(': ')
            second = first[1].split(' ')
            res = int(first[0])
            vals = deque([int(i) for i in second])
            match = rec(res,vals,0)
            if match:
                all += res
    return all

def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()