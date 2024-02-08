import streamlit as st
import pandas as pd
from github import Github

# GitHub Zugangsdaten
github_token = st.secrets["GH_Token"]
github_repo_owner = "tobkirch"
github_repo_name = "test"
github_file_path = "ergebnisse.csv"

# Streamlit App Titel
st.title("Daten in CSV speichern")

# Textfeldeingaben
input1 = st.text_input("Eingabe 1")
input2 = st.text_input("Eingabe 2")

# Speichern Button
if st.button("Speichern"):
    # Daten in DataFrame speichern
    data = {"Eingabe 1": [input1], "Eingabe 2": [input2]}
    df = pd.DataFrame(data)
    
    # GitHub Verbindung herstellen
    g = Github(github_token)
    repo = g.get_repo(f"{github_repo_owner}/{github_repo_name}")
    
    # CSV Datei auf GitHub aktualisieren
    contents = repo.get_contents(github_file_path)
    repo.update_file(contents.path, "Daten aktualisiert", df.to_csv(index=False), contents.sha)
    
    st.success("Daten erfolgreich gespeichert!")
