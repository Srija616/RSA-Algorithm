import gmpy2
from gmpy2 import mpz
p=input() #input a prime number (len(p))<=10^18, p>=3
q=input() #input a prime number (len(q))<=10^18, q>p
m=input() #enter the message to be encrypted
n=gmpy2.mul(mpz(p),mpz(q));
phi=gmpy2.mul(mpz(gmpy2.add(mpz(p),-1)),mpz(gmpy2.add(mpz(q),-1)))   #phi=(p-1)*(q-1)

e=gmpy2.next_prime(mpz(q)) 
#(e*d)mod(phi)=1 ----> e*d=k*phi+1 for some k. This is what invert function of gmpy2 does.

k=11
k=mpz(k)
c1=gmpy2.powmod(gmpy2.add(k,1),e,n) #c1=(k+1)^e mod n
c2=gmpy2.mul(mpz(m), gmpy2.powmod(k,e,n)) #c2=k^e mods= n

d=mpz(gmpy2.invert(e,phi)) #e*d=1mod(phi)
print (c1)
print (c2)
print (k)
print (e)
print (d)
print (n)