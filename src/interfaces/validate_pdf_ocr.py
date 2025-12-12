import streamlit as st
import detect_pdf as ipdf 

st.title("Validation des Extractions OCR")
uploaded_file = st.file_uploader("Choisir un PDF", type="pdf")
if uploaded_file:
    st.write("nom du fichier : ",uploaded_file.name)
    text ,table,pdf_type = ipdf.extract_text(f"../data/{uploaded_file.name}")
    st.write("PDF type : ",pdf_type)
    st.text_area("Texte extrait", text, height=300)
    if st.button("Valider"):
        st.success("Texte validé !")