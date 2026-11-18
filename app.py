
import streamlit as st
#import rsa_core

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
    border: 1px solid #f9f0e0;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR / NAVIGASI
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
# 3. HALAMAN HOME
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
# 4. HALAMAN KEY GENERATION
# ==========================================

elif menu == "Key Generation":

    st.title("Key Generation")

    st.write(
        "Halaman untuk mempelajari proses pembangkitan kunci RSA."
    )

    st.info("Fitur pembangkitan kunci akan ditambahkan berikutnya.")

# ==========================================
# 5. HALAMAN ENCRYPTION
# ==========================================

elif menu == "Encryption":

    st.title("Message Encryption")

    st.write(
        "Halaman untuk melakukan enkripsi plaintext menjadi ciphertext."
    )

    st.info("Fitur enkripsi akan ditambahkan berikutnya.")

# ==========================================
# 6. HALAMAN DECRYPTION
# ==========================================

elif menu == "Decryption":

    st.title("Message Decryption")

    st.write(
        "Halaman untuk melakukan dekripsi ciphertext menjadi plaintext."
    )

    st.info("Fitur dekripsi akan ditambahkan berikutnya.")

# ==========================================
# 7. FOOTER
# ==========================================

st.divider()

st.caption(
    "RSA MATDIS | Interactive Cryptography Learning Platform"
)
