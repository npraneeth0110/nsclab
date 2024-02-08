p = 7
q = 11
e = 7

n = p * q

phi = (p - 1) * (q - 1)

def encrypt(message):
  cipher = (message**e) % n
  print(cipher)

message = int(input("Enter your message: "))

encrypt(message)