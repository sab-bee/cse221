def bubbleSort(arr, n):
  flag = False
  for i in range(n):
    for j in range(n):
      if arr[j+1] < arr[j]:
        flag = True
        arr[j], arr[j+1] = arr[j+1], arr[j]
    
    if flag == False:
      return

if __name__ == '__main__':
  f1 = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\input2.txt', 'r')
  f2 = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\output2.txt', 'w')

  l = int(f1.readline()) - 1
  arr = [int(x) for x in f1.readline().split()]

  bubbleSort(arr, l)
  for i in arr:
    f2.write(str(i) + ' ')