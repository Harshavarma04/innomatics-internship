import streamlit as st
import google.generativeai as ai
import config

# title of Streamlit
st.title("Data Science Tutor App :")

# user query field
user_prompt = st.text_input("Enter Query:", placeholder="Type query here...")

# Button to generate the answer
btn_click = st.button("Generate Answer")

key= config.key
# Check the key is read successfully
if key:
    ai.configure(api_key=key)

    # System instructions for the AI model
    sys_prompt = """
    You are a helpful AI tutor for data science.
    Students will ask you doubts related to various topics in Data Science.
    You are expected to reply in as much detail as possible.
    Make sure to take examples while explaining the concepts.
    In case a student asks any question outside the data science scope,
    politely decline and tell them to ask questions within the data science domain only.
    """

    # Load the model
    model = ai.GenerativeModel(model_name="models/gemini-1.5-flash-8b-latest", system_instruction=sys_prompt)

    # Generate response when button is clicked
    if btn_click:
        if user_prompt.strip():  # Check if the user input is not empty
            try:
                response = model.generate_content(user_prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Error generating content: {str(e)}")
        else:
            st.warning("Please enter a valid query.")
else:
    st.error("API key is not available or invalid.")