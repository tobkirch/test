import streamlit as st
import pandas as pd

# Funktion zum Hochladen einer CSV-Datei
def upload_csv():
    uploaded_file = st.file_uploader("CSV-Datei hochladen", type=["csv"])
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file, sep=";")
    return None

# Funktion zum Speichern von Daten in der CSV-Datei
def save_to_csv(data, filename):
    data.to_csv(filename, index=False, sep=";")

# Streamlit-Anwendung
def main():
    st.title("CSV Daten bearbeiten")

    # CSV-Datei hochladen
    st.header("CSV-Datei hochladen")
    df = upload_csv()
    if df is not None:
        st.dataframe(df)

        # Texteingaben machen
        st.header("Neue Einträge hinzufügen")
        text_input1 = st.text_input("Texteingabe 1")
        text_input2 = st.text_input("Texteingabe 2")

        # Button zum Speichern der Daten
        if st.button("Daten speichern"):
            new_entry = {'Spalte 1': text_input1, 'Spalte 2': text_input2}
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            save_to_csv(df, "updated_data.csv")
            st.success("Daten erfolgreich gespeichert!")

        # Button zum Herunterladen der CSV-Datei
        st.header("CSV-Datei herunterladen")
        if st.button("CSV-Datei herunterladen"):
            st.write("Herunterladen der CSV-Datei...")
            with open("updated_data.csv", "rb") as file:
                st.download_button(label="Klicke hier, um die aktualisierte CSV-Datei herunterzuladen",
                                   data=file,
                                   file_name="updated_data.csv",
                                   mime="text/csv")

if __name__ == "__main__":
    main()
