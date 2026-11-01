def main():
    # for the creation of list of tuples
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple']
    sizes = ['small', 'medium', 'large']
    T_shirts = [(color,size)
                for color in colors
                for size in sizes
                if 'purple' in colors
                ]
    print(T_shirts)

if __name__ == '__main__':
    main()