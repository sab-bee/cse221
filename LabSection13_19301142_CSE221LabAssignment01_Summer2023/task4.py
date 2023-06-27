def lexical(i, n):
    trains = []
    times = []
    locations = []
    while i < n:
        arr = inp.readline().split()
        trains.append(arr[0])
        locations.append(arr[-3])
        times.append(arr[-1])
        i+=1
    
    for i in range(n-1):
        for j in range(n-1):
            if trains[j+1] < trains[j]:
                trains[j] ,trains[j+1] = trains[j+1], trains[j]
                times[j] ,times[j+1] = times[j+1], times[j]
            if trains[j+1] == trains[j]:
                if times[j+1] > times[j]:
                    trains[j] ,trains[j+1] = trains[j+1], trains[j]
                    times[j] ,times[j+1] = times[j+1], times[j]

    for i in range(n):
        op.write(f'{trains[i]} will departure for {locations[i]} at {times[i]}\n')


if __name__ == '__main__':
    inp = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\input4.txt', 'r')
    op = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\output4.txt', 'w')

    n = int(inp.readline())
    lexical(0, n)