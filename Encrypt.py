import gmpy2
from gmpy2 import mpz
p=input("enter p") #input a prime number (len(p))<=10^18, p>=3
q=input("enter q") #input a prime number (len(q))<=10^18, q>p
m=input("enter m") #The string to be encrypted
n=gmpy2.mul(mpz(p),mpz(q)) #product of p, q
phi=gmpy2.mul(mpz(mpz(p)-1),mpz(mpz(q)-1)) #product of p-1 and q-1
m=mpz(m)
e=gmpy2.next_prime(mpz(gmpy2.f_div(phi,2))) #divide phi by 2, then find the next prime
# e=mpz(2)
# e=next_prime(mpz(q))

# while (e<phi):
# 	if (phi%e!=0):
# 		break
# 	else:
# 		e=gmpy2.next_prime(e)

d=mpz(gmpy2.invert(e,phi)) # e*d=1modphi, therefore calculate d which is the secret key
# c=mpz((mpz(mpz(m))**e)%mpz(n))
c=mpz(gmpy2.powmod(m,e,n)) # c is the encrypted value.
# m_d=mpz((mpz(mpz(c))**d)%mpz(n))
# m_d=gmpy2.powmod(c,d,n)
# print (m_d)
print (c)
print (e)
print (d)
print (n)