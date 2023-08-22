import streamlit as st
from PIL import Image
from io import BytesIO
from utils.scrape import scrape_seriale
import requests
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Atanase Streamlit", page_icon="💪")

st.title("Seriale 📺")
st.text("")

st.sidebar.success("Select a page above.")


def resize_image(image, target_width, target_height):
    return image.resize((target_width, target_height))


try:
    seriale = scrape_seriale()
    num_rows = len(seriale) // 3
    target_width = 300  # Lățimea dorită a imaginilor
    target_height = 280  # Înălțimea dorită a imaginilor

    for i in range(num_rows):
        # Creează un layout cu trei coloane pentru fiecare rând
        col1, spacer, col2, spacer, col3 = st.columns([2, 0.1, 2, 0.1, 2])

        # Afișați imaginile și textul pentru fiecare coloană
        with col1:
            img_url = seriale[i * 3].img
            img = Image.open(BytesIO(requests.get(img_url).content))
            img = resize_image(
                img, target_width, target_height
            )  # Redimensionați imaginea

            st.image(img, caption=f"", use_column_width=True)

            # st.write(seriale[i * 3].title)
            if st.button(f"Vezi {seriale[i * 3].title}"):
                # Generați URL-ul pentru pagina de redirecționare cu parametrul URL

                st.session_state["serial_ales"] = seriale[i * 3]
                switch_page("Serial")

        with col2:
            img_url = seriale[i * 3 + 1].img
            img = Image.open(BytesIO(requests.get(img_url).content))

            img = resize_image(
                img, target_width, target_height
            )  # Redimensionați imaginea

            st.image(img, caption=f"", use_column_width=True)

            if st.button(f"Vezi {seriale[i * 3+1].title}"):
                # Generați URL-ul pentru pagina de redirecționare cu parametrul URL

                st.session_state["serial_ales"] = seriale[i * 3 + 1]
                switch_page("Serial")

        with col3:
            img_url = seriale[i * 3 + 2].img
            img = Image.open(BytesIO(requests.get(img_url).content))
            img = resize_image(
                img, target_width, target_height
            )  # Redimensionați imaginea

            st.image(img, caption=f"", use_column_width=True)

            if st.button(f"Vezi {seriale[i * 3+2].title}"):
                # Generați URL-ul pentru pagina de redirecționare cu parametrul URL

                st.session_state["serial_ales"] = seriale[i * 3 + 2]
                switch_page("Serial")
        st.text("")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")


# Pentru redirecționarea efectivă
