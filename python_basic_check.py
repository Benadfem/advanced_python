
def main():
    # Handling 6 bytes Memory of array
    from array import array
#   create an array element
    octets = array ('B' , range(6))
    print(octets, "\n")
    m1 = memoryview(octets)
    m1.tolist()
    print(m1.tolist())
#   Now we create a new array that is 2 x 3 dimension
# this is done by casting m1
    m2 = m1.cast('B', [2,3])
    print(m2, "\n")
    print(m2.tolist())

if __name__ == '__main__':
    main()