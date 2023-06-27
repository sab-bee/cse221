def findSumN2(arr, len, sum, i):
    while i < len:
        j = 0
        while j < i:
            s = arr[i] + arr[j]
            if s == sum:
                return j,i
            j += 1
        i+= 1
'''
time complexity - O(n^2)
below solution is for O(nlogN)
'''

def findSumNlog(arr, len, sum, i):
    arr = sorted(arr)

    while i < len:
        n1 = sum - arr[i]
        index = binarySearch(arr, 0, len, n1)
        if arr[index] == n1:
            return i, index
        i+=1

'''
using binary search on sorted array
'''
def binarySearch(arr, l, h, x):
    if h > l:
        mid = (h+l)//2
        midVal = arr[mid]
        if midVal == x:
            return mid
        elif midVal > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, h, x)
    else:
        return -1


if __name__ == '__main__':
    f = open(r'C:\Users\sabbi\OneDrive\Desktop\lab2\input1.txt', 'r')
    len, sum = [int(x) for x in f.readline().split()]
    arr = [int(x) for x in f.readline().split()]

    val = findSumNlog(arr, len, sum, 1)
    print(val)

    
    