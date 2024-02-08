p=7
q=11
e=7

n = p*q
phi = (p-1)*(q-1)

print("e: ",e)

d = pow(e, -1, phi)

print("d: ",d)

def decrypt(cipher):
    msg = (cipher**d)%n
    print(msg)

cipher = int(input("Enter cipher number: "))

decrypt(cipher)