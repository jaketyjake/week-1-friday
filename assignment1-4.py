# print a pyramid of asterisks
levels = int(input("Enter the number of stacks you want your pyramid to have: "))

def pyramid(levels):
    for line in range(levels):
        print(f" " * (levels - line - 1) + "*" * (2 * line + 1))

pyramid(levels)

        


