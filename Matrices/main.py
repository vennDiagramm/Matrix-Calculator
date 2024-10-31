import math
import numpy as np

# Ask for matrix A
def askMatrix_A():
    matrix_A_rows = int(input("Enter the number of rows for matrix A: "))
    matrix_A_columns = int(input("Enter the number of columns for matrix A: "))
    matrix_A = []
    print()

    # Input the entries for A
    print("Enter the entries row-wise for matrix A: ")
    for i in range(matrix_A_rows):
        row_A = []
        for j in range(matrix_A_columns):
            entry = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row_A.append(entry)
        matrix_A.append(row_A)
    return matrix_A

# Ask for matrix B
def askMatrix_B():
    matrix_B_rows = int(input("Enter the number of rows for matrix B: "))
    matrix_B_columns = int(input("Enter the number of columns for matrix B: "))
    matrix_B = []
    print()

    # Input the entries for B
    print("Enter the entries row-wise for matrix B: ")
    for i in range(matrix_B_rows):
        row_B = []
        for j in range(matrix_B_columns):
            entry = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row_B.append(entry)
        matrix_B.append(row_B)
    return matrix_B

# Multiplication
def multi(matrix_A, matrix_B):
    # Convert matrices to NumPy arrays
    np_matrix_A = np.array(matrix_A)
    np_matrix_B = np.array(matrix_B)
    # Conditional Check If Possible
    if np_matrix_A.shape[1] != np_matrix_B.shape[0]:
        print("Not Possible")
        return None
    else:
        result_matrix = np.dot(np_matrix_A, np_matrix_B)
        return result_matrix.tolist() 

def main():
    matrix_A = askMatrix_A()
    print()
    matrix_B = askMatrix_B()

    askUser = input("Would you like to perform an operation? (Y/N): ")

    if askUser.upper() == 'Y':
        op = input("What operation would you like to perform? (+, -, * /): ")

        if op in ["+", "-"]:
            # Addition and Subtraction code
            A = matrix_A
            B = matrix_B
            if len(A) != len(B) or len(A[0]) != len(B[0]):
                print("Not Possible")
            else:
                # Perform matrix addition or subtraction based on user input
                result_matrix = {}
                for i in range(len(A)):
                    for j in range(len(A[0])):
                        result_matrix[(i+1, j+1)] = A[i][j] + B[i][j] if op == "+" else A[i][j] - B[i][j]
                      
                # For users to see the matrices
                print("\nMatrix A: ")
                for row_A in A:
                    print(row_A)
                print("\nMatrix B: ")
                for row_B in B:
                    print(row_B)
                  
                # Display the result matrix
                print("\nMatrix Result:")
                for i in range(len(A)):
                    for j in range(len(A[0])):
                        print(result_matrix[(i+1, j+1)], end=" ")
                    print()

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


# References:
# https://allinpython.com/matrix-multiplication-in-python-with-user-input/
# https://www.javatpoint.com/python-matrix
# https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/
# https://www.javatpoint.com/how-to-take-matrix-input-from-user-in-python
# https://www.programiz.com/python-programming/matrix