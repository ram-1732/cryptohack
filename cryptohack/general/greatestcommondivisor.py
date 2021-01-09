a = 66528
b = 52920
 
## getting gcd of a and b
def gcd(a,b):
    ## if a modulus b = 0 then return b
	if a%b == 0:
		return b
        ##return the gcd of b and a modulus b
	return gcd(b, a%b)

##main function
def main():
	a = 66528
	b = 52920
	print(gcd(a,b))

main()