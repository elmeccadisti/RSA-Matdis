
import streamlit as st
import rsa_core

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="RSA Matdis",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F8FAFD;
    color: #243B68;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EDF2FA;
}

/* Main text */
h1, h2, h3, p, label {
    color: #243B68;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF;
    color: #243B68;
    border: 1px solid #D5DEED;
    border-radius: 8px;
}

/* Buttons */
.stButton button {
    background-color: #315DA8;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton button:hover {
    background-color: #24477F;
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

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
            **Key Generation**

            Pelajari proses pembangkitan pasangan
            public key dan private key.
            """
        )

        st.success(
            """
            **Encryption**

            Pelajari bagaimana plaintext
            diubah menjadi ciphertext.
            """
        )

    with col2:
        st.warning(
            """
            **Decryption**

            Pelajari bagaimana ciphertext
            dikembalikan menjadi plaintext.
            """
        )

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
