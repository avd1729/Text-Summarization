# Text-Summarization

# Text Summarizer in Streamlit using Hugging Face Library

## Overview

This is a simple web application built with Streamlit that utilizes the Hugging Face Transformers library to perform text summarization. With this tool, you can input a long piece of text and generate a concise summary of it. Whether you want to summarize articles, research papers, or any other type of content, this app makes it easy and efficient.

## Features

- Input any text for summarization.
- Choose from different models for summarization.
- Adjust the length of the summary.
- Receive instant summaries.

## Prerequisites

Before you begin using this application, make sure you have the following installed:

- Python (3.6 or higher)
- Pip (Python package manager)
- Streamlit (`pip install streamlit`)
- Hugging Face Transformers (`pip install transformers`)

## Getting Started

1. Clone this repository or download the project files to your local machine.

2. Open a terminal and navigate to the project directory.

3. Install the required Python packages if you haven't already:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. A new browser window/tab should open automatically with the Text Summarizer app.

## Usage

1. In the Streamlit app, you'll see a text input area where you can paste or type the text you want to summarize.

2. Choose a pre-trained model from the dropdown menu. You can experiment with different models to see which one provides the best summary for your input.

3. Adjust the "Max Summary Length" slider to control the length of the generated summary. Longer values will result in more extensive summaries.

4. Click the "Generate Summary" button to generate the summary.

5. The generated summary will appear below the input area.

6. You can copy the summary to your clipboard using the "Copy to Clipboard" button.

## Customization

Feel free to customize this app according to your needs. You can modify the following aspects:

- **UI Design**: You can change the layout, colors, and styling by editing the Streamlit app's code in `app.py`.

- **Models**: You can add or remove pre-trained models from the `MODELS` dictionary in `app.py`.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.

2. Clone the forked repository to your local machine.

3. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/my-new-feature
   ```

4. Make your changes and commit them:

   ```bash
   git commit -m "Add my new feature"
   ```

5. Push your changes to your forked repository:

   ```bash
   git push origin feature/my-new-feature
   ```

6. Create a pull request on the original repository, explaining your changes and why they should be merged.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [OpenAI GPT-3](https://openai.com/)
- [Your Name / Your Team Name]

Feel free to replace "[Your Name / Your Team Name]" with your name or the name of your team if you'd like to give credit to anyone specific.


![Screenshot (286)](https://github.com/avd1729/Text-Summarization/assets/94891044/f9f7816d-3693-4852-915e-ab7c9d5b3f68)
![Screenshot (287)](https://github.com/avd1729/Text-Summarization/assets/94891044/8d8a2710-7b53-4e56-9c51-895a1a58e1ca)
