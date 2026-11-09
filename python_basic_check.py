
def main():
    #creating a list comprehension  of list
    board = [["_"] * 3 for _ in range(3)]
    print(board)
    print("\n")
    board[2][2] = "*"
    print(board)
    print("\n")


if __name__ == '__main__':
    main()