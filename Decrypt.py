import gmpy2
from gmpy2 import mpz
c=input() #enter the encrypted msg
d=input() #The secret key
n=input() #p*q
c=mpz(c)
d=mpz(d)
n=mpz(n)
m_d=gmpy2.powmod(c,d,n) #(c^d)mod n is the decrypted msg
print (m_d)