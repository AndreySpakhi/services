def recursion(x):
    if x <= 1:
        return 1
    else:
        return x * recursion(x - 1)


def main():
    user_input = int(input('Enter number for recursion calculation '))
    print(recursion(user_input))


if __name__ == '__main__':
    main()