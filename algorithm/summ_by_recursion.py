def sum_by_recursion(x):
    if len(x) == 0:
        return 0
    else:
        return x[0] + sum_by_recursion(x[1:])


def main():
    user_input = [1, 2, 3, 4, 5, 6, 7]
    print(sum_by_recursion(user_input))


if __name__ == '__main__':
    main()
