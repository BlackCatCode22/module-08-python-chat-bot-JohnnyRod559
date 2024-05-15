# pip install streamlit langchain openai
import streamlit as st
from langchain import document_loaders
import openai

# User-defined function for generating a response
def generate_response(user_input):
    try:
        if isinstance(user_input, str):
            # If user input is a string, assume it's text input
            text = user_input
        else:
            # If user input is a file, assume it's a PDF and process it using Langchain
            doc = document_loaders.from_path(user_input.name)
            text = doc.text

        # Call the OpenAI API to generate a response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Assume the role of a teacher, and think step by step. Your name is Skippy Py."},
                      {"role": "user", "content": text}]
        )

        # Extract the text of the response
        response_text = completion['choices'][0]['message']['content']
        return response_text
    except Exception as e:
        # Print an error message if there's an exception
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate a response."

# Define the Streamlit app
def main():
    # Set up Streamlit app title and description
    st.title("Python Study Bot")
    st.write("Welcome to the Python Study Bot! Type your question or upload a PDF document.")

    # File uploader for PDF documents
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    # Text input field for user input
    user_input = st.text_input("Python student question:")

    # Button to submit the question
    if st.button("Ask"):
        if uploaded_file is not None:
            # If a PDF file is uploaded, process it
            response = generate_response(uploaded_file)
        else:
            # Otherwise, use the user input directly
            response = generate_response(user_input)

        # Display the response
        st.write("Python Study Bot:", response)

if __name__ == "__main__":
    # Set your OpenAI API key
    openai.api_key = "sk-proj-6Xf3F8esHtMIJLIFpxGnT3BlbkFJU84bnri3AtnaeLYkJgsN"

    # Run the Streamlit app
    main()
