import streamlit as st
import numpy as np
import pickle
import plotly.express as px
import pandas as pd

# -----------------------------------------
# SETUP APLIKASI
# -----------------------------------------
st.set_page_config(
    page_title="KNN Loan Prediction",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# LOAD MODEL
# -----------------------------------------
try:
    with open('knn_pinjam_mod.pkl', 'rb') as model_file:
        knn = pickle.load(model_file)
except FileNotFoundError:
    st.error("❌ File model 'knn_pinjam_mod.pkl' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama.")
    st.stop()

# -----------------------------------------
# HEADER
# -----------------------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#00b4d8;'>💳 K-Nearest Neighbor (KNN) Loan Eligibility Prediction</h1>
    <p style='text-align:center; color:gray;'>
        Aplikasi ini memprediksi kelayakan pinjaman berdasarkan data pribadi dan finansial Anda.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------
# INPUT SECTION
# -----------------------------------------
st.sidebar.header("🧾 Masukkan Data Peminjam")

usia = st.sidebar.number_input('Usia', min_value=18, max_value=70, value=30)
pendapatan = st.sidebar.number_input('Pendapatan (juta per bulan)', min_value=10, max_value=200, value=50)

status_perkawinan_label = st.sidebar.selectbox('Status Perkawinan', ['Belum Menikah', 'Menikah'])
status_perkawinan = 0 if status_perkawinan_label == 'Belum Menikah' else 1

jumlah_pinjaman = st.sidebar.number_input('Jumlah Pinjaman (juta)', min_value=10, max_value=500, value=100)
durasi_pinjaman = st.sidebar.number_input('Durasi Pinjaman (tahun)', min_value=1, max_value=30, value=10)

status_pekerjaan_label = st.sidebar.selectbox(
    'Status Pekerjaan',
    ['Karyawan Kontrak', 'Karyawan Tetap', 'Pensiunan', 'Wirausaha']
)
status_pekerjaan_dict = {
    'Karyawan Kontrak': 0,
    'Karyawan Tetap': 1,
    'Pensiunan': 2,
    'Wirausaha': 3
}
status_pekerjaan = status_pekerjaan_dict[status_pekerjaan_label]

# -----------------------------------------
# PREDIKSI
# -----------------------------------------
new_data = np.array([[usia, pendapatan, status_perkawinan, jumlah_pinjaman, durasi_pinjaman, status_pekerjaan]])

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 Hasil Prediksi")
    if st.button('Prediksi Sekarang'):
        prediction = knn.predict(new_data)
        result = 'Layak' if prediction == 0 else 'Tidak Layak'

        color = "#06d6a0" if result == 'Layak' else "#ef476f"
        st.markdown(
            f"""
            <div style='padding:20px; border-radius:10px; text-align:center; 
                        background-color:{color}; color:white; font-size:24px;'>
                <b>{result}</b>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Klik tombol **Prediksi Sekarang** untuk melihat hasil.")

# -----------------------------------------
# VISUALISASI 3D
# -----------------------------------------
with col2:
    st.subheader("📊 Visualisasi Prediksi KNN (Dummy Data)")

    df = pd.DataFrame({
        'Usia': np.random.randint(18, 70, size=80),
        'Pendapatan': np.random.randint(10, 200, size=80),
        'Jumlah_Pinjaman': np.random.randint(10, 500, size=80),
        'Lulus_Kredit': np.random.choice([0, 1], size=80)
    })

    fig = px.scatter_3d(
        df,
        x='Usia',
        y='Pendapatan',
        z='Jumlah_Pinjaman',
        color='Lulus_Kredit',
        color_continuous_scale=['#ef476f', '#06d6a0'],
        title='Simulasi Distribusi Data KNN'
    )

    fig.update_layout(
        scene=dict(
            xaxis_title='Usia',
            yaxis_title='Pendapatan',
            zaxis_title='Jumlah Pinjaman'
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray; font-size:13px;'>
        © 2025 Sistem Prediksi Kelayakan Pinjaman 
    </p>
    """,
    unsafe_allow_html=True
)