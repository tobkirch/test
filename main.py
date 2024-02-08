import streamlit as st
import pandas as pd
from github import Github
from io import StringIO

# GitHub Zugangsdaten
github_token = "IHR_GITHUB_TOKEN"
github_repo_owner = "IHR_REPO_OWNER"
github_repo_name = "IHR_REPO_NAME"
github_file_path = "daten.csv"

# Streamlit App Titel
st.title("Daten in CSV speichern")

# Textfeldeingaben
input1 = st.text_input("Eingabe 1")
input2 = st.text_input("Eingabe 2")

# Laden der bisherigen Daten von GitHub
g = Github(github_token)
repo = g.get_repo(f"{github_repo_owner}/{github_repo_name}")
contents = repo.get_contents(github_file_path)
csv_content = contents.decoded_content.decode('utf-8')
existing_df = pd.read_csv(StringIO(csv_content))

# Speichern Button
if st.button("Speichern"):
    # Neue Daten hinzufügen
    new_data = {"Eingabe 1": [input1], "Eingabe 2": [input2]}
    new_df = pd.DataFrame(new_data)
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    
    # CSV Datei auf GitHub aktualisieren
    repo.update_file(contents.path, "Daten aktualisiert", updated_df.to_csv(index=False), contents.sha)
    
    st.success("Daten erfolgreich gespeichert!")
