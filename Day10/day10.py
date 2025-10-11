def dayTen():
    with open("Day10/10_1.txt") as file:
        arr = []
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        n = 0
        for line in file:
            content = line.rstrip()
            if len(arr) == 0:
                n = len(content)+2
                arr.append('#'*n)
            arr.append('#'+content+'#')
        arr.append('#'*n)

    for a in arr:
        print(a)

    def dfs(i,j,num):
        if arr[i][j] == '#' or ( arr[i+1][j] != str(num+1) and arr[i-1][j] != str(num+1) and arr[i][j+1] != str(num+1) and arr[i][j-1] != str(num+1) ):
            return 0
        elif arr[i][j] == '9' and num == 9:
            return 1
        elif arr[i+1][j] == str(num+1):
            dfs(i+1,j,num+1)

        elif arr[i-1][j] == str(num+1):
            dfs(i-1,j,num+1)

        elif arr[i][j+1] == str(num+1):
            dfs(i,j+1,num+1)

        elif arr[i][j-1] == str(num+1):
            dfs(i,j-1,num+1)

        

        return dfs(i+1,j,num+1) + dfs(i-1,j,num+1) + dfs(i,j+1,num+1) + dfs(i,j-1,num+1)

    res = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if arr[i][j] == '0':
                res += dfs(i,j,0)

    return res

def dayTen2():
    pass

def main():
    print("Hallo")
    print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()