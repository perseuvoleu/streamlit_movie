import streamlit as st


st.set_page_config(
    page_title="Pagina de Redirecționare",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded",
)
if "serial_ales" not in st.session_state:
    st.session_state["serial_ales"] = ""
    st.title("Pagina nu a fost gasita")
else:
    try:
        st.title(st.session_state["serial_ales"].title + "")
        st.session_state["serial_ales"].scrape_video()
        st.session_state.serial_ales = [
            x for x in st.session_state["serial_ales"].videos
        ]
    except:
        st.title("Pagina nu a fost gasita")


if len(st.session_state.serial_ales) > 0:
    for idx, episod in enumerate(st.session_state.serial_ales):
        val = "Episodul {}".format(str(idx + 1))
        st.markdown(f"## {val}")

        iframe = episod.split("video/")[1]
        # st.video(video_url)
        # print(iframe)
        ifram = """
<iframe width="100%" height="500px" src="//ok.ru/videoembed/{}" allowfullscreen frameborder="0" webkitAllowFullScreen="true" mozAllowFullScreen="true"></iframe>
""".format(
            iframe
        )
        st.markdown(ifram, unsafe_allow_html=True)
