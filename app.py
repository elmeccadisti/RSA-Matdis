import streamlit as st
import rsa_core

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="RSA Matematika Diskrit",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #fff7eb;
    color: #cc3a63;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #f9f0e0;
}

/* Main text */
h1, h2, h3, p, label {
    color: #cc3a63;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #fff7eb;
    color: #cc3a63;
    border: 1px solid #f9f0e0;
    border-radius: 8px;
}

/* Buttons */
.stButton button {
    background-color: #cc3a63;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton button:hover {
    background-color: #cc3a63;
    color: white;
}

/* Cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #E0E7F1;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE
# ==========================================

defaults = {
    "primes": None,        # hasil rsa_core.generate_primes (p, q, n, phi)
    "rsa_keys": None,          # hasil rsa_core.compute_keys (lengkap dengan e, d)
    "e_input": "65537",    # isi kolom input e
    "pesan": "",           # plaintext asli
    "ciphertext": [],      # hasil enkripsi
    "hasil_dekripsi": None # hasil dekripsi terakhir
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ==========================================
# 3. SIDEBAR / NAVIGASI
# ==========================================

st.sidebar.title("🔐 RSA MATDIS")
st.sidebar.caption("Cryptography Learning Platform")
st.sidebar.divider()

menu = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Key Generation",
        "Encryption",
        "Decryption"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Discrete Mathematics Project")

# ==========================================
# 4. HALAMAN HOME
# ==========================================

if menu == "Home":

    st.title("RSA Cryptography")
    st.subheader(
        "Interactive RSA Cryptography Learning Platform"
    )

    st.write(
        """
        Selamat datang di platform pembelajaran algoritma RSA.

        Website ini dirancang untuk membantu memahami konsep
        kriptografi asimetris melalui pembelajaran teori dan
        simulasi proses enkripsi serta dekripsi pesan.
        """
    )

    st.divider()

    st.header("Explore RSA")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card" style="
            background-color: #fff7eb;
            border-color: #f9f0e0;
        ">
            <h3 style="color: #287a67;">Key Generation</h3>
            <p>
            Pelajari proses pembangkitan pasangan
            public key dan private key.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card" style="
            background-color: #fff7eb;
            border-color: #f9f0e0;
        ">
            <h3 style="color: #287A67;">Encryption</h3>
            <p>
            Pelajari bagaimana plaintext
            diubah menjadi ciphertext.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card" style="
            background-color: #fff7eb;
            border-color: #f9f0e0;
        ">
            <h3 style="color: #287a67;">Decryption</h3>
            <p>
            Pelajari bagaimana ciphertext
            dikembalikan menjadi plaintext.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.header("How RSA Works")

    step1, step2, step3 = st.columns(3)

    with step1:
        st.subheader("01. Key Generation")
        st.write("Membentuk public key dan private key.")

    with step2:
        st.subheader("02. Encryption")
        st.write("Mengenkripsi pesan menggunakan public key.")

    with step3:
        st.subheader("03. Decryption")
        st.write("Mengembalikan pesan menggunakan private key.")

# ==========================================
# 5. HALAMAN KEY GENERATION
# ==========================================

elif menu == "Key Generation":

    st.title("Key Generation 🔑")

    st.write(
        "Atur panjang bit bilangan prima p dan q, bangkitkan keduanya, "
        "lalu masukkan nilai e untuk mendapatkan pasangan public key "
        "dan private key."
    )

    # ---------- TAHAP 1: p dan q ----------
    st.subheader("Tahap 1: Bilangan Prima p dan q")

    def regenerate_primes():
        """Bangkitkan p dan q langsung dari nilai slider."""
        st.session_state.primes = rsa_core.generate_primes(
            st.session_state.p_bits, st.session_state.q_bits
        )
        # p, q baru -> kunci dan hasil lama tidak berlaku lagi
        st.session_state.rsa_keys = None
        st.session_state.ciphertext = []
        st.session_state.hasil_dekripsi = None

    # Slider mengikuti p dan q yang sudah ada (misal saat kembali ke halaman ini)
    _pr = st.session_state.primes
    st.session_state.setdefault("p_bits", _pr["p_bits"] if _pr else 448)
    st.session_state.setdefault("q_bits", _pr["q_bits"] if _pr else 448)

    col_p, col_q = st.columns(2)

    with col_p:
        st.slider("Panjang bit p", 16, 1024, step=8,
                  key="p_bits", on_change=regenerate_primes)
    with col_q:
        st.slider("Panjang bit q", 16, 1024, step=8,
                  key="q_bits", on_change=regenerate_primes)

    st.caption(
        f"n = p × q akan berukuran ±{st.session_state.p_bits + st.session_state.q_bits} bit. "
        "p dan q otomatis dibangkitkan setiap slider digeser."
    )

    st.button("Bangkitkan ulang p dan q (acak baru)", on_click=regenerate_primes)

    # Pertama kali halaman dibuka: langsung bangkitkan p dan q
    if st.session_state.primes is None:
        with st.spinner("Membangkitkan bilangan prima..."):
            regenerate_primes()

    primes = st.session_state.primes

    if primes:
        st.info(
            f"Step 1: p ({primes['p_bits']} bit) dan q ({primes['q_bits']} bit) "
            "dibangkitkan."
        )
        st.code(f"p = {primes['p']}\n\nq = {primes['q']}", language=None, wrap_lines=True)

        st.info("Step 2: Menghitung n = p × q.")
        st.code(f"n = {primes['n']}", language=None, wrap_lines=True)

        st.info("Step 3: Menghitung φ(n) = (p − 1) × (q − 1).")
        st.code(f"phi(n) = {primes['phi']}", language=None, wrap_lines=True)

        # ---------- TAHAP 2: input e ----------
        st.divider()
        st.subheader("Tahap 2: Input Public Exponent (e)")

        st.write(
            "Masukkan e dengan syarat **1 < e < φ(n)** dan "
            "**gcd(e, φ(n)) = 1**."
        )

        def pakai_e_acak():
            st.session_state.e_input = str(rsa_core.random_e(primes["phi"]))

        st.text_input("Nilai e", key="e_input")

        col_a, col_b = st.columns(2)
        with col_a:
            hitung = st.button("Hitung Kunci", type="primary")
        with col_b:
            st.button("Pilih e acak", on_click=pakai_e_acak)

        if hitung:
            try:
                e_val = int(st.session_state.e_input.strip())
                st.session_state.rsa_keys = rsa_core.compute_keys(primes, e_val)
                st.session_state.ciphertext = []
                st.session_state.hasil_dekripsi = None
            except ValueError as err:
                st.session_state.rsa_keys = None
                if "invalid literal" in str(err):
                    st.error("e harus berupa bilangan bulat.")
                else:
                    st.error(str(err))

    keys = st.session_state.rsa_keys

    if primes and keys:
        st.info("Step 4: e valid (gcd(e, φ(n)) = 1).")
        st.code(f"e = {keys['e']}", language=None, wrap_lines=True)

        st.info("Step 5: Menghitung private exponent d = e⁻¹ mod φ(n).")
        st.code(f"d = {keys['d']}", language=None, wrap_lines=True)

        st.success("Kunci berhasil dibangkitkan!")

        st.divider()
        st.subheader("Hasil Kunci")

        col_pub, col_priv = st.columns(2)

        with col_pub:
            st.write("**Public Key (n, e)**")
            st.code(f"n = {keys['n']}\n\ne = {keys['e']}", language=None, wrap_lines=True)

        with col_priv:
            st.write("**Private Key (n, d)**")
            st.code(f"n = {keys['n']}\n\nd = {keys['d']}", language=None, wrap_lines=True)

        st.warning("🚨 Jaga kerahasiaan private key!")

# ==========================================
# 6. HALAMAN ENCRYPTION
# ==========================================

elif menu == "Encryption":

    st.title("Message Encryption 🔒")

    st.write(
        "Masukkan pesan yang ingin dienkripsi menggunakan public key."
    )

    keys = st.session_state.rsa_keys

    if not keys:
        st.warning(
            "🚫 Belum ada kunci. Buat kunci terlebih dahulu di menu "
            "**Key Generation**."
        )
    else:
        n_pub, e_pub = keys["public_key"]

        with st.expander("Public Key yang digunakan", expanded=False):
            st.code(f"n = {n_pub}\n\ne = {e_pub}", language=None, wrap_lines=True)

        pesan = st.text_area(
            "Plaintext Message",
            value=st.session_state.pesan
            or "Halo, ini adalah pesan rahasia dari Matematika Diskrit!",
            height=120
        )

        if st.button("Encrypt Message", type="primary"):
            try:
                ciphertext = rsa_core.enkripsi(pesan, keys["public_key"])
            except ValueError as err:
                st.error(str(err))
            else:
                if not ciphertext:
                    st.warning("Pesan tidak boleh kosong.")
                else:
                    st.session_state.pesan = pesan
                    st.session_state.ciphertext = ciphertext
                    st.session_state.hasil_dekripsi = None
                    st.success("Pesan berhasil dienkripsi!")

        if st.session_state.ciphertext:
            st.divider()
            st.subheader("Hasil Enkripsi")

            st.write("**Plaintext:**")
            st.code(st.session_state.pesan, language=None, wrap_lines=True)

            st.write("**Ciphertext (list bilangan bulat):**")
            st.code(str(st.session_state.ciphertext), language=None, wrap_lines=True)

            st.caption(
                "Setiap karakter diubah ke kode ASCII (M), lalu dienkripsi "
                "dengan rumus C = M^e mod n."
            )

            with st.expander("Lihat detail per karakter"):
                rows = [
                    {
                        "Karakter": ch,
                        "ASCII (M)": ord(ch),
                        "Ciphertext (C)": str(c),
                    }
                    for ch, c in zip(
                        st.session_state.pesan, st.session_state.ciphertext
                    )
                ]
                st.dataframe(rows, use_container_width=True)

# ==========================================
# 7. HALAMAN DECRYPTION
# ==========================================

elif menu == "Decryption":

    st.title("Message Decryption ✅")

    st.write(
        "Pesan terenkripsi dari halaman Encryption akan dipakai "
        "otomatis untuk proses dekripsi."
    )

    keys = st.session_state.rsa_keys

    if not keys:
        st.warning(
            "🚫 Belum ada kunci. Buat kunci di menu **Key Generation**."
        )
    elif not st.session_state.ciphertext:
        st.warning(
            "🚫 Belum ada pesan terenkripsi. Enkripsi pesan di menu "
            "**Encryption** terlebih dahulu."
        )
    else:
        n_priv, d_priv = keys["private_key"]

        with st.expander("Private Key yang digunakan", expanded=False):
            st.code(f"n = {n_priv}\n\nd = {d_priv}", language=None, wrap_lines=True)

        st.write("**Encrypted Message to Decrypt:**")
        st.code(str(st.session_state.ciphertext), language=None, wrap_lines=True)

        if st.button("Decrypt Message", type="primary"):
            try:
                st.session_state.hasil_dekripsi = rsa_core.dekripsi(
                    st.session_state.ciphertext, keys["private_key"]
                )
            except ValueError as err:
                st.session_state.hasil_dekripsi = None
                st.error(str(err))

        if st.session_state.hasil_dekripsi is not None:
            st.success("Pesan berhasil didekripsi!")

            st.subheader("Decrypted Message")
            st.code(st.session_state.hasil_dekripsi, language=None, wrap_lines=True)

            st.divider()
            st.subheader("Verification")

            if st.session_state.pesan == st.session_state.hasil_dekripsi:
                st.success(
                    "🎉 Verifikasi berhasil! Pesan hasil dekripsi sama "
                    "dengan pesan asli."
                )
            else:
                st.error(
                    "❌ Verifikasi gagal! Pesan hasil dekripsi berbeda "
                    "dengan pesan asli."
                )
                st.write(f"**Pesan asli:** `{st.session_state.pesan}`")
                st.write(f"**Hasil dekripsi:** `{st.session_state.hasil_dekripsi}`")

# ==========================================
# 8. FOOTER
# ==========================================

st.divider()

st.caption(
    "RSA MATDIS | Interactive Cryptography Learning Platform"
)
st.caption(
    "Catatan: ini adalah implementasi RSA sederhana untuk pembelajaran. "
    "RSA sungguhan memakai padding (mis. OAEP) dan umumnya hanya "
    "mengenkripsi kunci simetris, bukan pesan per karakter seperti di sini."
)
