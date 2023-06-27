### task - 1

in oder to find the sum from the array of two element used 2 different approach.

1. nested loop
2. binary search

```py
while i < len:
    j = 0
    while j < i:
        s = arr[i] + arr[j]
        if s == sum:
            return j,i
        j += 1
    i+= 1
```

this is the code for O(n²) time complexity

```py

arr = sorted(arr)
    while i < len:
        n1 = sum - arr[i]
        index = binarySearch(arr, 0, len, n1)
        if arr[index] == n1:
            return i, index
        i+=1
```

- first we sort the array using built in sort functino
- loop through the whole array
- pick each element, subtract it from the expected sum
- now find the subtraction result using binary search

### task - 2

merging two array in a sorted manner

```py
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
```

- loop through both array from start to finish using `i` and `j` pointer
- append the minimum to another array and if minimum in `arr1` increase `i`. other wise increase `j`
- finally loop individually both array to append the already sorted left out elements

### task - 3

merge sort
```py
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    leftMost = arr[:mid]
    rightMost = arr[mid:]

    leftSorted = partition(leftMost)
    rightSorted = partition(rightMost)

    return merge(leftSorted, rightSorted)
```
above code is `partition` function.

- `leftMost` variable has the value upto middle element
- `rightMost` variable has the value after middle upto n-1 index
- `partition` function returns a single array after sorting and merging two different array. [merge function at task3]
- `leftSorted` variable has sorted array of its two children array
- `rightSorted` has sorted array of its two children array
- again returning recusive merge function call for next 2 arrays

### task - 4
finding the max element using devide and conquer approach. main arr will be devided into two sub arrays
```py
def findMax(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    mid = n // 2
    leftMax = findMax(arr[:mid])
    rightMax = findMax(arr[mid:])
    return max(leftMax, rightMax)
```

|index|0|1|2|3|4|5|6
|-|-|-|-|-|-|-|-|
|numbers|5|15|2|3|10|1|9


*recursive calls*
```
leftMax = [5, 15, 2, 3]
rightMax = [10, 1, 9]
```
```
leftMax = [5, 15]
rightMax = [2, 3]
```
```
leftMax = [5]
rightMax = [15]
```
```
leftMax = [2]
rightMax = [3]
```
```
leftMax = [10, 1]
rightMax = [9]
```
```
leftMax = [10]
rightMax = [1]
```
```
rightMax = [9]
```

*backtracking*

- max(5, 15) -> 15
- max(2, 3) -> 3
- max(15, 3) -> 15
- max(10, 1) -> 10
- max(10, 9) -> 10
- max(15, 10) -> 15

time complexity of the code is `O(logN)`. creating sub array although takes `N` time. however, for a large input the constant factor becomes negligible which makes it `O(logN)` complexity.