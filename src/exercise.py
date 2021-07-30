def main():
    #write your code below this line
    n = int(input("Give a number:"))
    product = 1

    for i in range(1, n+1):
        product *= i

    print("Factorial: " + str(product))

if __name__ == '__main__':
    main()
