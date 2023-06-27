def merge(arr1, arr2, n1, n2):
    i = j = 0
    arr = []

    while i < n1 and j < n2:
        arr.append(min(arr1[i], arr2[j]))
        if arr1[i] < arr2[j]: i+=1
        else: j+=1
    
    while i < n1:
        arr.append(arr1[i])
        i+=1
    
    while j < n2:
        arr.append(arr2[j])
        j+=1

    return arr


if __name__ == '__main__':
    f = open(r'C:\Users\sabbi\OneDrive\Desktop\lab2\input2.txt', 'r')
    n1 = int(f.readline())
    arr1 = [int(x) for x in f.readline().split()]
    n2 = int(f.readline())
    arr2 = [int(x) for x in f.readline().split()]
    
    print(merge(arr1, arr2, n1, n2))