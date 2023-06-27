def bubbleSort(id, mark, n):
    flag = False
    for i in range(n-1):
        for j in range(n-1):
            if mark[j+1] > mark[j]:
                flag = True
                id[j], id[j+1] = id[j+1], id[j]
                mark[j], mark[j+1] = mark[j+1], mark[j]
            if mark[j+1] == mark[j]:
                if id[j+1] < id[j]:
                    id[j], id[j+1] = id[j+1], id[j]
                    mark[j], mark[j+1] = mark[j+1], mark[j]
        if flag == False:
            return
            
if __name__ == '__main__':
    inp = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\input3.txt', 'r')
    op = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\output3.txt', 'w')

    n = int(inp.readline())
    id = [int(x) for x in inp.readline().split()]
    mark = [int(x) for x in inp.readline().split()]

    bubbleSort(id, mark, n)

    for i in range(n):
        op.write(f'id: {id[i]} mark: {mark[i]} \n')