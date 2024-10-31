import math
import numpy as np

def askMatrix_A():
    matrix_A_rows = int(input("Enter the number of rows for matrix A: "))
    matrix_A_columns = int(input("Enter the number of columns for matrix A: "))
    return matrix_A_rows, matrix_A_columns

def askMatrix_B():
    matrix_B_rows = int(input("Enter the number of rows for matrix B: "))
    matrix_B_columns = int(input("Enter the number of columns for matrix B: "))
    return matrix_B_rows, matrix_B_columns

def multi(matrix_A, matrix_B):
    matrix_A_rows, matrix_A_columns = matrix_A
    matrix_B_rows, matrix_B_columns = matrix_B

    if matrix_A_columns != matrix_B_rows:
        print("The number of columns in matrix A must be equal to the number of rows in matrix B")
        return None
    else:
        matrix_C = [[0 for _ in range(matrix_B_columns)] for _ in range(matrix_A_rows)]

        for i in range(matrix_A_rows):
            for j in range(matrix_B_columns):
                for k in range(matrix_A_columns):
                    matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
        return matrix_C

def main():
    matrix_A_rows, matrix_A_columns = askMatrix_A()
    print()
    matrix_B_rows, matrix_B_columns = askMatrix_B()
    print()

    # matrix A
    print("Enter the entries row-wise for matrix A: ")
    matrix_A = []
    for i in range(matrix_A_rows):
        row_A = []
        for j in range(matrix_A_columns):
            entry = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row_A.append(entry)
        matrix_A.append(row_A)
    print()

    # matrix B
    print("Enter the entries row-wise for matrix B: ")
    matrix_B = []
    for i in range(matrix_B_rows):
        row_B = []
        for j in range(matrix_B_columns):
            entry = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row_B.append(entry)
        matrix_B.append(row_B)
    print()

    askUser = input("Would you like to perform an operation? (Y/N): ")

    if askUser.upper() == 'Y':
        op = input("What operation would you like to perform? (+, -, * /): ")

        if op == "+":
            # To be followed
            pass
        elif op == "-":
            # To be followed
            pass

        # For multiplication
        elif op == "*":
            result_matrix = multi(matrix_A, matrix_B)

            if result_matrix:
                # For users to see the matrices
                print("\nMatrix A: ")
                for row_A in matrix_A:
                    print(row_A)
                print("\nMatrix B: ")
                for row_B in matrix_B:
                    print(row_B)

                # Print Product
                print("\nThe Product of the two matrices is: \n")
                for row_C in result_matrix:
                    print(row_C)

        elif op == "/":
            # To be followed
            pass
        else:
            print("Invalid operation")

    elif askUser.upper() == 'N':
        print("\nMatrix A: ")
        for row_A in matrix_A:
            print(row_A)

        print("\nMatrix B: ")
        for row_B in matrix_B:
            print(row_B)
        print("Thank you for using the program!")
    else:
        print("Wrong Command!")

if __name__ == "__main__":
    main()


#multipliaction
import math
import numpy as np

def multi():
    matrix_A_rows = int(input("Enter the number of rows for matrix A: "))
    matrix_A_columns = int(input("Enter the number of columns for matrix A: "))

    print()

    matrix_B_rows = int(input("Enter the number of rows for matrix B: "))
    matrix_B_columns = int(input("Enter the number of columns for matrix B: "))

    if matrix_A_columns != matrix_B_rows:
        print("The number of columns in matrix A must be equal to the number of rows in matrix B")
        return
    else:
        matrix_A = []
        matrix_B = []
        matrix_C = []
        print()

        # matrix A
        print("Enter the entries row-wise for matrix A: ")
        matrix_A = []
        for i in range(matrix_A_rows):
            row_A = []
            for j in range(matrix_A_columns):
                entry = int(input(f"Enter element at position ({i+1}, {j+1}): "))
                row_A.append(entry)
            matrix_A.append(row_A)
        print()

        # matrix B
        print("Enter the entries row-wise for matrix B: ")
        matrix_B = []
        for i in range(matrix_B_rows):
            row_B = []
            for j in range(matrix_B_columns):
                entry = int(input(f"Enter element at position ({i+1}, {j+1}): "))
                row_B.append(entry)
            matrix_B.append(row_B)
        print()

        # For users to see the matrices
        print("Matrix A: ")
        for mat_A in matrix_A:
            print(mat_A)

        print("\nMatrix B: ")
        for mat_B in matrix_B:
            print(mat_B)

        # matrix C // result
        for _ in range(matrix_A_rows):
            c = []
            for _ in range(matrix_B_columns):
                c.append(0)
            matrix_C.append(c)

        for i in range(matrix_A_rows):
            for j in range(matrix_B_columns):
                for k in range(matrix_A_columns):
                    matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]

        # For users to see the result
        print("\nThe Product of the two matrices is: \n", matrix_C)

multi()

