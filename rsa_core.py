# KEY GENERATION

!pip install pycryptodome
from Crypto.Util.number import getPrime
from math import gcd
import secrets

def generate_keys(key_size):

    # STEP 1: Generate bilangan prima p dan q

    p_bits = key_size // 2
    q_bits = key_size - p_bits

    p = getPrime(p_bits)
    q = getPrime(q_bits)

    while p == q:
        q = getPrime(q_bits)

    # STEP 2: Menghitung n

    n = p * q

    # STEP 3: Menghitung phi(n)

    phi = (p - 1) * (q - 1)

    # STEP 4: Menentukan public exponent (e)

    e = secrets.randbelow(phi - 2) + 2

    while gcd(e, phi) != 1:
        e = secrets.randbelow(phi - 2) + 2

    # STEP 5: Menentukan private exponent (d)

    d = pow(e, -1, phi)

    # STEP 6: Menampilkan hasil

    print("========== GENERATED KEYS ==========")

    print("\nGenerated p =", p)
    print("\nGenerated q =", q)
    print("\nCalculated n =", n)
    print("\nCalculated phi(n) =", phi)
    print("\nPublic exponent (e) =", e)
    print("\nPrivate exponent (d) =", d)

    print("\n========== PUBLIC KEY ==========")
    print("n =", n)
    print("e =", e)

    print("\n========== PRIVATE KEY ==========")
    print("n =", n)
    print("d =", d)

    print("\nKeys generated successfully!")

    # Mengembalikan hasil agar bisa digunakan fungsi lain
    return p, q, n, phi, e, d

key_size = 896

p, q, n, phi, e, d = generate_keys(key_size)

# ENKRIPSI 

# RSA ENCRYPTION (ASCII)

def enkripsi(pesan, public_key):

    # Mengambil public key
    n, e = public_key

    # Mengubah pesan menjadi kode ASCII
    data = pesan.encode("ascii")

    # Menyiapkan list untuk ciphertext
    ciphertext = []

    # Melakukan enkripsi setiap karakter
    for karakter in data:

        # Mengambil nilai ASCII
        M = karakter

        # Rumus enkripsi RSA
        C = pow(M, e, n)

        # Menyimpan hasil enkripsi
        ciphertext.append(C)

    return ciphertext

# MENGAMBIL PUBLIC KEY

public_key = (n, e)

# INPUT PLAINTEXT
pesan = input("Masukkan pesan: ")

# PROSES ENKRIPSI
ciphertext = enkripsi(pesan, public_key)

# MENAMPILKAN HASIL
print("\n========== ENCRYPTION RESULT ==========")

print("Plaintext Message =", pesan)

print("Public Key =", public_key)

print("\nCiphertext =")
print(ciphertext)

# DEKRIPSI (ASCII)

def dekripsi(ciphertext, private_key):

    # Mengambil private key
    n, d = private_key

    # Menyiapkan list hasil dekripsi
    hasil_dekripsi = []

    # Melakukan dekripsi setiap karakter
    for karakter in ciphertext:

        # Rumus dekripsi RSA
        M = pow(karakter, d, n)

        # Menyimpan hasil ASCII
        hasil_dekripsi.append(M)

    # Mengubah kode ASCII menjadi teks
    plaintext = bytes(hasil_dekripsi).decode("ascii")

    return plaintext
# MENGAMBIL PRIVATE KEY

private_key = (n, d)

# MENGAMBIL CIPHERTEXT DARI ENKRIPSI
encrypted_message = ciphertext

# PROSES DEKRIPSI
decrypted_message = dekripsi(encrypted_message, private_key)

# MENAMPILKAN HASIL

print("\n========== DECRYPTION RESULT ==========")

print("Current Private Key:")
print(private_key)

print("\nEncrypted Message to Decrypt:")
print(encrypted_message)

print("\nMessage decrypted successfully!")

print("\n========== DECRYPTED MESSAGE ==========")

print(decrypted_message)

# RSA VERIFICATION

print("\n========== VERIFICATION ==========")

if pesan == decrypted_message:

    print("Verification: Decryption Successful!")

    print("The original message matches the decrypted message.")

else:

    print("Verification Failed!")

    print("The original message does not match the decrypted message.")
