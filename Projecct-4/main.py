import streamlit as st
import google.generativeai as genai
import config

# API Key Configuration
api_key = config.key
genai.configure(api_key=api_key)

# Configure Streamlit page settings
st.set_page_config(
    page_title="AI Code Reviewer",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS Styling
st.markdown(
    """
  <style>
      /* Global background */
      .stApp {
          background: #f4f6f9;
      }

      /* Title styling */
      .header-title {
          font-size: 3em;
          font-weight: 600;
          color: #343a40;
          text-align: center;
          margin-top: 30px;
          font-family: 'Arial', sans-serif;
      }

      /* Text area styling */
      textarea {
          background: #ffffff;
          border: 2px solid #007bff;
          color: #495057;
          border-radius: 8px;
          font-size: 16px;
          padding: 12px;
          width: 100%;
          height: 250px;
          resize: none;
      }

      /* Button styling */
      button[kind="primary"] {
          background-color: #007bff !important;
          color: white !important;
          border-radius: 50px !important;
          font-size: 18px !important;
          padding: 15px 30px !important;
          margin-top: 20px;
          border: none !important;
          box-shadow: 0 4px 6px rgba(0, 123, 255, 0.3);
          cursor: pointer;
          transition: all 0.3s ease;
      }

      button[kind="primary"]:hover {
          background-color: #0056b3 !important;
      }

      /* Sidebar styling */
      .sidebar .sidebar-content {
          background-color: #343a40;
          color: white;
      }

      .sidebar .sidebar-content h1, .sidebar .sidebar-content h2 {
          color: #ffffff;
      }

      /* Subheader and content section */
      .stMarkdown h2 {
          color: #343a40;
          font-weight: 600;
      }

      /* Review Section Styling */
      .review-section {
          background-color: #ffffff;
          border-radius: 10px;
          padding: 20px;
          box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
          max-width: 100%;
          overflow: auto;
          margin-top: 30px;
      }

      .review-section pre {
          background-color: #f8f9fa;
          border: 1px solid #ddd;
          padding: 15px;
          border-radius: 5px;
          color: #495057;
          font-size: 16px;
          white-space: pre-wrap;
          word-wrap: break-word;
          height: auto;  /* Prevent slider */
          max-height: 600px;  /* Ensure the output area grows without a slider */
          overflow-y: auto;  /* Only scroll if necessary */
      }
  </style>
  """,
    unsafe_allow_html=True,
)

# Sidebar content
st.sidebar.title("Code Review Assistant")
st.sidebar.subheader("How to use?")
st.sidebar.write("1. Paste your Python code in the text box below.")
st.sidebar.write("2. Click the button to analyze the code.")
st.sidebar.markdown("---")
st.sidebar.write("Designed to help you review and debug your Python code efficiently.")

# Title Section
st.markdown('<div class="header-title">AI Code Reviewer</div>', unsafe_allow_html=True)

# Description
st.write(
    "Welcome to the **AI Code Reviewer**! Paste your Python code in the box below and click **Analyze Code** to receive detailed feedback on potential issues."
)

# Code Input Area
input_code = st.text_area("📝 Paste your Python code here:", "")

# Button to trigger code analysis
if st.button("🔍 Analyze Code"):
    if input_code:
        # Initialize Generative Model
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        # Start chat and send code for review
        chatbot = model.start_chat(history=[])
        review_response = chatbot.send_message(f"Please analyze the following Python code for bugs:\n{input_code}")

        # Display the AI feedback in a styled section
        st.markdown('<div class="review-section">', unsafe_allow_html=True)
        st.subheader("🧐 Code Review Feedback")
        st.markdown("**Bug Report:**")
        st.code(review_response.text, language='python')  # Show AI review result
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("❌ Please paste some code to analyze before proceeding!")

# Footer Section (optional)
st.markdown("---")
# st.markdown("Made by Harsha Vardhini")

