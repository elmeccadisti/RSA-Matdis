import streamlit as st
import rsa_core

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="RSA Matdis | Cryptography Lab",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. GLOBAL STYLE
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --paper: #F8F3E9;
    --ink: #303529;
    --secondary: #505747;
    --green: #77C982;
    --yellow: #F5E76A;
    --blue: #8BB8CC;
    --coral: #F08080;
    --white: #FFFDF8;
    --border: #55594D;
}

/* Background and page layout */
.stApp {
    background-color: var(--paper);
    background-image:
        linear-gradient(rgba(92, 139, 157, 0.16) 1px, transparent 1px),
        linear-gradient(90deg, rgba(92, 139, 157, 0.16) 1px, transparent 1px);
    background-size: 32px 32px;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

/* Typography */
.stApp h1,
.stApp h2,
.stApp h3 {
    color: var(--ink) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
}

.stApp p,
.stApp label,
.stApp li {
    color: var(--ink);
}

.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stCaptionContainer"] p {
    color: var(--secondary) !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: var(--paper);
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: var(--ink) !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 9px 11px;
    border: 1px solid transparent;
    border-radius: 2px;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background-color: var(--yellow);
    border-color: var(--ink);
}

/* Buttons */
.stButton > button {
    background-color: var(--green);
    color: var(--ink) !important;
    border: 1px solid var(--ink);
    border-radius: 2px;
    font-family: 'DM Mono', monospace;
    font-weight: 600;
    min-height: 2.6rem;
}

.stButton > button p {
    color: var(--ink) !important;
}

.stButton > button:hover {
    background-color: var(--yellow);
    color: var(--ink) !important;
    border: 1px solid var(--ink);
}

/* Primary buttons */
.stButton > button[kind="primary"] {
    background-color: var(--ink);
    color: var(--white) !important;
    border: 1px solid var(--ink);
}

.stButton > button[kind="primary"] p {
    color: var(--white) !important;
}

.stButton > button[kind="primary"]:hover {
    background-color: #505747;
    color: var(--white) !important;
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: var(--white) !important;
    color: var(--ink) !important;
    border: 1px solid var(--border) !important;
    border-radius: 2px !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #64695D !important;
    opacity: 1;
}

/* Selectors and slider labels */
.stSlider label,
.stTextInput label,
.stTextArea label {
    color: var(--ink) !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: var(--white);
    border: 1px solid var(--border);
    border-radius: 2px;
    padding: 15px;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: var(--secondary) !important;
}

[data-testid="stMetricValue"] {
    color: var(--ink) !important;
}

/* Editorial cards */
.editorial-card {
    background-color: var(--white);
    border: 1px solid var(--ink);
    padding: 20px;
    min-height: 165px;
}

.editorial-card h3,
.editorial-card p {
    color: var(--ink) !important;
}

.editorial-card h3 {
    font-size: 19px;
    margin-bottom: 10px;
}

.editorial-card p {
    font-size: 14px;
    line-height: 1.6;
}

/* Parameter cards */
.parameter-card {
    background: var(--white);
    border: 1px solid var(--border);
    padding: 16px;
    min-height: 105px;
}

.parameter-label {
    color: var(--secondary);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.parameter-value {
    color: var(--ink);
    font-family: 'DM Mono', monospace;
    font-size: 17px;
    font-weight: 600;
    overflow-wrap: anywhere;
}

/* Code, data and expanders */
[data-testid="stCode"] {
    border: 1px solid var(--border);
    border-radius: 2px;
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
}

[data-testid="stExpander"] {
    background-color: var(--white);
    border: 1px solid var(--border);
    border-radius: 2px;
}

[data-testid="stExpander"] summary {
    color: var(--ink) !important;
}

/* Alerts and separators */
[data-testid="stAlert"] {
    border-radius: 2px;
}

hr {
    border-color: rgba(48, 53, 41, 0.45);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-title {
        font-size: 32px !important;
    }

    .editorial-card {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. SESSION STATE
# =========================================================

defaults = {
    "primes": None,
    "rsa_keys": None,
    "e_input": "65537",
    "pesan": "",
    "ciphertext": [],
    "hasil_dekripsi": None,
    "p_bits": 448,
    "q_bits": 448,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def clear_message_results():
    """Clear encryption/decryption results when the key pair changes."""
    st.session_state.ciphertext = []
    st.session_state.hasil_dekripsi = None


def regenerate_primes():
    """Generate new p and q based on the selected bit lengths."""
    st.session_state.primes = rsa_core.generate_primes(
        st.session_state.p_bits,
        st.session_state.q_bits
    )
    st.session_state.rsa_keys = None
    clear_message_results()


# =========================================================
# 4. SIDEBAR / NAVIGATION
# =========================================================

st.sidebar.markdown("""
<div style="
    border-bottom: 1px solid #55594D;
    padding: 12px 5px 20px 5px;
">
    <div style="
        font-family: 'DM Mono', monospace;
        font-size: 10px;
        letter-spacing: 1.5px;
        color: #505747;
    ">
        DISCRETE MATHEMATICS
    </div>
    <div style="
        font-family: 'Space Grotesk', sans-serif;
        font-size: 27px;
        font-weight: 700;
        color: #303529;
        margin-top: 7px;
    ">
        RSA LAB 🔐
    </div>
    <div style="
        font-family: 'DM Sans', sans-serif;
        font-size: 12px;
        color: #505747;
    ">
        Interactive Cryptography
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.write("")
st.sidebar.caption("NAVIGATION")

menu = st.sidebar.radio(
    "Menu",
    ["Home", "Key Generation", "Encryption", "Decryption"],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.markdown("""
<div style="
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    line-height: 1.8;
    color: #505747;
">
    RSA MATDIS PROJECT<br>
    LEARN • ENCRYPT • DECRYPT
</div>
""", unsafe_allow_html=True)


# =========================================================
# 5. REUSABLE DISPLAY HELPERS
# =========================================================

def show_parameter_card(label, value, background="#FFFDF8"):
    """Display a parameter in a high-contrast editorial card."""
    st.markdown(
        f"""
        <div class="parameter-card" style="background:{background};">
            <div class="parameter-label">{label}</div>
            <div class="parameter-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 6. HOME PAGE
# =========================================================

if menu == "Home":

    st.markdown("""
    <div style="
        border: 1px solid #303529;
        background: #FFFDF8;
        padding: 38px;
    ">
        <p style="
            color: #505747;
            font-family: 'DM Mono', monospace;
            font-size: 11px;
            letter-spacing: 2px;
        ">
            DISCRETE MATHEMATICS / RSA PROJECT
        </p>

        <h1 class="hero-title" style="
            color: #303529;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 46px;
            line-height: 1.12;
            margin: 12px 0;
        ">
            Explore the world of<br>
            RSA Cryptography.
        </h1>

        <p style="
            color: #303529;
            font-size: 15px;
            max-width: 620px;
            line-height: 1.7;
        ">
            Discover the mathematics behind secure communication
            through interactive learning, key generation,
            encryption, and decryption.
        </p>

        <div style="
            display: inline-block;
            background: #F5E76A;
            border: 1px solid #303529;
            padding: 8px 13px;
            margin-top: 8px;
            color: #303529;
            font-family: 'DM Mono', monospace;
            font-size: 11px;
            font-weight: 600;
        ">
            LEARN • ENCRYPT • DECRYPT
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Explore RSA")
    st.caption("THREE STEPS TO UNDERSTAND RSA")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="editorial-card" style="background:#8BB8CC;">
            <h3>01. Key Generation 🔑</h3>
            <p>
                Generate public and private keys using prime numbers
                and Euler's totient function.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="editorial-card" style="background:#F5E76A;">
            <h3>02. Encryption 🔒</h3>
            <p>
                Transform plaintext into ciphertext using
                the RSA public key.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="editorial-card" style="background:#77C982;">
            <h3>03. Decryption 🔓</h3>
            <p>
                Recover the original message using
                the RSA private key.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    st.subheader("The Mathematics Behind RSA")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <div class="editorial-card">
            <h3>How does RSA work?</h3>
            <p>
                RSA is an asymmetric cryptographic algorithm that
                uses two different keys: a public key for encryption
                and a private key for decryption.
            </p>
            <p>
                Its mathematical foundation includes prime numbers,
                Euler's totient function, and modular arithmetic.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="editorial-card" style="background:#F5E76A;">
            <h3>RSA Formula</h3>
            <p style="
                font-family:'DM Mono', monospace;
                font-size:19px;
                font-weight:600;
            ">
                C = M<sup>e</sup> mod n
            </p>
            <p style="
                font-family:'DM Mono', monospace;
                font-size:19px;
                font-weight:600;
            ">
                M = C<sup>d</sup> mod n
            </p>
            <p>
                Encryption uses the public key, while decryption
                uses the private key.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.caption("RSA MATDIS | INTERACTIVE CRYPTOGRAPHY LEARNING PLATFORM")


# =========================================================
# 7. KEY GENERATION PAGE
# =========================================================

elif menu == "Key Generation":

    st.title("Key Generation 🔑")
    st.write(
        "Generate prime numbers p and q, calculate RSA parameters, "
        "then determine the public and private keys."
    )

    # ----- STEP 1: Generate p and q -----

    st.divider()
    st.subheader("01 — Prime Numbers")

    st.write(
        "Atur panjang bit bilangan prima p dan q. "
        "Bilangan prima akan dibangkitkan ketika slider digeser "
        "atau tombol pembangkitan ditekan."
    )

    # Restore slider values based on previously generated primes.
    current_primes = st.session_state.primes
    if current_primes:
        st.session_state.p_bits = current_primes["p_bits"]
        st.session_state.q_bits = current_primes["q_bits"]

    col_p, col_q = st.columns(2)

    with col_p:
        st.slider(
            "Panjang bit p",
            min_value=16,
            max_value=1024,
            step=8,
            key="p_bits",
            on_change=regenerate_primes
        )

    with col_q:
        st.slider(
            "Panjang bit q",
            min_value=16,
            max_value=1024,
            step=8,
            key="q_bits",
            on_change=regenerate_primes
        )

    st.caption(
        f"Perkiraan panjang n: "
        f"{st.session_state.p_bits + st.session_state.q_bits} bit."
    )

    st.button(
        "Generate New Prime Numbers",
        on_click=regenerate_primes
    )

    # Generate the first pair when the page is first opened.
    if st.session_state.primes is None:
        with st.spinner("Generating prime numbers..."):
            regenerate_primes()

    primes = st.session_state.primes

    if primes:
        st.success("Prime numbers successfully generated.")

        col1, col2 = st.columns(2)

        with col1:
            show_parameter_card(
                f"PRIME NUMBER P · {primes['p_bits']} BITS",
                primes["p"],
                "#8BB8CC"
            )

        with col2:
            show_parameter_card(
                f"PRIME NUMBER Q · {primes['q_bits']} BITS",
                primes["q"],
                "#F5E76A"
            )

        with st.expander("View p and q details", expanded=False):
            st.write("**p**")
            st.code(str(primes["p"]), language=None, wrap_lines=True)
            st.write("**q**")
            st.code(str(primes["q"]), language=None, wrap_lines=True)

        # ----- STEP 2: Calculate n and phi -----

        st.divider()
        st.subheader("02 — RSA Parameters")

        col1, col2 = st.columns(2)

        with col1:
            show_parameter_card(
                "MODULUS · n = p × q",
                primes["n"],
                "#FFFDF8"
            )

        with col2:
            show_parameter_card(
                "EULER'S TOTIENT · φ(n)",
                primes["phi"],
                "#77C982"
            )

        # ----- STEP 3: Input e -----

        st.divider()
        st.subheader("03 — Public Exponent (e)")

        st.write(
            "Masukkan e dengan syarat **1 < e < φ(n)** dan "
            "**gcd(e, φ(n)) = 1**."
        )

        def pakai_e_acak():
            st.session_state.e_input = str(
                rsa_core.random_e(st.session_state.primes["phi"])
            )

        st.text_input("Nilai e", key="e_input")

        col_a, col_b = st.columns(2)

        with col_a:
            hitung = st.button(
                "Calculate RSA Keys",
                type="primary",
                use_container_width=True
            )

        with col_b:
            st.button(
                "Generate Random e",
                on_click=pakai_e_acak,
                use_container_width=True
            )

        if hitung:
            try:
                e_val = int(st.session_state.e_input.strip())
                st.session_state.rsa_keys = rsa_core.compute_keys(
                    primes,
                    e_val
                )
                clear_message_results()

            except ValueError as err:
                st.session_state.rsa_keys = None

                if "invalid literal" in str(err):
                    st.error("e harus berupa bilangan bulat.")
                else:
                    st.error(str(err))

        # ----- STEP 4: Display key pair -----

        keys = st.session_state.rsa_keys

        if keys:
            st.divider()
            st.subheader("04 — Generated RSA Key Pair")

            st.success("RSA key pair successfully generated!")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("""
                <div style="
                    background:#77C982;
                    border:1px solid #303529;
                    padding:15px;
                    margin-bottom:10px;
                ">
                    <div style="
                        color:#303529;
                        font-family:'DM Mono',monospace;
                        font-size:12px;
                        font-weight:600;
                    ">
                        PUBLIC KEY
                    </div>
                    <div style="color:#303529;font-size:13px;">
                        Used for encryption
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.code(
                    f"n = {keys['n']}\ne = {keys['e']}",
                    language=None,
                    wrap_lines=True
                )

            with col2:
                st.markdown("""
                <div style="
                    background:#F5E76A;
                    border:1px solid #303529;
                    padding:15px;
                    margin-bottom:10px;
                ">
                    <div style="
                        color:#303529;
                        font-family:'DM Mono',monospace;
                        font-size:12px;
                        font-weight:600;
                    ">
                        PRIVATE KEY
                    </div>
                    <div style="color:#303529;font-size:13px;">
                        Used for decryption
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.code(
                    f"n = {keys['n']}\nd = {keys['d']}",
                    language=None,
                    wrap_lines=True
                )

            st.warning(
                "Jaga kerahasiaan private key. "
                "Implementasi ini ditujukan untuk pembelajaran."
            )

            with st.expander("View mathematical calculation"):
                st.markdown("**Step 1 — Public exponent**")
                st.latex(r"1 < e < \varphi(n)")
                st.write(f"e = {keys['e']}")

                st.markdown("**Step 2 — Private exponent**")
                st.latex(r"d = e^{-1} \mod \varphi(n)")
                st.write(f"d = {keys['d']}")


# =========================================================
# 8. ENCRYPTION PAGE
# =========================================================

elif menu == "Encryption":

    st.title("Message Encryption 🔒")
    st.write(
        "Masukkan pesan yang ingin dienkripsi menggunakan public key."
    )

    keys = st.session_state.rsa_keys

    if not keys:
        st.warning(
            "Belum ada kunci RSA. Buat kunci terlebih dahulu "
            "melalui menu **Key Generation**."
        )

    else:
        n_pub, e_pub = keys["public_key"]

        with st.expander("Public key being used", expanded=False):
            st.code(
                f"n = {n_pub}\ne = {e_pub}",
                language=None,
                wrap_lines=True
            )

        st.divider()
        st.subheader("01 — Enter Plaintext")

        default_message = (
            st.session_state.pesan
            if st.session_state.pesan
            else "Halo, ini Mecca, Dara, Michelle!"
        )

        pesan = st.text_area(
            "Plaintext Message",
            value=default_message,
            height=130,
            help="Masukkan pesan yang ingin dienkripsi."
        )

        if st.button("Encrypt Message", type="primary"):
            try:
                ciphertext = rsa_core.enkripsi(
                    pesan,
                    keys["public_key"]
                )

            except ValueError as err:
                st.error(str(err))

            else:
                if not ciphertext:
                    st.warning("Pesan tidak boleh kosong.")
                else:
                    st.session_state.pesan = pesan
                    st.session_state.ciphertext = ciphertext
                    st.session_state.hasil_dekripsi = None
                    st.success("Message successfully encrypted!")

        if st.session_state.ciphertext:
            st.divider()
            st.subheader("02 — Encryption Result")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("""
                <div style="
                    background:#F5E76A;
                    border:1px solid #303529;
                    padding:12px;
                    margin-bottom:8px;
                ">
                    <strong style="color:#303529;">PLAINTEXT</strong>
                </div>
                """, unsafe_allow_html=True)

                st.code(
                    st.session_state.pesan,
                    language=None,
                    wrap_lines=True
                )

            with col2:
                st.markdown("""
                <div style="
                    background:#8BB8CC;
                    border:1px solid #303529;
                    padding:12px;
                    margin-bottom:8px;
                ">
                    <strong style="color:#26384A;">CIPHERTEXT</strong>
                </div>
                """, unsafe_allow_html=True)

                st.code(
                    str(st.session_state.ciphertext),
                    language=None,
                    wrap_lines=True
                )

            st.metric(
                "Total Characters Encrypted",
                len(st.session_state.ciphertext)
            )

            st.markdown("**Encryption formula**")
            st.latex(r"C = M^e \mod n")

            st.caption(
                "Setiap karakter diubah menjadi kode ASCII (M), "
                "kemudian dienkripsi menggunakan rumus RSA."
            )

            with st.expander("View character-by-character details"):
                rows = [
                    {
                        "Karakter": ch,
                        "ASCII (M)": ord(ch),
                        "Ciphertext (C)": str(c)
                    }
                    for ch, c in zip(
                        st.session_state.pesan,
                        st.session_state.ciphertext
                    )
                ]

                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True
                )


# =========================================================
# 9. DECRYPTION PAGE
# =========================================================

elif menu == "Decryption":

    st.title("Message Decryption 🔓")
    st.write(
        "Gunakan private key untuk mengembalikan ciphertext "
        "menjadi plaintext."
    )

    keys = st.session_state.rsa_keys

    if not keys:
        st.warning(
            "Belum ada kunci RSA. Buat kunci terlebih dahulu "
            "melalui menu **Key Generation**."
        )

    elif not st.session_state.ciphertext:
        st.warning(
            "Belum ada ciphertext. Lakukan enkripsi pesan terlebih dahulu "
            "melalui menu **Encryption**."
        )

    else:
        n_priv, d_priv = keys["private_key"]

        with st.expander("Private key being used", expanded=False):
            st.code(
                f"n = {n_priv}\nd = {d_priv}",
                language=None,
                wrap_lines=True
            )

        st.divider()
        st.subheader("01 — Encrypted Message")

        st.code(
            str(st.session_state.ciphertext),
            language=None,
            wrap_lines=True
        )

        if st.button("Decrypt Message", type="primary"):
            try:
                st.session_state.hasil_dekripsi = rsa_core.dekripsi(
                    st.session_state.ciphertext,
                    keys["private_key"]
                )

            except ValueError as err:
                st.session_state.hasil_dekripsi = None
                st.error(str(err))

        if st.session_state.hasil_dekripsi is not None:
            st.divider()
            st.subheader("02 — Decryption Result")

            st.markdown("""
            <div style="
                background:#77C982;
                border:1px solid #303529;
                padding:12px;
                margin-bottom:8px;
            ">
                <strong style="color:#303529;">
                    DECRYPTED MESSAGE
                </strong>
            </div>
            """, unsafe_allow_html=True)

            st.code(
                st.session_state.hasil_dekripsi,
                language=None,
                wrap_lines=True
            )

            st.markdown("**Decryption formula**")
            st.latex(r"M = C^d \mod n")

            st.divider()
            st.subheader("03 — Verification")

            if st.session_state.pesan == st.session_state.hasil_dekripsi:
                st.success(
                    "VERIFICATION SUCCESSFUL — "
                    "Pesan hasil dekripsi sama dengan pesan asli."
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Original Message**")
                    st.code(
                        st.session_state.pesan,
                        language=None
                    )

                with col2:
                    st.markdown("**Decrypted Message**")
                    st.code(
                        st.session_state.hasil_dekripsi,
                        language=None
                    )

            else:
                st.error(
                    "VERIFICATION FAILED — "
                    "Pesan hasil dekripsi berbeda dengan pesan asli."
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Original Message**")
                    st.code(
                        st.session_state.pesan,
                        language=None
                    )

                with col2:
                    st.markdown("**Decrypted Message**")
                    st.code(
                        st.session_state.hasil_dekripsi,
                        language=None
                    )


# =========================================================
# 10. FOOTER
# =========================================================

st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.caption(
        "RSA MATDIS | INTERACTIVE CRYPTOGRAPHY LEARNING PLATFORM"
    )

with col2:
    st.caption("LEARN • ENCRYPT • DECRYPT")

st.caption(
    "Catatan: implementasi RSA ini digunakan untuk pembelajaran. "
    "RSA dalam penggunaan nyata memerlukan padding yang aman "
    "(misalnya OAEP) dan umumnya digunakan untuk mengenkripsi "
    "kunci simetris, bukan pesan per karakter seperti simulasi ini."
)
