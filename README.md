# RSA-Algorithm
Implemented RSA Algorithm using GMP Library in Python <br />

Two types of RSA Algorithms have been implemented in this repository, the classic RSA and the dependent RSA. <br />
Classic RSA <br />
a. Choose two prime numbers p, q. <br />
b. Let n = p * q <br />
c. Let φ = (p − 1)(q − 1) <br />
d. Choose a large number e ∈ [2, φ − 1]that is coprime to φ. <br />
e. Compute d ∈ [2, φ − 1] such that e × d = 1 (mod φ) , and d must be coprime to φ <br />
f. (e, n) is the public key <br />
g. (d, n) is the private key <br />
  Encryption:<br />
     C = m^e (mod n)<br />
  Decryption:<br />
    m = C^d (mod n) <br />
    
Dependent RSA<br />
a. The key generation process is exactly as in the original RSA.<br />
b. Choose a random integer k in the residue class of Zn*<br />
c. Encryption: to obtain ciphertexts C1 C2 given a message M <br />
i. C1 = (k+1)^e mod n<br />
ii. C2 = m [k^e (mod n)]<br />

d. Decryption: <br />
i. k = (C1^d (mod n))-1 <br />
ii. M = C /[(k^e)(mod n)] <br />
