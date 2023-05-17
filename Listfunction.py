def initialize():

    list = []

    for i in range(20):

        list.append(i)

    return list


def square(arr):

    list = []

    for i in range(len(arr)):

        list.append(arr[i] ** 2)

    return list


def halve(arr):

    list = []

    for i in range(len(arr)):

        list.append(arr[i] // 2)

    return list



def accumulate(arr):

    list = []
    sum = 0;
    for i in range(len(arr)):
        sum = sum + arr[i]
        list.append(sum)

    return list


def transpose(arr):
    list = []
    for i in range(0, len(arr)):
        if i == len(arr) - 1:
            break
        if i % 2 == 0:
            list.append(arr[i +1])
            list.append(arr[i])

    return list

def shift(arr):
    list = []
    i = 19;
    while i >= len(arr):
        list.append(arr[i])
        list.append(arr[i])



    return list


def reverse(arr):
    list = []
    i = len(arr) - 1
    while i >= 0:
        list.append(arr[i])
        i = i - 1

    return list









l = initialize()
print('INITIALIZE')
print(l)
print('HALVE')
print(halve(l))
print('SQUARE')
print(square(l))
print('ACCUMULATE')
print(accumulate(l))
print('TRANSPOSE')
print(transpose(l));
print('SHIFT')
print(shift(l));
print('REVERSE')
print(reverse(l));






print("Please select an option: ")
