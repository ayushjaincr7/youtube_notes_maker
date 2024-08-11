# YouTube Notes Maker

## How to Use

1. **Install Dependencies:**  
   Run the following command to install the necessary Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
2. **Set Up Environment Variables:**<br>
   Create a .env file in the root directory of your project. Inside this file, provide your Google Generative AI API key:
  ```bash
    GOOGLE_API_KEY=your_api_key_here
  ```
3. **Launch the Application:**
   To start the app, run:
    ```bash
    streamlit run app.py
    ```


**Simple Use of LangChain**

1. Retrieve YouTube Transcript:
The app utilizes the youtube_transcript_api library to fetch the transcript of a YouTube video.
2. Convert Transcript to Text Paragraphs:
The transcript is then processed and converted into coherent text paragraphs.
3. Generate Summarized Notes:
A PromptTemplate is used to format the text paragraphs, which are then fed into a language model (LLM) via LangChain. The model processes the input and generates a summarized response.
4.	Display the Results:
The generated notes are displayed on the web page using Streamlit’s markdown feature, providing a clean and readable format.
