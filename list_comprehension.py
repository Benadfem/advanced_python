def main():
    # This program test the usage of list comprehension
    numbers = [n for n in range(1, 11) if n % 3 == 0]
    print(numbers)

if __name__ == '__main__':
    main()