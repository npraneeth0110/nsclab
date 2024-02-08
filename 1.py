text = str(input("Enter plain text: "))
shift = int(input("Enter a shift number: "))

def caesar_encryption(text, shift):
    result=""
    text = text.lower()
    for char in text:
        result += chr((ord(char)+shift-97)%26+97)
    print("Cipher Text: ",result)

caesar_encryption(text,shift)
 
print("******************************************************************")

matrix = [[2,3],[4,5]]

def determinant_of(matrix):
    determinant = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    print("Determinant : ", determinant % 26)
determinant_of(matrix)

def adjoint_of(matrix):
    adjoint = [[matrix[1][1]%26, -matrix[1][0]%26], [-matrix[0][1]%26], matrix[0][0]%26]
    print("Adjoint: ", adjoint)
adjoint_of(matrix)