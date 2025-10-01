import streamlit as st
from fpdf import FPDF
import numpy as np

st.set_page_config(page_title="Body na kružnici", layout="centered")

# Záložky
tab1, tab2 = st.tabs(["📊 Úloha", "ℹ️ Informace o mně"])

with tab1:
    st.header("Výpočet a vizualizace")

    # Střed kružnice
    stred_input = st.text_input("Zadejte souřadnice středu (x,y)", "0,0")
    try:
        stred = tuple(map(float, stred_input.split(",")))
    except:
        stred = (0,0)
        st.warning("Zadejte souřadnice ve formátu x,y")

    polomer = st.number_input("Poloměr (m)", min_value=0.1, value=5.0)
    pocet_bodu = st.number_input("Počet bodů", min_value=1, value=8)
    barva = st.color_picker("Barva bodů", "#ff0000")

    # Výpočet bodů
    angles = np.linspace(0, 2*np.pi, int(pocet_bodu), endpoint=False)
    x = stred[0] + polomer * np.cos(angles)
    y = stred[1] + polomer * np.sin(angles)

    # Vykreslení grafu
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.grid(True)

    ax.scatter(x, y, color=barva)
    for i, (xx, yy) in enumerate(zip(x, y), start=1):
        ax.text(xx, yy, str(i), fontsize=8, ha="center", va="center")

    kruh = plt.Circle(stred, polomer, fill=False)
    ax.add_artist(kruh)

    st.pyplot(fig)

    # PDF export
    st.subheader("Export do PDF")
    jmeno = st.text_input("Vaše jméno")
    kontakt = st.text_input("Kontakt (email)")

    if st.button("Vytvořit PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200,10,txt="Výpočet bodů na kružnici", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200,10,txt=f"Jméno: {jmeno}", ln=True)
        pdf.cell(200,10,txt=f"Kontakt: {kontakt}", ln=True)
        pdf.cell(200,10,txt=f"Střed: {stred}", ln=True)
        pdf.cell(200,10,txt=f"Poloměr: {polomer} m", ln=True)
        pdf.cell(200,10,txt=f"Počet bodů: {pocet_bodu}", ln=True)
        pdf.cell(200,10,txt=f"Barva: {barva}", ln=True)
        pdf_file = "vystup.pdf"
        pdf.output(pdf_file)

        with open(pdf_file, "rb") as f:
            st.download_button("📥 Stáhnout PDF", f, file_name=pdf_file)

with tab2:
    st.header("ℹ️ Informace o mně")
    st.write("""
    **Autor:** Jan Novák  
    **Kontakt:** jan.novak@email.cz  
    **Použité technologie:**  
    - Python  
    - Streamlit  
    - Matplotlib  
    - NumPy  
    - FPDF  
    """)
