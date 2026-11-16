import streamlit as st

st.set_page_config(page_title="My Machine Learning  App")

# Light Theme CSS
st.markdown("""
<style>
.stApp {
    background-color: #fff5f7;
}

h1 {
    color: #d63384;
    text-align: center;
}

h2, h3 {
    color: #b83280;
}

.stButton button {
    background-color: #f4a6c1;
    color: white;
    border-radius: 10px;
    border: none;
}

.stButton button:hover {
    background-color: #e879a5;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title(" My Machine Learning App    ")
st.markdown(
    "<p style='text-align: center;'>Welcome to my application!</p>",
    unsafe_allow_html=True
)

st.divider()

# User Input
st.subheader("User Information")

name = st.text_input("Enter your name")

# Submit Button
if st.button("Submit"):
    if name:
        st.success("Hello, " + name + "! Welcome.")
    else:
        st.warning("Please enter your name.")

