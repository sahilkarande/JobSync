# JobSync - Resume Evaluation and Job Matching

![JobSync Thumbnail](..\assets\JobSync.png)

JobSync is a web-based application developed using Streamlit to help job seekers evaluate the alignment of their resumes with job descriptions. It offers various functionalities such as matching percentages, resume improvement suggestions, custom queries on resumes, and more. This project utilizes Google's Gemini AI for natural language processing tasks, such as matching resumes with job descriptions, extracting keywords, and suggesting areas for improvement.

## Features

- **Enter Job Description:** Users can paste a job description into the input field.
- **Upload Resume:** Upload your resume in PDF format for evaluation.
- **Match Percentage:** Evaluate how closely the uploaded resume matches the job description.
- **Resume Improvement Suggestions:** Get suggestions on how to improve your resume.
- **Areas of Improvement:** Provides feedback on specific areas of the resume that need attention.
- **Preview Resume:** View a preview of the uploaded resume.
- **Custom Query:** Ask custom queries (e.g., skills, experience, certifications) based on the resume and job description.

## Requirements

- Python 3.x
- Streamlit
- Google Gemini AI (via the `google-generativeai` package)
- `pdf2image` for rendering PDF resumes
- `poppler-utils` for PDF-to-image conversion
- `dotenv` for loading environment variables
- Install required packages using `requirements.txt` or manually as shown below.

### Install Dependencies

1. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Install Poppler (for converting PDFs to images):
    - [Download Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) or use your system's package manager for Linux/Mac.
  
3. Set up environment variables:
    - Create a `.env` file in the root directory and add your `GOOGLE_API_KEY`:
        ```ini
        GOOGLE_API_KEY=your_google_api_key
        ```

## Usage

### Running the Streamlit App

1. Run the application using Streamlit:
    ```bash
    streamlit run main.py
    ```

2. The app will open in your browser at `http://localhost:8501`.

### Functionalities

- **Enter Job Description:** Paste a job description in the provided text area. This will be compared with the uploaded resume.
- **Upload Resume:** Upload your resume in PDF format.
- **Evaluate Resume:** Click on "📄 Evaluate Resume" to evaluate how well your resume matches the job description.
- **Match Percentage:** Get a percentage of how well the resume matches the job description.
- **Resume Improvement Suggestions:** Get actionable suggestions to improve your resume.
- **Areas of Improvement:** View the areas of your resume that require improvement.
- **Preview Resume:** View a preview of your uploaded resume.
- **Custom Query:** Ask specific questions about the resume (e.g., "Does this resume have experience in Python?" or "Is this resume suitable for a Data Scientist role?").

## Code Overview

### main.py

This is the main entry point for the application, where the Streamlit app is set up, and the user interface components are defined.

- **Streamlit Layout:** The layout consists of sections for entering job descriptions, uploading resumes, and interacting with the app.
- **Actions:** The app allows users to click buttons to evaluate the resume, get match percentages, or see improvement suggestions.
- **PDF Preview:** Uploaded PDF resumes are previewed using the `pdf2image` library, allowing users to see their resume before making evaluations.
- **Custom Query:** Users can input custom queries related to their resume and job description, and the app responds based on AI analysis.

### helper_functions.py

Contains the helper functions that handle the core functionalities of the project:

- **get_gemini_response:** This function interacts with the Google Gemini AI model to generate responses based on the job description and resume content.
- **PDF Processing:** Extracts content from the uploaded PDF and processes it for comparison.
- **Keyword Matching:** Extracts keywords from both job descriptions and resumes for comparison and matching.
- **Experience and Relevance Calculation:** Calculates experience relevance and the match percentage between the resume and job description.

## Examples

### Upload a PDF Resume
- Upload your resume by clicking the **Upload Your Resume** section and selecting your PDF file.
  
### Enter Job Description
- Paste the job description into the text area, describing the role you're applying for.

### Evaluate Resume
- Click **📄 Evaluate Resume** to analyze your resume's match with the job description.

### Match Percentage
- Click **📊 Match Percentage** to see how much of your resume aligns with the job description, expressed as a percentage.

### Custom Query
- Enter any custom query related to the resume (e.g., "Does the resume include Python skills?").

### Preview Resume
- Click **👁️ Preview Resume** to view a preview of your uploaded resume.

## Development

### Folder Structure

```plaintext
.
├── assets
│   ├── Icons.ico
│   ├── cover.png
├── .env
├── helper_functions.py
├── main.py
├── requirements.txt
└── README.md
```

- **assets:** Contains image assets such as the app icon and cover image.
- **helper_functions.py:** Contains utility functions for PDF processing, resume evaluation, and matching logic.
- **main.py:** The main Streamlit app file.
- **requirements.txt:** Lists the required Python packages for the project.

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to fork this repository, create pull requests, and contribute improvements. Please follow standard open-source contribution guidelines.

## Contact

Made with ❤️ by Sahil.

For any issues or feature requests, please reach out via email at [skarande220@gmail.com](mailto:skarande220@gmail.com)
