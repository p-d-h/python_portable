import streamlit as st

# https://emojipedia.org/
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"
)

# https://discuss.streamlit.io/t/reduce-white-space-top-of-the-page/21737/6
# st.markdown("""
#         <style>
#                .block-container {
#                     padding-top: 1rem;
#                     padding-bottom: 1rem;
#                     padding-left: 1rem;
#                     padding-right: 1rem;
#                 }
#         </style>
#         """, unsafe_allow_html=True)

st.write("# Welcome to PythonPortable 👋")
st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)