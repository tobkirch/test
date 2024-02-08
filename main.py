import streamlit as st
import pandas as pd

# Funktion zum Hochladen einer CSV-Datei
def upload_csv():
    uploaded_file = st.file_uploader("CSV-Datei hochladen", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)  # Anzeigen der Daten aus der hochgeladenen CSV-Datei
            return df
        except pd.errors.EmptyDataError:
            st.error("Die hochgeladene CSV-Datei ist leer.")
            return None
    return None

# Funktion zum Speichern von Daten in der CSV-Datei
def save_to_csv(data, filename):
    data.to_csv(filename, index=False)

# Streamlit-Anwendung
def main():
    st.title("CSV Daten bearbeiten")

    # CSV-Datei hochladen
    st.header("CSV-Datei hochladen")
    df = upload_csv()
    if df is not None:
        st.dataframe(df)

        # Texteingaben machen
        st.header("Neuen Eintrag hinzufügen")
        text_input1 = st.text_input("Texteingabe 1")
        text_input2 = st.text_input("Texteingabe 2")

        # Debugging-Ausgabe
        st.write("DataFrame ist nicht None:", df is not None)
        st.write("DataFrame ist leer:", df.empty)

        # Button zum Speichern der Daten
        if st.button("Daten speichern"):
            if df is not None and not df.empty:
                new_entry = {'Text 1': text_input1, 'Text 2': text_input2}
                df = df.append(new_entry, ignore_index=True)
                save_to_csv(df, "updated_data.csv")
                st.success("Daten erfolgreich gespeichert!")
            else:
                st.error("Es wurde keine CSV-Datei hochgeladen oder die hochgeladene CSV-Datei ist leer.")

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
