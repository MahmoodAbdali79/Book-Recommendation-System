import streamlit as st

st.markdown("# Main page")

multi = '''Here you can see two section:
\n - **Recommendation**: you can search you desire book and see related books.
\n - **Not found books**: If you search for books that we can't find related books for, we save them to improve our system.
'''
st.markdown(multi)

# st.markdown("This page built to show recommendation system as demo")
multi = '''
[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/MahmoodAbdali79/Book-Recommendation-System)
[![Website Icon](https://badgen.net/badge/icon/Website?icon=chrome&label)](https://mahmoodabdali79.github.io/Portfolio)
[![LinkedIn Icon](https://badgen.net/badge/icon/LinkedIn?icon=linkedin&label)](https://www.linkedin.com/in/mahmood-abdali)
'''
st.markdown(multi)




