import streamlit as st

st.set_page_config(
    page_title="AI Note App",
    page_icon="📝",
    layout="wide"
)

st.title("AI Note Generation")
st.caption("Generation clean,Readable notes from AI(Markdown render)")

st.sidebar.header("⚙️ Controls")
use_ai = st.sidebar.checkbox("use AI", value=True)
