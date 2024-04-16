import streamlit as st

st.title("These are books you did not find")


if 'NotFound'  in st.session_state:
    st.info('We use these to imporove oursystem', icon="ℹ️")
    for book in st.session_state['NotFound']:
        with st.container(height=60):
                    st.markdown(book)
else: 
    st.info('There is nothing to show', icon="ℹ️")