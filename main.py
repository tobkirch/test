import streamlit as st
from github import Github

# Streamlit App
def main():
    st.title("Text in GitHub Datei schreiben")

    # Texteingabefelder
    text1 = st.text_input("Text 1 eingeben")
    text2 = st.text_input("Text 2 eingeben")

    # Button zum Speichern
    if st.button("Speichern"):
        # GitHub-Repository konfigurieren
        github_token = "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"
        github_repo_owner = "tobkirch"
        github_repo_name = "test"
        github_file_path = "ergebnisse.txt"

        # GitHub-Client initialisieren
        g = Github(github_token)
        repo = g.get_user(github_repo_owner).get_repo(github_repo_name)
        contents = repo.get_contents(github_file_path)

        # Texte in Datei schreiben
        updated_content = f"{text1}\n{text2}"
        repo.update_file(contents.path, "Updated via Streamlit", updated_content, contents.sha)

        st.success("Text erfolgreich in GitHub Datei gespeichert!")

if __name__ == "__main__":
    main()
