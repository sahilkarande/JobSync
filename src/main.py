import base64
import io
import streamlit as st
import pdf2image
from helper_functions import (
    get_gemini_response,
    extract_match_percentage,
    extract_keywords,
    calculate_keyword_match_count,
    calculate_experience_relevance,
    input_pdf_setup,
    preview_pdf,
)

# Streamlit Layout and UI Setup
st.set_page_config(page_title="JobSync", page_icon="../assets/Icons.ico", layout="wide", initial_sidebar_state="expanded")
cover_image_path = "../assets/JobSync_Cover_image.png"
st.image(cover_image_path)
st.title("🎯 JobSync")
st.markdown("### Evaluate your resume's alignment with job descriptions.")

# Input section
col1, col2 = st.columns(2)
with col1:
    st.subheader("Enter Job Description")
    input_text = st.text_area("Paste the job description below:", height=78)
with col2:
    st.subheader("Upload Your Resume")
    uploaded_file = st.file_uploader("Upload your resume as a PDF file:", type=["pdf"])

# New Section: Custom Query Input
st.markdown("---")
st.subheader("🔍 Ask a Custom Query")
user_query = st.text_input("Enter your query (e.g., skills, experience, certifications):")

# Horizontal Action Buttons
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)

# Initialize the selected_action variable
selected_action = None  # To store the selected action for dynamic subheader
with col1:
    if st.button("📄 Evaluate Resume"):
        selected_action = "📄 Evaluate Resume"
with col2:
    if st.button("📊 Match Percentage"):
        selected_action = "📊 Match Percentage"
with col3:
    if st.button("💡 Resume Improvement Suggestions"):
        selected_action = "💡 Resume Improvement Suggestions"
with col4:
    if st.button("📝 Areas of Improvement"):
        selected_action = "📝 Areas of Improvement"
with col5:
    if st.button("👁️ Preview Resume"):
        selected_action = "👁️ Preview Resume"

# Function to preview the uploaded resume
def preview_pdf(uploaded_file):
    if uploaded_file:
        # Read file content as bytes
        file_bytes = uploaded_file.read()
        # Convert the PDF to images
        images = pdf2image.convert_from_bytes(file_bytes, poppler_path=r'poppler-24.08.0\Library\bin')
        st.image(images[0], caption="Preview of your Resume", use_container_width=True)
    else:
        st.warning("⚠️ Please upload a resume to preview.")

# Preview PDF Button Action
if selected_action == "👁️ Preview Resume":
    preview_pdf(uploaded_file)

# Processing Section for other actions
if selected_action:
    if not uploaded_file:
        st.warning("⚠️ Please upload a resume to proceed.")
    elif not input_text.strip():
        st.warning("⚠️ Please provide a job description.")
    else:
        with st.spinner("Processing your resume..."):
            try:
                # Extract PDF content and process with the selected prompt
                pdf_content = input_pdf_setup(uploaded_file)
                prompt = ""

                # Assign the appropriate prompt based on the selected action
                if selected_action == "📄 Evaluate Resume":
                    prompt = "Please evaluate the resume against the job description."
                elif selected_action == "📊 Match Percentage":
                    prompt = "Evaluate the resume's match with the job description and provide a match percentage."
                elif selected_action == "💡 Resume Improvement Suggestions":
                    prompt = "Provide suggestions for improving the resume."
                elif selected_action == "📝 Areas of Improvement":
                    prompt = "Provide feedback on areas that need improvement."
                elif selected_action == "📈 Analysis":
                    prompt = "Analyze the resume and provide metrics such as match percentage, keyword matches, and experience relevance."

                # Get response from Gemini model
                response = get_gemini_response(input_text, pdf_content, prompt)

                # Metrics calculation for Analysis or Match Percentage
                if selected_action == "📈 Analysis":
                    match_percentage = extract_match_percentage(response)
                    jd_keywords = extract_keywords(input_text)
                    resume_keywords = extract_keywords(response)
                    keyword_match_count = calculate_keyword_match_count(jd_keywords, resume_keywords)

                    jd_experience = 3  # Example value, replace dynamically if possible
                    resume_experience = 2  # Example value, replace dynamically if possible
                    experience_relevance_score = calculate_experience_relevance(jd_experience, resume_experience)

                # Analysis Section
                if selected_action == "📈 Analysis":
                    st.subheader("📈 Analysis")
                    st.metric(label="Resume Match Percentage", value=f"{match_percentage}%", delta=None)
                    st.metric(label="Keyword Match Count", value=f"{keyword_match_count} matches", delta=None)
                    st.metric(label="Experience Relevance Score", value=f"{experience_relevance_score}%", delta=None)

                # Display specific responses for other buttons
                if selected_action in ["📄 Evaluate Resume", "💡 Resume Improvement Suggestions", "📝 Areas of Improvement", "📊 Match Percentage"]:
                    st.subheader(selected_action)  # Dynamic subheader based on selected action
                    st.success(response)  # Display the response for the selected action

            except Exception as e:
                st.error(f"❌ Error: {e}")

# New feature for custom query
if user_query:
    if not uploaded_file or not input_text.strip():
        st.warning("⚠️ Please upload a resume and provide a job description to process your query.")
    else:
        with st.spinner("Processing your custom query..."):
            try:
                # Extract PDF content
                pdf_content = input_pdf_setup(uploaded_file)  # Add this line to process the uploaded file

                # Combine the user query with the job description and resume content
                custom_prompt = f"Job Description: {input_text}\nResume: {pdf_content[0]}\nQuery: {user_query}"

                # Get response from Gemini model for the custom query
                custom_response = get_gemini_response(input_text, pdf_content, custom_prompt)
                st.subheader("🔍 Custom Query Response")
                st.success(custom_response)  # Display the response for the custom query

            except Exception as e:
                st.error(f"❌ Error: {e}")


# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 14px;'>Made with ❤️ by Sahil | Powered by Google Generative AI & Streamlit</p>",
    unsafe_allow_html=True,
)
