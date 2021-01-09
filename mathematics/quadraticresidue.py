
##initial data
p = 29
ints = [6,11,14]
##getting quadratic residue
quadres = [a for a in range(p) if pow(a,2,p)in ints]

print(f"{min(quadres)}")