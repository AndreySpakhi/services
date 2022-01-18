def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        base = arr[0]
        less_base = [i for i in arr[1:] if i < base]
        great_base = [i for i in arr[1:] if i > base]
        return quick_sort(less_base) + [base] + quick_sort(great_base)


def main():
    user_input = [4, 2, 5, 1, 9, 8, 3]
    print(quick_sort(user_input))


if __name__ == '__main__':
    main()
