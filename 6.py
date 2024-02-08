P_10_TABLE = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P_8_TABLE = [6, 3, 7, 4, 8, 5, 10, 9]
IP_TABLE = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
EP_TABLE = [4, 1, 2, 3, 2, 3, 4, 1]
P_4_TABLE = [2, 4, 3, 1]
def generate_subkeys(key):
  initial_key = [key[i - 1] for i in P_10_TABLE]

  left_half = initial_key[:5]
  right_half = initial_key[5:]

  # left circular shift
  left_half = left_half[1:] + left_half[:1]
  right_half = right_half[1:] + right_half[:1]

  combined_key = left_half + right_half

  subkey1 = [combined_key[i - 1] for i in P_8_TABLE]

  # left circular shift by 2
  left_half = left_half[2:] + left_half[:2]
  right_half = right_half[2:] + right_half[:2]

  combined_key = left_half + right_half
  subkey2 = [combined_key[i - 1] for i in P_8_TABLE]

  print(subkey1, subkey2)

generate_subkeys([1, 0, 1, 0, 0, 0, 0, 0, 0, 0])

print("6B\n6B\n6B")

sbox = [
    [[1, 0], [0, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 0], [1, 0]],
    [[0, 0], [0, 1], [1, 0], [0, 0]],
    [[0, 1], [1, 1], [1, 1], [0, 1]]
]

def xor(list1, list2):
    res = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            res.append(0)
        else:
            res.append(1)
    return res

def sbox_lookup(bits):
    row = int(bits[0] * 2 + bits[3])
    col = int(bits[1] * 2 + bits[2])
    return sbox[row][col]

def Fiestal(data, subkey):
    left_half = data[:4]
    right_half = data[4:]
    expanded_right_half = [right_half[i - 1] for i in EP_TABLE]
    xor1 = xor(subkey, expanded_right_half)
    sbox_output = sbox_lookup(xor1[:4]) + sbox_lookup(xor1[4:])
    p4_result = [sbox_output[i - 1] for i in P_4_TABLE]
    xor_2 = xor(p4_result, left_half)
    combined = xor_2 + right_half
    return combined

def key_gen(key):
    initial_key = [key[i - 1] for i in P_10_TABLE]
    left_half = initial_key[:5]
    right_half = initial_key[5:]
    left_half = left_half[1:] + left_half[:1]
    right_half = right_half[1:] + right_half[:1]
    combined_key = left_half + right_half
    subkey1 = [combined_key[i - 1] for i in P_8_TABLE]
    left_half = left_half[2:] + left_half[:2]
    right_half = right_half[2:] + right_half[:2]
    combined_key = left_half + right_half
    subkey2 = [combined_key[i - 1] for i in P_8_TABLE]
    return (subkey1, subkey2)

def sdes_enc(message, key):
    subkey1, subkey2 = key_gen(key)
    initial_permutation = [message[i - 1] for i in IP_TABLE]
    first_half = Fiestal(initial_permutation, subkey1)
    second_half = Fiestal(first_half[4:] + first_half[:4], subkey2)
    final_cipher_text = [second_half[i - 1] for i in IP_INVERSE]
    return final_cipher_text

plaintext = [1, 0, 0, 0, 0, 0, 0, 1]  # 8-bit plaintext
key = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  # 10-bit key

final_cipher_text = sdes_enc(plaintext, key)

def sdes_dec(cipher, key):
    subkey1, subkey2 = key_gen(key)
    initial_permutation = [cipher[i - 1] for i in IP_TABLE]
    first_half = Fiestal(initial_permutation, subkey2)
    second_half = Fiestal(first_half[4:] + first_half[:4], subkey1)
    message = [second_half[i - 1] for i in IP_INVERSE]
    print("Decrypted message: ", message)

sdes_dec(final_cipher_text, key)
