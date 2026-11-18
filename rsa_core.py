"""
Modul inti RSA (hanya fungsi, tanpa input/print) agar bisa di-import app.py.
"""

from math import gcd
import secrets

from Crypto.Util.number import getPrime


# ==========================================
# KEY GENERATION (2 tahap)
# ==========================================

def generate_primes(p_bits, q_bits):
    """
    Tahap 1: bangkitkan p dan q (panjang bit masing-masing bisa diatur),
    lalu hitung n dan phi(n).
    """
    p = getPrime(p_bits)
    q = getPrime(q_bits)

    while p == q:
        q = getPrime(q_bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "p_bits": p_bits,
        "q_bits": q_bits,
    }


def validate_e(e, phi):
    """Raise ValueError jika e tidak memenuhi 1 < e < phi dan gcd(e, phi) = 1."""
    if e <= 1 or e >= phi:
        raise ValueError("e harus memenuhi 1 < e < phi(n).")
    if gcd(e, phi) != 1:
        raise ValueError(
            f"gcd(e, phi(n)) = {gcd(e, phi)}, harus 1. Pilih nilai e lain."
        )


def random_e(phi):
    """Memilih e acak yang valid (opsional, sebagai bantuan)."""
    e = secrets.randbelow(phi - 2) + 2
    while gcd(e, phi) != 1:
        e = secrets.randbelow(phi - 2) + 2
    return e


def compute_keys(primes, e):
    """
    Tahap 2: dari p, q (hasil generate_primes) dan e input user,
    hitung d = e^-1 mod phi(n) dan bentuk public/private key.
    """
    phi = primes["phi"]
    validate_e(e, phi)

    d = pow(e, -1, phi)
    n = primes["n"]

    keys = dict(primes)
    keys.update({
        "e": e,
        "d": d,
        "public_key": (n, e),
        "private_key": (n, d),
    })
    return keys


# ==========================================
# ENKRIPSI (ASCII, per karakter)
# ==========================================

def enkripsi(pesan, public_key):
    """
    Mengenkripsi pesan per karakter (kode ASCII).
    Mengembalikan list ciphertext (int).
    Raise ValueError jika pesan tidak valid.
    """
    n, e = public_key

    try:
        data = pesan.encode("ascii")
    except UnicodeEncodeError:
        raise ValueError(
            "Pesan hanya boleh berisi karakter ASCII (tanpa emoji / huruf berakson)."
        )

    ciphertext = []
    for M in data:
        if M >= n:
            raise ValueError(
                f"Nilai ASCII {M} >= n. Gunakan ukuran bit p dan q yang lebih besar."
            )
        ciphertext.append(pow(M, e, n))

    return ciphertext


# ==========================================
# DEKRIPSI (ASCII, per karakter)
# ==========================================

def dekripsi(ciphertext, private_key):
    """
    Mendekripsi list ciphertext menjadi string.
    Raise ValueError jika hasil dekripsi bukan ASCII valid.
    """
    n, d = private_key

    hasil = [pow(c, d, n) for c in ciphertext]

    try:
        return bytes(hasil).decode("ascii")
    except (ValueError, UnicodeDecodeError):
        raise ValueError(
            "Dekripsi gagal: hasil bukan teks ASCII yang valid. "
            "Pastikan private key sesuai dengan public key yang dipakai."
        )
