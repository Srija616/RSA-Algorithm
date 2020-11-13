# RSA-Algorithm
Implemented RSA Algorithm using GMP Library in Python

Two types of RSA Algorithms have been implemented in this repository, the classic RSA and the dependent RSA.
Classic RSA
a. Choose two prime numbers p, q .
b. Let n = p * q
c. Let φ = (p − 1)(q − 1)
d. Choose a large number e ∈ [2, φ − 1]that is coprime to φ.
e. Compute d ∈ [2, φ − 1] such that e × d = 1 (mod φ) , and d must be coprime to φ
f. (e, n) is the public key
g. (d, n) is the private key
  Encryption:
     C = m^e (mod n)
  Decryption:
    m = C^d (mod n)
    
Dependent RSA
a. The key generation process is exactly as in the original RSA.
b. Choose a random integer k in the residue class of Zn*
c. Encryption: to obtain ciphertexts C1 C2 given a message M
i. C1 = (k+1)^e mod n
ii. C2 = m [k^e (mod n)]

d. Decryption: 
i. k = (C1^d (mod n))-1
ii. M = C /[(k^e)(mod n)]
