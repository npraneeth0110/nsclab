cipher = str(input("Enter cipher text: "))
shift = int(input("Enter a shift value: "))

def caeser_dec(cipher, shift):
    result = ""
    cipher = cipher.upper()
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in cipher:
        if char in ALPHABET:
            result += ALPHABET[(ALPHABET.index(char)-shift)%26]
        else:
            result += char
    print(result)

caeser_dec(cipher, shift)

print("**************************************************************")

def det_matrix(matrix):
        return (matrix[0][0] * matrix[0][1] - matrix[1][0] * matrix[1][1])

def inv_matrix(matrix):
    det = det_matrix(matrix)
    if(det==0):
        print("No Inverse possible")
        return
    inv_det = 1/det
    print("Det: ",det)
    print("Inv_det: ", inv_det)
    inv = [
        [(matrix[1][1]*inv_det)%26, (-matrix[1][0]*inv_det)%26,
         (-matrix[0][1]*inv_det)%26, (matrix[0][0]*inv_det)%26]
    ]

    print("Inverse: ", inv)
    
matrix = [[1,2],[3,4]]
inv_matrix(matrix)