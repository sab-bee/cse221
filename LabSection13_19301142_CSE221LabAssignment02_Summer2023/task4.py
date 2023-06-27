def findMax(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    mid = n // 2
    leftMax = findMax(arr[:mid])
    rightMax = findMax(arr[mid:])
    return max(leftMax, rightMax)
    

if __name__ == '__main__':
    f = open(r'C:\Users\sabbi\OneDrive\Desktop\lab2\input4.txt','r')
    n = int(f.readline())
    arr = [int(x) for x in f.readline().split()]
    print(findMax(arr))