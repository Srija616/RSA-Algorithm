import gmpy2
from gmpy2 import mpz
c1=input()
c2=input()
e=input()
d=input()
n=input()
c1=mpz(c1)
c2=mpz(c2)
e=mpz(e)
d=mpz(d)
n=mpz(n)
m_k=mpz(mpz(gmpy2.powmod(c1,d,n))-1) # c1^d mod n
m_d=gmpy2.f_div(c2,gmpy2.powmod(m_k,e,n)) #c2/(m_k^e mod(n))
print (m_d)
print (m_k)
		