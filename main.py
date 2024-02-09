import streamlit as st
from PIL import Image

def main():
    st.title("Bildzuschnitts-App")
    st.write("Lade ein Bild hoch und wähle den Bereich aus, den du zuschneiden möchtest.")

    # Bild hochladen
    uploaded_image = st.file_uploader("Bild auswählen", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Bild anzeigen
        image = Image.open(uploaded_image)

        cropped_image = crop_image(image)
        # Zugeschnittenes Bild anzeigen
        st.image(cropped_image, caption="Zugeschnittenes Bild", use_column_width=True)

def crop_image (image):
     # Zuschnittbereich auswählen
        st.write("Wähle den Bereich aus, den du zuschneiden möchtest.")
        left = st.sidebar.slider("Linker Rand:", 0, image.width, 0)
        top = st.sidebar.slider("Oberer Rand:", 0, image.height, 0)
        right = st.sidebar.slider("Rechter Rand:", 0, image.width, image.width)
        bottom = st.sidebar.slider("Unterer Rand:", 0, image.height, image.height)

        # Bild zuschneiden
        cropped_image = image.crop((left, top, right, bottom))

        return cropped_image


if __name__ == "__main__":
    main()
