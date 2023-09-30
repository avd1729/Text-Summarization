
# Text Summarizer in Streamlit using Hugging Face Library

![Screenshot (287)](https://github.com/avd1729/Text-Summarization/assets/94891044/8d8a2710-7b53-4e56-9c51-895a1a58e1ca)


## Overview

This is a simple web application built with Streamlit that utilizes the Hugging Face Transformers library to perform text summarization. With this tool, you can input a long piece of text and generate a concise summary of it. Whether you want to summarize articles, research papers, or any other type of content, this app makes it easy and efficient.


## Prerequisites

Before you begin using this application, make sure you have the following installed:

- Python (3.6 or higher)
- Pip (Python package manager)
- Streamlit (`pip install streamlit`)
- Hugging Face Transformers (`pip install transformers`)

## Getting Started

1. Clone this repository or download the project files to your local machine.

2. Open a terminal and navigate to the project directory.

3. Since the model is 1.14 GB , it cannot be hosted in github , so run the summarizer.ipynb file to create the model.pkl file

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. A new browser window/tab should open automatically with the Text Summarizer app.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)


