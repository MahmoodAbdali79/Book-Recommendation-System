from Model import recommend
import time
import streamlit as st

st.title("Let's find :green[book] :sunglasses:")

st.text_input("What was the last book you read? you can start with '1984' book ", key="name")
if len(st.session_state.name) != 0:
    respond = recommend(st.session_state.name)

    with st.spinner('Wait for it...'):
        time.sleep(1.5) 

    if None not in respond:
        for bookname, url in respond:
            with st.container(height=240):
                link = 'https://amazon.com'
                st.markdown(f'{bookname}: Buy from [amazone]({link})')
                # st.markdown(url)
                st.image(url)

    else:
        st.write("We can't find related book. write an other book please")

        if 'NotFound' not in st.session_state:
            st.session_state['NotFound'] = []
        st.session_state['NotFound'].append(st.session_state.name)
        

