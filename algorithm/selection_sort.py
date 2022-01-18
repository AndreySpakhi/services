def findsmallest(arr):
    smallest = arr[0]
    smallestindex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestindex = i
    return smallestindex


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selection_sort([5, 3, 6, 2, 10]))

