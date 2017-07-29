#! python3
##sprawdzenie, czy macierz jest ortogonalna, idempotentna, inwolutywna.
import numpy as np
matrix=np.matrix(input("wprowadź macierz A w formacie 11 12 13; 21 22 23; 31 32 33: "))

print("A=\n", matrix)
#ortogonalna At*A=I
ortog=np.dot(np.transpose(matrix), matrix)
print("A^t*A=\n", ortog)
matrixTrue=ortog==np.identity(len(matrix))
#print(matrixTrue)
def statement(MType):
    if False not in matrixTrue:
        print ("Macierz JEST", str(MType))
    else:
        print ("Macierz NIE JEST", str(MType))
statement("ortogonalna")
#idempotentna A*A=A
ASquared=np.dot(matrix, matrix)
print("A*A=\n", ASquared)
matrixTrue=ASquared==matrix
statement("idempotentna")
#inwolutywna A*A=I
matrixTrue=ASquared==np.identity(len(matrix))
statement("inwolutywna")
