import numpy
from sympy import Symbol, Derivative, Integral

#https://numpy.org/doc/stable/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace
def first():
    array = numpy.linspace(-1.3, 2.5, 64)
    print(array)

#https://numpy.org/doc/stable/reference/generated/numpy.tile.html?highlight=tile#numpy.tile
def second(n):
    cyclicArray = [1, 2, 3]
    array = numpy.tile(cyclicArray, 3 * n)
    print(array)

#https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange
def third():
    array = numpy.arange(20)
    array = [x for x in array if x % 2 != 0]
    print(array)

#https://numpy.org/doc/stable/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros
#https://numpy.org/doc/stable/reference/generated/numpy.pad.html?highlight=pad#numpy.pad
def fourth():
    #10x10 board of zeros
    #Create array of zeros first and then fill borders with ones
    array = numpy.zeros((10, 10))
    #Add border of ones
    array = numpy.pad(array, pad_width=1, mode='constant', constant_values=1)
    print(array)

#https://numpy.org/doc/stable/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros
def fifth():
    #Start with an 8x8 board of zeros
    array = numpy.zeros((8, 8))
    #Fill 2n-1 rows and columns with ones, starts from 0 and steps by 2
    array[::2, ::2] = 1
    #Fill 2n rows and columns with ones, starts from 1 and steps by 2
    array[1::2, 1::2] = 1
    print(array);

#https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html?highlight=fromfunction#numpy.fromfunction
def sixth(n):
    array = numpy.fromfunction(lambda i, j: i + j, (n, n), dtype=int)
    print (array)

#https://numpy.org/doc/stable/reference/generated/numpy.sum.html?highlight=sum#numpy.sum
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html#numpy.sum
def seventh():
    array = numpy.random.rand(3, 5)
    print(array, '\n')
    print('Sum: ', array.sum(), '\n')
    print('Row sums: ', array.sum(axis=1), '\n')
    print('Column sums:', array.sum(axis=0))

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html?highlight=argsort#numpy.argsort
def eigth():
    array = numpy.random.rand(5, 5)
    #Sort by second column, using slicing and indexing
    indexArray = array[:, 1].argsort()
    #Get array of values from index array
    sortedArray = array[indexArray]
    print('Original array: \n', array, '\n')
    print('Sorted array: \n', sortedArray)

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html?highlight=matrix#numpy.matrix
def ninth(matrixAsArray):
    matrix = numpy.matrix(matrixAsArray)
    inverseMatrix = matrix.I
    print('Original matrix:\n', matrix)
    print('Inversed matrix:\n', inverseMatrix)

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig
def tenth(matrixAsArray):
    values, vectors = numpy.linalg.eig(numpy.matrix(matrixAsArray))
    print('Matrix: ', matrixAsArray)
    print('Values: ', values)
    print('Vectors: ', vectors)

#https://www.geeksforgeeks.org/python-sympy-derivative-method/
def eleventh(function):
    x = Symbol('x')
    derivative = Derivative(function, x).doit()
    print('Function: ', function)
    print('Derivative: ', derivative)

#https://docs.sympy.org/latest/modules/integrals/integrals.html
def twelfth(function, start, end):
    x = Symbol('x')
    indefiniteIntegral = Integral(function, x).doit()
    definiteIntegral = Integral(function, (x, start, end)).doit()
    print('Function: ', function)
    print('Indefinite integral: ', indefiniteIntegral)
    print('Definite integral [', start, ', ', end, ']: ', definiteIntegral)

#Examples
if __name__ == '__main__':
    print("First task: \n")
    first()

    print("\nSecond task:")
    print("Enter n: ")
    n = int(input())
    print("\n")
    second(n)

    print("\nThird task: \n")
    third()

    print("\nForth task: \n")
    fourth()

    print("\nFifth task: \n")
    fifth()

    print("\nSixth task: \n")
    print("Enter n: ")
    n = int(input())
    print("\n")
    sixth(n)
    
    print("\nSeventh task: \n")
    seventh()

    print("\nEigth task: \n")
    eigth()

    print("\nNinth task: \n")
    matrixAsArray = [[1, 2], [3, 4], [4, 5], [6, 7], [8, 9]]
    ninth(matrixAsArray)

    print("\nTenth task: \n")
    matrixAsArray = [[1, 2], [3, 4]]
    tenth(matrixAsArray)

    print("\nEleventh task:")
    #print("Enter function: ")
    #function = input()
    #Example function, for input uncomment above
    function = 'x**2'
    eleventh(function)

    print("\nTwelth task:")
    #print("Enter function: ")
    #function = input()
    #print("Enter start: ")
    #start = int(input())
    #print("Enter start: ")
    #end = int(input())
    #Example function, for input uncomment above
    function = 'x**2'
    start = 1
    end = 2
    twelfth(function, start, end)
