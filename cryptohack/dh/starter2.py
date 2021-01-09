p = 28151
g = 2 #find smallest g
found = False
while not found:
    for n in range(2,p):
        #if g^n mod p 1
        if pow(g,n,p) == 1:
            break
        if n == p-2:
            print (g)
            found = True
    g=g+1