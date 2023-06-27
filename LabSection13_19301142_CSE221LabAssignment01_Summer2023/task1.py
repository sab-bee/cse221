
def A(nums):
    for num in nums:
        if int(num) % 2 == 0:
            f2.write(f'{num} is an Even number \n')
        else:
            f2.write(f'{num} is an Odd number \n')


import operator
def B(i, n):
    op = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
    }

    while i < n:
        arr = f1.readline().split()
        f2.write(f'the result of {arr[1]} {arr[2]} {arr[3]} is {op[arr[2]](int(arr[1]), int(arr[3]))}\n')
        i+=1


if __name__ == '__main__':
    f1 = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\input1a.txt', 'r')
    f2 = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\output1a.txt', 'w')
    nums = f1.read().splitlines()
    A(nums)

    f1 = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\input1b.txt', 'r')
    f2 = open(r'C:\Users\sabbi\OneDrive\Desktop\lab1\output1b.txt', 'w')
    n = int(f1.readline())
    B(0, n)