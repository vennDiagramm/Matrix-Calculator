import math
import numpy as np

# Ask for matrix A
def askMatrix_A():
  matrix_A_rows = int(input("Enter the number of rows for matrix A: "))
  matrix_A_columns = int(input("Enter the number of columns for matrix A: "))
  matrix_A = []

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
  # This was the problem -- Get the len
  matrix_A_rows, matrix_A_columns = len(matrix_A), len(matrix_A[0])
  matrix_B_rows, matrix_B_columns = len(matrix_B), len(matrix_B[0])

  if matrix_A_columns != matrix_B_rows:
      print("Not Possible")
      return None
  else:
      matrix_C = [[0] * matrix_B_columns for _ in range(matrix_A_rows)]

      for i in range(matrix_A_rows):
          for j in range(matrix_B_columns):
              for k in range(matrix_A_columns):
                  matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
      return matrix_C


def main():
  matrix_A = askMatrix_A()
  matrix_B = askMatrix_B()

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



# References:
# https://allinpython.com/matrix-multiplication-in-python-with-user-input/
# https://www.javatpoint.com/python-matrix
# https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/
# https://www.javatpoint.com/how-to-take-matrix-input-from-user-in-python
# https://www.programiz.com/python-programming/matrix