def partition(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    leftMost = arr[:mid]
    rightMost = arr[mid:]

    leftSorted = partition(leftMost)
    rightSorted = partition(rightMost)

    return merge(leftSorted, rightSorted)

def merge(arr1, arr2):
    i = j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):
        arr.append(min(arr1[i], arr2[j]))
        if arr1[i] < arr2[j]: i+=1
        else: j+=1
    
    while i < len(arr1):
        arr.append(arr1[i])
        i+=1
    
    while j < len(arr2):
        arr.append(arr2[j])
        j+=1

    return arr

if __name__ == '__main__':
    f = open(r'C:\Users\sabbi\OneDrive\Desktop\lab2\input3.txt', 'r')
    n = int(f.readline())
    arr = [int(x) for x in f.readline().split()]
    arr = partition(arr)
    print(arr)

