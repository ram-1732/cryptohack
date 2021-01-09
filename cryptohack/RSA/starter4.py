import gmpy 

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

#d*e mod phi(n)== 1
t = (p-1)*(q-1)

d= gmpy.invert(e,t)
print(d)