def binary_search(inputlist, item):
    low = 0
    high = len(inputlist) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if item == inputlist[mid]:
            return mid
        if item > inputlist[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


mylist = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(mylist, 2))