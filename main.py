print("Program to Implement DSA")

def sign_verification(HM, r, s):
    print("Value of (r,s):",r,s)
    w = pow(s, -1, q)
    u1 = (HM*w) % q
    u2 = (r*w) % q
    v = ((pow(g,u1) * pow(y,u2)) % p) % q
    print("(w, u1, u2, v) = ", (w, u1, u2, v))
    if v==r:
        print("signature is verified.")
    else:
        print("signature is not verified.")

p = int(input("Enter the value p:"))
q = int(input("Enter the value q:"))
h = int(input("Enter the value h:"))
x = int(input("Enter the private key x:"))
k = int(input("Enter the secret number k:"))
g = pow(h, int((p-1)/q), p)
y = pow(g, x, p)
print("Value of g, y:",(g, y))
HM1 = int(input("\nEnter the value of H(M1) to calculate (r,s):"))
r = (pow(g, k) % p) % q
s = int((pow(k,-1)*(HM1 + x*r)) % q)
sign_verification(HM1, r, s)
HM2 = int(input("\nEnter the value of H(M2) to calculate (r,s):"))
sign_verification(HM2, r, s)

