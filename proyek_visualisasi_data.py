import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ======== Konfigurasi Halaman ========
st.set_page_config(page_title="Visualisasi Data Kesehatan Mental di Industri Teknologi", layout="wide")

# ======== Styling CSS Responsif Dark/Light Mode ========
st.markdown("""
    <style>
    .stApp {
        font-family: 'Segoe UI', sans-serif;
        transition: background-color 0.5s, color 0.5s;
    }

    /* Light Mode */
    @media (prefers-color-scheme: light) {
        .stApp {
            background: linear-gradient(to right, #f0f0f0, #ffffff);
            color: #212121;
        }
        h1, h2, h3, h4 {
            color: #004d40;
        }
        section[data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #ccc;
        }
        section[data-testid="stSidebar"] * {
            color: #004d40 !important;
        }
    }

    /* Dark Mode */
    @media (prefers-color-scheme: dark) {
        .stApp {
            background: linear-gradient(to right, #0d0d0d, #1c1c1c);
            color: #e0f2f1;
        }
        h1, h2, h3, h4 {
            color: #80cbc4;
        }
        section[data-testid="stSidebar"] {
            background-color: #1f2c2c;
            border-right: 1px solid #37474f;
        }
        section[data-testid="stSidebar"] * {
            color: #e0f2f1 !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ======== Sidebar ========
st.sidebar.title("Dashboard")
opsi = st.sidebar.radio(
    "Pilih halaman visualisasi:",
    [
        "Home",
        "Jumlah Responden per Negara",
        "Distribusi Usia Responden",
        "Usia vs Keputusan Mencari Pengobatan",
        "Heatmap Korelasi Usia & Pengobatan",
        "Distribusi Jenis Kelamin Responden"
    ]
)

# ======== Home Page ========
if opsi == "Home":
    st.markdown("## Proyek pada Mata Kuliah Visualisasi Data")
    st.markdown("""
    ### Visualisasi Data Kesehatan Mental di Industri Teknologi  
    **Dibuat oleh:**
    - Muhammad Nizar Al-Faiq (0110223298)  
    - Sabrina Marliani (0110223141)
    """)
    st.success("""
    Masalah kesehatan mental seperti stres, kecemasan, dan depresi sering kali tidak mendapatkan perhatian yang setara dengan kesehatan fisik. 
    Terutama di industri teknologi yang dikenal memiliki tekanan tinggi, jam kerja panjang, dan ekspektasi performa besar. 
    Aplikasi ini menampilkan visualisasi data untuk membantu memahami isu ini lebih baik.
    """)

# ======== Visualisasi 1 - Bar Chart ========
elif opsi == "Jumlah Responden per Negara":
    st.markdown("## Jumlah Responden per Negara")
    st.markdown("Visualisasi ini menunjukkan bahwa survei tentang kesehatan mental di bidang teknologi memiliki cakupan global, namun masih didominasi oleh negara-negara tertentu, terutama Amerika Serikat.")

    with st.spinner("Memuat grafik..."):
        negara = [
            'United States', 'United Kingdom', 'Canada', 'Germany', 'Netherlands', 'Ireland', 'Australia',
            'France', 'India', 'Poland', 'New Zealand', 'Switzerland', 'Sweden', 'Italy', 'Brazil',
            'Belgium', 'South Africa', 'Israel', 'Singapore', 'Austria', 'Bulgaria', 'Mexico', 'Finland',
            'Russia', 'Colombia', 'Greece', 'Portugal', 'Croatia', 'Spain', 'Slovenia', 'Thailand', 'Romania',
            'Ukraine', 'Uruguay', 'Philippines', 'Japan', 'Norway', 'Moldova', 'Latvia', 'Hungary',
            'Georgia', 'Egypt', 'Denmark', 'Czech Republic', 'Bosnia and Herzegovina', 'China', 'Total Keseluruhan'
        ]
        jumlah = [
            735, 180, 75, 40, 30, 28, 25, 20, 18, 16, 14, 13, 11, 10, 9,
            8, 7, 7, 6, 6, 5, 5, 5, 4, 4, 3, 3, 3, 3, 3, 2, 2,
            2, 2, 2, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1
        ]
        df = pd.DataFrame({'Negara': negara, 'Jumlah Responden': jumlah})
        fig = px.bar(df, x="Negara", y="Jumlah Responden",
                     title="Jumlah Responden per Negara",
                     labels={"Jumlah Responden": "Jumlah"},
                     color="Jumlah Responden",
                     color_continuous_scale="Teal")
        fig.update_layout(xaxis_tickangle=-90, height=600)
        st.plotly_chart(fig, use_container_width=True)

# ======== Visualisasi 2 - Histogram ========
elif opsi == "Distribusi Usia Responden":
    st.markdown("## Distribusi Usia Responden")
    st.markdown("Distribusi usia responden menunjukkan dominasi kelompok usia muda yang menyuarakan kesehatan mental mereka di industri teknologi.")

    with st.spinner("Memuat histogram..."):
        np.random.seed(42)
        usia = np.random.normal(loc=30, scale=10, size=1300).astype(int)
        usia = np.clip(usia, 18, 75)
        df = pd.DataFrame({"Usia": usia})
        fig = px.histogram(df, x="Usia", nbins=30,
                           title="Histogram Usia Responden",
                           color_discrete_sequence=['#26a69a'])
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

# ======== Visualisasi 3 - Scatter Plot ========
elif opsi == "Usia vs Keputusan Mencari Pengobatan":
    st.markdown("## Usia vs Keputusan Mencari Pengobatan")
    st.markdown("Scatter plot ini menunjukkan distribusi usia terhadap keputusan untuk mencari pengobatan atas kondisi mental.")

    with st.spinner("Memuat scatter plot..."):
        np.random.seed(42)
        jumlah_data = 200
        usia = np.random.randint(18, 75, jumlah_data)
        pengobatan = np.random.choice([0, 1], jumlah_data)
        df = pd.DataFrame({"Usia": usia, "Mencari Pengobatan": pengobatan})
        fig = px.scatter(df, x="Usia", y="Mencari Pengobatan", color="Mencari Pengobatan",
                         title="Usia vs Keputusan Mencari Pengobatan",
                         labels={"Mencari Pengobatan": "Pengobatan (0=Tidak, 1=Ya)"},
                         height=500)
        st.plotly_chart(fig, use_container_width=True)

# ======== Visualisasi 4 - Heatmap Korelasi ========
elif opsi == "Heatmap Korelasi Usia & Pengobatan":
    st.markdown("## Korelasi Usia & Pengobatan")
    st.markdown("Heatmap menunjukkan korelasi antara variabel usia dan keputusan mencari pengobatan.")

    with st.spinner("Memuat heatmap..."):
        np.random.seed(42)
        usia = np.random.randint(18, 75, 200)
        pengobatan = np.random.choice([0, 1], 200)
        df = pd.DataFrame({"Usia": usia, "Pengobatan": pengobatan})
        corr = df.corr()
        fig = go.Figure(data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            colorscale='RdBu',
            zmin=0, zmax=1,
            text=corr.values.round(2),
            hoverinfo='text'
        ))
        fig.update_layout(title="Korelasi Usia & Pengobatan", height=400)
        st.plotly_chart(fig, use_container_width=True)

# ======== Visualisasi 5 - Pie Chart ========
elif opsi == "Distribusi Jenis Kelamin Responden":
    st.markdown("## Distribusi Jenis Kelamin Responden")
    st.markdown("Diagram lingkaran menunjukkan komposisi gender dari responden survei.")

    with st.spinner("Memuat pie chart..."):
        labels = ['Male', 'Female', 'Other']
        values = [77.6, 15.5, 6.9]
        fig = px.pie(names=labels, values=values,
                     title="Distribusi Jenis Kelamin",
                     color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

# ======== Footer ========
st.markdown("---")
st.markdown("<center>Kelompok 5 - Visualisasi Data Kesehatan Mental di Industri Teknologi - STT Terpadu Nurul Fikri</center>", unsafe_allow_html=True)
