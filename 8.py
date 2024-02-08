def decrypt_hill(cipher_text, key):
    A = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = cipher_text.lower()
    cipher = [A.index(char) for char in cipher_text]

    # Inverse of the key matrix
    determinant = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    inverse_determinant = pow(determinant, -1, 26)  # Using modular inverse
    inverse_key = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
    inverse_key = [[(inverse_determinant * element) % 26 for element in row] for row in inverse_key]

    # break the cipher text into pairs
    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]

    plain_text = []
    for pair in pairs:
        i = [(inverse_key[0][0] * pair[0] + inverse_key[0][1] * pair[1]) % 26,
             (inverse_key[1][0] * pair[0] + inverse_key[1][1] * pair[1]) % 26]
        plain_text += i

    print(plain_text)
    decrypted_text = "".join(A[num] for num in plain_text)
    print(decrypted_text)

decrypt_hill("FKMFIO", [[2,3],[3,6]])
