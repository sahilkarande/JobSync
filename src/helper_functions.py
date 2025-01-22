import os
import base64
import io
import re
import google.generativeai as genai
from dotenv import load_dotenv
import pdf2image 
# load environment Variables


# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Google API key not found. Please check your environment setup.")
genai.configure(api_key=api_key)


# Function to preview the uploaded resume PDF
def preview_pdf(uploaded_file):
    if uploaded_file:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=r'poppler-24.08.0\Library\bin')
        return images
    else:
        return None

# Helper function to extract match percentage
def extract_match_percentage(response):
    match = re.search(r"(\d+)%", response)
    return match.group(1) if match else "N/A"

# Function to get Gemini response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    return model.generate_content([input, pdf_content[0], prompt]).text

def extract_keywords(text):
    """ Extract keywords from a given text (job description or resume). """
    # This can be improved with NLP techniques, but for simplicity, we use basic tokenization
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def extract_experience(text):
    """ Extract the experience mentioned in the job description. """
    # Here, we're just looking for experience numbers in years (you can improve this)
    experience = re.search(r'(\d+)\s*(?:years?|yrs?|yr)', text, re.IGNORECASE)
    return int(experience.group(1)) if experience else 0  # Default to 0 if no experience found

def extract_experience_from_resume(text):
    """ Extract the experience mentioned in the resume. """
    experience = re.search(r'(\d+)\s*(?:years?|yrs?|yr)', text, re.IGNORECASE)
    return int(experience.group(1)) if experience else 0

def calculate_experience_relevance(jd_experience, resume_experience):
    """ Calculate experience relevance score. """
    if jd_experience == 0:  # If JD doesn't specify experience, treat it as 100% relevant
        return 100
    return min(100, (resume_experience / jd_experience) * 100)

def calculate_skills_relevance(jd_text, resume_text):
    """ Calculate skills relevance score based on matching skills. """
    jd_keywords = set(extract_keywords(jd_text))
    resume_keywords = set(extract_keywords(resume_text))

    # Get common keywords (skills) between job description and resume
    common_skills = jd_keywords.intersection(resume_keywords)

    # Calculate the relevance score as the percentage of common skills in the job description
    if len(jd_keywords) == 0:
        return 0  # Avoid division by zero if there are no keywords in JD
    return (len(common_skills) / len(jd_keywords)) * 100

def calculate_job_title_match(jd_text, resume_text):
    """ Calculate job title match percentage. """
    # A simple approach is to check if the job title in the JD matches any title in the resume
    job_titles = ["data scientist", "software engineer", "machine learning engineer", "developer", "analyst"]
    jd_title_found = any(title in jd_text.lower() for title in job_titles)
    resume_title_found = any(title in resume_text.lower() for title in job_titles)

    if not jd_title_found or not resume_title_found:
        return 0  # No match
    return 100 if jd_title_found and resume_title_found else 50

def calculate_certifications_match(jd_text, resume_text):
    """ Calculate certifications match between the job description and the resume. """
    # Define a list of common certifications
    certifications = ["certified data scientist", "machine learning", "aws certified", "google cloud", "pmp", "scrum master"]
    
    # Find certifications mentioned in JD and resume (convert to sets)
    jd_certifications = {cert for cert in certifications if cert in jd_text.lower()}
    resume_certifications = {cert for cert in certifications if cert in resume_text.lower()}

    # Calculate the match count using intersection of sets
    return len(jd_certifications.intersection(resume_certifications))

# Calculate Keyword Match Count
def calculate_keyword_match_count(jd_keywords, resume_keywords):
    return len(jd_keywords.intersection(resume_keywords))

# Calculate Experience Relevance Score
def calculate_experience_relevance(jd_experience, resume_experience):
    return 100 if resume_experience >= jd_experience else (resume_experience / jd_experience) * 100

# Setup PDF content extraction
def input_pdf_setup(uploaded_file):
    if uploaded_file:
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=r'poppler-24.08.0\Library\bin')
        img_byte_arr = io.BytesIO()
        images[0].save(img_byte_arr, format='JPEG')
        return [{"mime_type": "image/jpeg", "data": base64.b64encode(img_byte_arr.getvalue()).decode()}]
    raise FileNotFoundError("No file uploaded")