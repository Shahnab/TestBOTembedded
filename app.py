import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

col1, mid, col2= st.columns([1,1,20])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/122/122482.png", width=70)
with col2:
    st.markdown("# Carlsberg Concierge: Your Personal Life, Business and Career Coach")

# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://ora.sh/embed/691f153b-12db-4243-b1d2-2eb069118ffc", width=1500, height=550, scrolling=True)
