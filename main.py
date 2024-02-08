import streamlit as st
import pandas as pd

def main():
    st.title("CSV Datei hochladen und anzeigen")

    # CSV-Datei hochladen
    uploaded_file = st.file_uploader("CSV-Datei hochladen", type=["csv"])

    if uploaded_file is not None:
        # DataFrame aus der hochgeladenen CSV-Datei erstellen
        df = pd.read_csv(uploaded_file)

        # Daten ausgeben
        st.write("Inhalte der CSV-Datei:")
        st.dataframe(df)

if __name__ == "__main__":
    main()
